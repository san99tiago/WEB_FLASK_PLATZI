#--------------------------------------------------------
#PRIMERA APP PARA MOSTRAR A TRAVES DE FLASK UN MENSAJE
#Santiago Garcia Arango
#--------------------------------------------------------
#Nota: Ademas de este archivo, ver "correr.sh" para correr con respectivos comandos...
#...que debemos indicar en terminal para correr servidor adecuadamente
#(ademas de indicarlos, permite automatizar proceso tedioso repetitivo)

from flask import Flask

#Indicamos que app va a tener como parametro el nomre de este archivo
app = Flask( __name__ )

#Con este decorador, logramos acceder a ruta "/" (osea la ruta por defecto)
@app.route("/")
def hola():
    return( "MI PRIMERA APP EN FLASK!!" )