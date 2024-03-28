# Creating Amazon S3 Endpoint in Virtual Private Cloud

Para crear un endpoint S3, siga los pasos que se describen a continuación:

## Step 1 - Create IAM User with required permission

1. Abra la consola de Amazon IAM

2. 

## Step 2 - Create a gateway endpoint

1. Abra la consola de Amazon VPC. 

2. En el panel de navegación, elija **Endpoints**.

3. Click en el botón **“Create Endpoint”**

4. En **Service Category**, elija **AWS services**.

5. En **Services**, agregue el filtro **Type: Gateway** y seleccione **com.amazonaws.** region **.s3**

6. En **VPC**, seleccione la VPC en la que desea crear el endpoint.

7. En **Route tables**, seleccione las tablas de enrutamiento que debe utilizar el endpoint. De forma automática, se agregará una ruta para dirigir el tráfico destinado del servicio a la interfaz de red del endpoint.

8. En **Policy**, seleccione **Custom** para adjuntar una política de endpoint de VPC que controle los permisos que tienen las entidades principales para realizar acciones en los recursos a través del endpoint de VPC.

9. Click en **Create endpoint**.



Also, you will need to select the route tables that will be used by the endpoint. All subnets associated with selected route tables will be able to access this S3 endpoint.

4. After you created your AWS S3 endpoint, you need to allow HTTP and HTTPS connections to this S3 VPC endpoint. Get back to the Amazon VPC console, click “Security Groups”, choose a security group associated with your Amazon S3 VPC, go to “Outbound Rules”, press “Edit”. You need to allow connections via ports 443 and 80 and specify your endpoint as a destination.

5. Ensure that your bucket is located in the exact same region as the EC2 instance. You can do that in the MSP360 Backup's settings. Select your S3 account on the main toolbar.

