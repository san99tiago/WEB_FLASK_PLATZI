#-------------------------------------------------------------
#PRIMERA APP PARA TRABAJAR CON "REQUEST" Y OBTENER IP USUARIO
#Santiago Garcia Arango
#-------------------------------------------------------------
#Nota: Ademas de este archivo, ver "correr.sh" para correr con respectivos comandos...
#...en terminal, para correr servidor flask adecuadamente.
#(ademas de indicarlos, permite automatizar proceso tedioso repetitivo en terminal)

from flask import Flask , request

#Indicamos que app va a tener como parametro el nomre de este archivo
app = Flask( __name__ )

#Con este decorador, logramos acceder a ruta "/" (osea la ruta por defecto)
@app.route("/")
def hola():
    #Accedemos a la IP actual del usuario (utilizando request)
    #Cuando se desarrolle app con servidor global, se podria acceder a esta IP de cada usuario
    IP_usuario = request.remote_addr

    return( "Querido usuario, su IP es {}".format( IP_usuario ) )