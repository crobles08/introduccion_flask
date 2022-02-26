from flask import Flask, render_template
#render_template => Siempre lee la carpeta templates
app = Flask(__name__)

@app.get("/") #*Cuando esta en @ es un decorador (COMO HERENCIA)*
def inicio():
    return render_template("index.html")


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