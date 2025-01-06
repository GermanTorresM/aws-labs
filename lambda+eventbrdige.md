
## Breve descripción

Use AWS Lambda y Amazon EventBridge para detener e iniciar automáticamente las instancias de Amazon EC2.

Nota: La siguiente resolución es un ejemplo de solución simple. Para una solución más avanzada, use AWS Instance Scheduler. Para obtener más información, consulte Automatizar el inicio y la detención de instancias de AWS.

Para usar Lambda con el fin de detener e iniciar instancias de EC2 a intervalos regulares, complete los siguientes pasos:

1. Cree una política de AWS Identity and Access Management (IAM) y un rol de IAM personalizados para su función de Lambda.

2. Cree funciones de Lambda que detengan e inicien sus instancias de EC2.

3. Pruebe sus funciones de Lambda.

4. Cree horarios en EventBridge que ejecuten la función siguiendo una programación.

   Nota: También puede crear reglas que reaccionen a los eventos en su cuenta de AWS.


## Resolución

**Nota:Después de completar los pasos siguientes, es posible que reciba un error de ** cliente al iniciar. Para obtener más información, consulte Cuando inicio mi instancia con volúmenes cifrados adjuntos, la instancia se detiene inmediatamente y aparece el error «error del cliente al iniciar.»

Obtenga los ID de las instancias de EC2 que desee detener e iniciar. A continuación, siga los siguientes pasos.

### Cree una política y un rol de IAM para la función de Lambda

1. Use el editor de políticas JSON para crear una política de IAM. Pegue el siguiente documento de la política JSON en el editor de políticas:

   ```json
   {  "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "logs:CreateLogGroup",
           "logs:CreateLogStream",
           "logs:PutLogEvents"
          ],
          "Resource": "arn:aws:logs:*:*:*"
        },
        {
          "Effect": "Allow",
          "Action": [
            "ec2:Start*",
            "ec2:Stop*"
          ],
          "Resource": "*"
        }
     ]
   }
   ```

2. Cree un rol de IAM para Lambda.
   
   __Importante:__ Cuando adjunte una política de permisos a Lambda, asegúrese de elegir la política de IAM.

Nota: Si usa un volumen de Amazon Elastic Block Store (Amazon EBS) cifrado mediante una clave de AWS Key Management Service (AWS KMS) gestionada por el cliente, añada kms:CreateGrant a la política de IAM.

### Cree funciones de Lambda que detengan e inicien las instancias

1. Abra la consola de Lambda y, a continuación, elija Crear una función.

2. Elija Autor desde cero.

3. Bajo Información básica, introduzca la siguiente información:
Para Nombre de la función, introduzca un nombre que describa la función, como «StopEC2Instances».
Para Tiempo de ejecución, elija Python 3.9.
Para __Permisos__, expanda Cambiar el rol de ejecución predeterminado.
Bajo __Rol de ejecución__, elijaUso de un rol existente.
Bajo __Rol existente__, elija el rol de IAM.

4. Elija __Crear una función.__

5. En la pestaña Código, en Código fuente, pegue el siguiente código en el panel del editor de códigos de la pestaña lambda_function. Este código detiene las instancias que indique:

   ```json
   import boto3
   region = 'us-west-1'
   instances = ['i-12345cb6de4f78g9h', 'i-08ce9b2d7eccf6d26']
   ec2 = boto3.client('ec2', region_name=region)

   def lambda_handler(event, context):
     ec2.stop_instances(InstanceIds=instances)
     print('stopped your instances: ' + str(instances))
   ```

   Sustituya __us-west-1__ con la región de AWS en la que se encuentren sus instancias. Sustituya InstanceIds con los ID de las instancias que desee detener e iniciar.

6. Elija __Implementar.__

7. En la pestaña Configuración, elija Configuración general y, a continuación, elija Editar.

8. Configure el Tiempo de espera en 10 segundos y, a continuación, elija Guardar.
Nota: (Opcional) Puede ajustar la configuración de la función de Lambda. Por ejemplo, para detener e iniciar varias instancias se puede utilizar un valor diferente en Tiempo de espera y Memoria.

9. Para crear otra función, repita los pasos 1 a 7. Complete los siguientes pasos para que esta función inicie sus instancias:
En el paso 3, introduzca otro valor diferente en Nombre de la función. Por ejemplo, «StartEC2Instances».
En el paso 5, pegue el siguiente código en el panel del editor de códigos, en la pestaña lambda_function:

   ```json
   import boto3
   region = 'us-west-1'
   instances = ['i-12345cb6de4f78g9h', 'i-08ce9b2d7eccf6d26']
   ec2 = boto3.client('ec2', region_name=region)

   def lambda_handler(event, context):
     ec2.start_instances(InstanceIds=instances)
     print('started your instances: ' + str(instances))
   ```

   Use su región y los mismos ID de las instancias.
   

### Pruebe sus funciones de Lambda

1. Abra la consola de Lambda y, a continuación, elija Funciones.

2. Elija una de las funciones.

3. Elija la pestaña Código.

4. En la sección Código fuente, elija Probar.

5. En el cuadro de diálogo Configurar un evento de prueba, elija Crear un evento de prueba nuevo.

6. Introduzca el Nombre del evento. A continuación, elija Crear.
Nota: No cambie el código JSON para el evento de prueba.

7. Para ejecutar la función, elija Probar.

8. Repita los pasos 1 a 7 para la otra función.

### Compruebe el estado de sus instancias

#### Consola de administración de AWS

Antes y después de realizar la prueba, compruebe el estado de sus instancias para confirmar que sus funciones trabajan.

#### CloudTrail

Para confirmar que la función Lambda detuvo o inició la instancia, use AWS CloudTrail para comprobar si hay eventos.

1. Abra la consola de CloudTrail.

2. En el panel de navegación, elija Historial de eventos.

3. Elija la lista desplegable Atributos de búsqueda y, a continuación, elija el Nombre del evento.

4. En la barra de búsqueda, escribe ** StopInstances ** para revisar los resultados. A continuación, introduzca StartInstances.

Si no hay resultados, entonces la función de Lambda no habrá detenido ni iniciado las instancias.

### Creación de reglas de EventBridge que ejecuten sus funciones de Lambda

1. Abra la consola de EventBridge.

2. Seleccione Crear regla.

3. Introduzca un nombre para su regla, como, «StopEC2Instances». (Opcional) En Descripción, introduzca la descripción de la regla.

4. Para Tipo de regla, elija Programar y, a continuación, elija Continuar en el Programador de EventBridge.

5. En «Patrón de programación», elija Programa recurrente.

6. En Patrón de programación, en Ocasión, elija Programa recurrente.

7. En __Tipo de programación__, elija un tipo de programación y, a continuación, siga estos pasos:

   En __Programación basada en frecuencia__, introduzca un valor de frecuencia y, a continuación, elija un intervalo de tiempo en minutos, horas o días.
\ -o-

   En el caso de Programación basada en Cron, introduzca una expresión que indique a Lambda cuándo debe detener su instancia. Para obtener información sobre la sintaxis de las expresiones, consulte Crear una regla de Amazon EventBridge que se ejecute según un cronograma..

   __Nota:__ Las expresiones Cron se evalúan en UTC. Asegúrese de adaptar la expresión para su zona horaria.

8. En __Seleccionar destinos__, elija Función de Lambda en la lista desplegable Destino.

9. En __Función__, elija la función para detener las instancias.

10. Seleccione Saltar a Revisar y crear y, a continuación, elija Crear.

11. Repita los pasos del 1 al 10 para crear una regla para iniciar sus instancias. Complete los pasos siguientes:
Introduzca un nombre para la regla, por ejemplo, «StartEC2Instances».
(Opcional) En Descripción, ingrese una descripción de la regla, por ejemplo, «Inicie las instancias de EC2 todas las mañanas a las 7:00 am.»
En el paso 7, para Expresión Cron, ingrese una expresión que indique a Lambda cuándo debe iniciar sus instancias.
En el paso 9, en Función, elija la función para iniciar las instancias.

__Nota:__ A veces, una función de Lambda detiene una instancia y no puede volver a iniciarla. Esto ocurre cuando un volumen de Amazon Elastic Block Store (Amazon EBS) está cifrado y el rol de Lambda no está autorizado a usar la clave de cifrado. Para obtener más información, consulte la política de claves de AWS KMS obligatorias para su uso con volúmenes cifrados y las políticas de claves en AWS KMS.





https://repost.aws/es/knowledge-center/start-stop-lambda-eventbridge