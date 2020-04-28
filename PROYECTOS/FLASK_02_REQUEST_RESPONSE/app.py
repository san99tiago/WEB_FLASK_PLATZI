#--------------------------------------------------------------------
#PRIMERA APP PARA TRABAJAR CON "REQUEST" Y GENERAR UN "RESPONSE"
#Santiago Garcia Arango
#--------------------------------------------------------------------
#Nota: Ademas de este archivo, ver "correr.sh" para correr con respectivos comandos...
#...en terminal, para correr servidor flask adecuadamente.
#(ademas de indicarlos, permite automatizar proceso tedioso repetitivo en terminal)

from flask import Flask , request , make_response , redirect

#Indicamos que app va a tener como parametro el nomre de este archivo
app = Flask( __name__ )

#Con este decorador, logramos acceder a ruta "/" (osea la ruta por defecto)
@app.route("/")
def index():
    #Accedemos a la IP actual del usuario (utilizando request)
    #Cuando se desarrolle app con servidor global, se podria acceder a esta IP de cada usuario
    IP_usuario = request.remote_addr

    #Ahora creamos un "response" que nos redirecciona a "/hola"
    respuesta = make_response( redirect("/hola") )
    
    #Ademas, creamos COOKIE para el IP_usuario
    respuesta.set_cookie( "IP_usuario" , IP_usuario )

    #Ejecutamos respuesta (que tiene tanto redirect, como cookie del IP)
    return( respuesta )


#Ruta que va a re-dirigir index, y recibira la respuesta, junto con la cookie
@app.route("/hola")
def hola():
    #Creamos IP_usuario a traves de request hacia las cookies y la "llave" que identificaba el IP_usuario
    IP_usuario = request.cookies.get( "IP_usuario" )

    return( "Querido usuario, su IP es {}".format( IP_usuario ) )