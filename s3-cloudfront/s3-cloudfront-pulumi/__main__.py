import mimetypes
import os

import pulumi
import pulumi_aws as aws

from pulumi import FileAsset, export

# Create an AWS resource (S3 Bucket)
bucket = aws.s3.Bucket("s3-cloudfront-demo-123",
    acl="private",
    tags={
        "Name": "s3-cloudfront-demo-123",
    }

)

content_dir = "www"
for file in os.listdir(content_dir):
    filepath = os.path.join(content_dir, file)
    mime_type, _ = mimetypes.guess_type(filepath)
    obj = aws.s3.BucketObject(file,
        bucket=bucket.id,
        source=FileAsset(filepath),
        content_type=mime_type)
    
# Export the name of the bucket
pulumi.export("bucketName", bucket.id)