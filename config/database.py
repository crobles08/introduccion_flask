import mysql.connector #Conector de base de datos
#render_template => Siempre lee la carpeta templates
from config import settings

db = mysql.connector.connect( #Parametros
    host=settings.MYSQL_HOSTNAME,
    user=settings.MYSQL_USERNAME,
    password=settings.MYSQL_PASSWORD,
    port=settings.MYSQL_PORT,
    database=settings.MYSQL_DATABASE,
)
db.autocommit = True #Para que las consultas se ejecuten, que no se guarden en cache