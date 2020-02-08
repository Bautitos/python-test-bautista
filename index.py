#importo flask
from flask import Flask, render_template 

#inicializo el framework
#se confirma que este es el archivo que arranca la app
#esta variable se utilizara para crear las rutas 
#del servidor, urls y demas...
app = Flask(__name__)

#se crea la ruta para la pagina principal
#la extencion .route nos deja establecer una direccion
#en este caso '/'
@app.route('/')
#esta sera la funcion que se llame cuando un usuario 
#entre a nuestra pagina principal(index) 
def home():
#devuelvo la pagina
    return render_template('home.html')
#segunda direccion que puede visitar el usuario
@app.route('/about')
#funcion que se ejecutara al entrar a about
def about():
#devuelvo la pagina de about.html
    return render_template('about.html')



#a continuacion, es para que la app
# este escuchando constantemente

#valido que estamos ejecutando archivo principal como lo que es 
#y no como un modulo
if __name__ == '__main__':
    #metodo run, nos permite ejecutar nuestra aplicacion
    app.run(debug = True)    