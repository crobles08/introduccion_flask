from config.database import db


def obtenerProductos():
    cursor = db.cursor(dictionary = True) #Abrir cursor
    
    cursor.execute("SELECT * FROM productos") #Ejecutar consulta
    productos = cursor.fetchall() #Obtener todo el resultado de la consulta
   # producto = cursor.fetchone() #Trae solo un registro (Primero que encuentra)

    #print(productos[5]['nombre'])
    #print(productos)
    cursor.close()#Cerrar cursor
    return productos
    
    
    

def crearProducto(nombre, price):
    cursor = db.cursor()
    cursor = db.cursor()
    cursor.execute("INSERT INTO productos(nombre, price) VALUES (%s, %s)", (
        nombre,
        price,
    ))
    cursor.close()