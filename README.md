# localesAPI

## Descripción del proyecto
API utilizada para la gestion de locales registrados por los dueños de los mismos, con el fin de obtener información acerca de que medidas sanitarias son cumplidas por dicho local.

## Descripción técnica del backend
### Tecnologías utilizadas
* Python, Django, Django Rest Framework
* Postgres

### Observaciones
Se debe definir las siguientes variables de entorno en un archivo *.env*, ubicado en donde se encuentre el archivo *settings.py*, o bien, definirlas como variables de entorno en el sistema operativo. Para envio de correos electrónicos, también debe definir las variables necesarias según su configuración, esta configuración de ejemplo es utilizando el servicio de Gmail/Google.
```
# SERVER CONFIG
DEBUG=False
SECRET_KEY=<su_clave_secreta>

# BD
BD_ENGINE=django.db.backends.postgresql
BD_NAME=movilApp
BD_USER=postgres
BD_PASS=postgres
BD_HOST=localhost
BD_PORT=5432

# EMAIL (gmail)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=correo@midominio.com
EMAIL_HOST_PASSWORD=micontrasenha
```