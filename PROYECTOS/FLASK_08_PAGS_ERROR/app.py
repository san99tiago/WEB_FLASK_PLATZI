#----------------------------------------------------------------------------------
#APP PARA EXTENDER UTILIDAD DE FLASK Y AGREGAR MANEJO PAGINAS DE ERROR (ej:404)
#Santiago Garcia Arango
#----------------------------------------------------------------------------------
#Nota: Ademas de este archivo, ver "correr.sh" para correr con respectivos comandos...
#...en terminal, para correr servidor flask adecuadamente.
#(ademas de indicarlos, permite automatizar proceso tedioso repetitivo en terminal)

from flask import Flask , request , make_response , redirect , render_template

#Indicamos que app va a tener como parametro el nomre de este archivo
app = Flask( __name__ )


#Configuramos el "error handler" para lograr solucionar problema de pagina NO encontrada (404)
@app.errorhandler(404)
def not_found_page( error ):
    #Redireccionamos a template de pagina_no_encontrada.html e indicamos error
    return( render_template("pag_no_encontrada.html" , error=error) )



#Vector que pasaremos hacia flask (para mostrar ciclos a traves de Jinja2 en HTML)
vector_cool = [1,1,2,3,5,8,13,21,34,55,89,144]


#Con este decorador, logramos acceder a ruta "/" (osea la ruta por defecto)
@app.route("/")
def index():
    #Accedemos a la IP actual del usuario (utilizando request)
    #Cuando se desarrolle app con servidor global, se podria acceder a esta IP de cada usuario
    IP_usuario = request.remote_addr

    #Ahora creamos un "response" que nos redirecciona a "/hello"
    respuesta = make_response( redirect("/hello") )
    
    #Ademas, creamos COOKIE para el IP_usuario
    respuesta.set_cookie( "IP_usuario" , IP_usuario )

    #Ejecutamos respuesta (que tiene tanto redirect, como cookie del IP)
    return( respuesta )


#Ruta que va a re-dirigir index, y recibira la respuesta, junto con la cookie
@app.route("/hello")
def hello():
    #Creamos IP_usuario a traves de request hacia las cookies y la "llave" que identificaba el IP_usuario
    IP_usuario = request.cookies.get( "IP_usuario" )

    #Como empezamos a tener muchos parametros, es buena practica enviarlos a render_template...
    #...en un diccinarios de "contexto" que tenga todos estos parametros respectivos
    context = {
        "IP_usuario" : IP_usuario,
        "vector_cool" : vector_cool
    }

    #Indicamos un render_template que permite indicar el HTML al que queremos ir, ademas de la variable IP_usuario
    #NOTA: al indicar **context , nos aprovechamos de python para expandir diccionario "context" y enviar cada...
    #...uno de sus keys y keywords hacia flask (equivalente a enviar todos uno a uno por aparte)
    return( render_template("hello.html", **context) )