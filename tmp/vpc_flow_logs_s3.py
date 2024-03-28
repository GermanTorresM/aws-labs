import pulumi
import pulumi_aws as aws

# Crear un bucket de S3 para almacenar los logs de flujo
flow_log_bucket = aws.s3.Bucket('flow-log-bucket')

# Crear un VPC
vpc = aws.ec2.Vpc("my-vpc", cidr_block="10.0.0.0/16")

# Crear una política de IAM para permitir la publicación de logs en S3
flow_log_policy_document = aws.iam.get_policy_document(statements=[
    aws.iam.GetPolicyDocumentStatementArgs(
        actions=["s3:GetBucketAcl", "s3:GetBucketPolicy"],
        resources=[flow_log_bucket.arn],
    ),
    aws.iam.GetPolicyDocumentStatementArgs(
        actions=["s3:PutObject"],
        resources=[flow_log_bucket.arn.apply(lambda arn: f"{arn}/*")],
        conditions=[
            aws.iam.GetPolicyDocumentStatementConditionArgs(
                test="StringEquals",
                variable="s3:x-amz-acl",
                values=["bucket-owner-full-control"]
            )
        ]
    )
])

flow_log_role = aws.iam.Role('flow-log-role',
    assume_role_policy=aws.iam.get_policy(
        version="2012-10-17",
        statements=[
            aws.iam.GetPolicyStatementArgs(
                effect="Allow",
                principals=[
                    aws.iam.GetPolicyStatementPrincipalArgs(
                        type="Service",
                        identifiers=["vpc-flow-logs.amazonaws.com"]
                    )
                ],
                actions=["sts:AssumeRole"],
            )
        ]
    ).json
)

flow_log_role_policy = aws.iam.RolePolicy('flow-log-role-policy',
    role=flow_log_role.id,
    policy=flow_log_policy_document.json
)

# Crear un Flow Log para el VPC y configurar la entrega de registros al bucket de S3
flow_log = aws.ec2.FlowLog("vpc-flow-log",
    iam_role_arn=flow_log_role.arn,
    log_destination=flow_log_bucket.arn,
    log_destination_type="s3",
    traffic_type="ALL",
    vpc_id=vpc.id
)

# Exportar la URL del bucket y el ID del Flow Log
pulumi.export("bucket_url", flow_log_bucket.website_endpoint)
pulumi.export("flow_log_id", flow_log.id)