#from crypt import methods
#from crypt import methods
from sqlite3 import Cursor
from flask import Flask, flash, render_template, request, redirect, url_for
import mysql.connector #Conector de base de datos
#render_template => Siempre lee la carpeta templates

db = mysql.connector.connect( #Parametros
    host = 'localhost',
    user = 'root',
    password = '',
    port = 3306,
    database = 'productos'
)

db.autocommit = True #Para que las consultas se ejecuten, que no se guarden en cache
app = Flask(__name__)

@app.get("/") #*Cuando esta en @ es un decorador (COMO HERENCIA)*
def inicio():
    
    cursor = db.cursor(dictionary = True) #Abrir cursor
    
    cursor.execute("SELECT * FROM productos") #Ejecutar consulta
    productos = cursor.fetchall() #Obtener todo el resultado de la consulta
   # producto = cursor.fetchone() #Trae solo un registro (Primero que encuentra)

    #print(productos[5]['nombre'])
    #print(productos)

    cursor.close()#Cerrar cursor
    return render_template("index.html", productos = productos)

@app.get("/form_crear")
def formCrearProducto():
    return render_template("crearProducto.html")

@app.post("/form_crear")
def crearProducto():
    
    #Recuperar los datos del formulario
    nombre = request.form.get('nombre')
    price = request.form.get('price')
    
    
    #Insertar los datos en la base de datos
    cursor = db.cursor()
    cursor.execute("INSERT INTO productos(nombre, price) VALUES (%s, %s)", (
        nombre,
        price,
    ))
    cursor.close()
    #Volver al listado o formulario

    return redirect(url_for('inicio'))

    #Volver al listado o formulario

    #return redirect(url_for('inicio'))

#Eliminar Registros 
@app.route("/eliminar/<int:id>")
def formEliminarProducto(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM productos WHERE id = {0}".format(id))
    cursor.close()
    return redirect(url_for('inicio'))

#Editar productos
@app.get("/form_editar")
def formEditarProducto():
    return render_template('editarProducto.html')

@app.route('/editarProducto/<int:id>', methods = ['POST', 'GET'])
def obtenerProducto(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = {0}".format(id))
    producto = cursor.fetchall()
    cursor.close()
    print (producto)
    return render_template('editarProducto.html', producto = producto[0])
#---------------------------------------------
#Acctualiza productos
@app.route('/actualizarProducto/<id>', methods=['POST'])
def actualizaProductoId(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        price = request.form['price']
        cursor = db.cursor()
        cursor.execute("""
            UPDATE productos SET  nombre = %s, price = %s
            WHERE id = %s
        """, (nombre, price, id)) 
        return redirect(url_for('inicio'))


#------------------------------------------

@app.get("/contactos")#Crear una ruta
def listarContactos():
    return render_template("index2.html")

#Rutas dinamicas pasan por parametro el nombre de la url entre <>
#@app.get("/contactos/<int:contactosId>") #Crear rutas dinamicas (Siempre deben ir entre <>)
#@app.get("/contactos/<int:contactosId>") La ruta espera un numero entero para imprimirlo str()
#def editarContacto(contactosId):
    #return render_template("index3.html" , id = contactosId)

@app.get("/contactos/<int:edades>") #Crear rutas dinamicas (Siempre deben ir entre <>)
#@app.get("/contactos/<int:contactosId>") La ruta espera un numero entero para imprimirlo str()
def editarContacto(edades):
    return render_template("edades.html" , id = edades)

app.run(debug = True)    