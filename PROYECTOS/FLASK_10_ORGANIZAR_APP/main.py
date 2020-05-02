#---------------------------------------------------------------------------------------
#APP PARA EXTENDER UTILIDAD DE FLASK Y ORGANIZAR APP MUCHO MEJOR Y MODULARIZARLA
#Santiago Garcia Arango
#---------------------------------------------------------------------------------------
#Nota: Ademas de este archivo, ver "correr.sh" para correr con respectivos comandos en terminal (bash) y correr...
#...servidor flask adecuadamente. (ademas de indicarlos, permite automatizar proceso tedioso repetitivo en terminal)


#Nota: todas las librerias y dependencias se van "modularizando" en los respectivos archivos en carpeta "app"...
#...de tal forma que se vaya organizando todos los componentes que vamos trabajando ( y dependencias)


from flask import request , make_response , redirect , render_template , session , url_for , flash


#Ahora para organizar APP importamos paquete "app" para correcta inicializacion y configuraciones de app respectivas
from app import crear_app
from app.forms import LoginForm


app = crear_app()



#Configuramos el "error handler" para lograr solucionar problema de pagina NO encontrada (404)
@app.errorhandler(404)
def not_found_page( error ):
    #Redireccionamos a template de pagina_no_encontrada.html e indicamos error
    return( render_template("pag_no_encontrada.html" , error=error) )



#Con este decorador, logramos acceder a ruta "/" (osea la ruta por defecto)
@app.route("/")
def index():
    #Accedemos a la IP actual del usuario (utilizando request)
    #Cuando se desarrolle app con servidor global, se podria acceder a esta IP de cada usuario
    IP_usuario = request.remote_addr

    #Ahora creamos un "response" que nos redirecciona a "/hello"
    respuesta = make_response( redirect("/hello") )
    
    #Agregamos ahora el dato del IP_usuario pero de forma personal para la session del usuario
    #NOTA: esto es totalmente diferente a crear una cookie
    session['IP_usuario'] = IP_usuario

    #Ejecutamos respuesta (que tiene tanto redirect, como cookie del IP)
    return( respuesta )



#Ruta que va a re-dirigir index, y recibira la respuesta, junto con la info usuario
#Ademas, ahora agregaremos metodos GET y POST(para hacer correcto POST del formulario)
@app.route("/hello" , methods=["GET","POST"])
def hello():
    #Obtenemos ahora el IP_usuario a traves de la info de la session actual del usuario (diferente de cookie)
    IP_usuario = session.get( 'IP_usuario' )

    #Ahora nos aprovechamos de los "forms.py" dentro de directorio "app" para crear el FORM
    login_form = LoginForm()


    #Cuando se logre realizar el POST para procesar la info del usuario, debe crearse "session["usuario"] = usuario"...
    #... ahora lo agregamos al contexto (esto sucede luego del IF de abajo)
    usuario = session.get("usuario")
    password = session.get("password")

    #Como empezamos a tener muchos parametros, es buena practica enviarlos a render_template...
    #...en un diccinarios de "contexto" que tenga todos estos parametros respectivos
    context = {
        "IP_usuario" : IP_usuario,
        "login_form": login_form,
        "usuario" : usuario,
        "password" : password,
    }

    #Validamos que se detecta un POST adecuadamente al efectuar boton de submit (ver HTML en seccion del FORM)
    #Este if nos permite validar y agregar a la session actual los datos del usuario
    if login_form.validate_on_submit():
        #Obtenemos los datos del usuario y los agregamos a la session respectivamente
        usuario = login_form.usuario.data
        session["usuario"] = usuario
        password = login_form.password.data
        session["password"] = password

        #Indicamos al usuario que fue agregado correctamente
        flash( "DATOS ACTUALIZADOS CORRECTAMENTE!" )


        return( redirect( url_for("hello") ) )

    #Indicamos un render_template que permite indicar el HTML al que queremos ir, ademas de la variable IP_usuario
    #NOTA: al indicar **context , nos aprovechamos de python para expandir diccionario "context" y enviar cada...
    #...uno de sus keys y keywords hacia flask (equivalente a enviar todos uno a uno por aparte)
    return( render_template("hello.html", **context) )





#Ruta para proyectos de IOT
@app.route("/IOT")
def IOT():

    #Obtenemos el dato del nombre usuario (para renderiarlo correctamente en navbar)
    #la contrasenna y los otros NO nos importan en este HTML de la pagina
    usuario = session.get("usuario")
    
    #Los agregamos al contexto para pasarlo al "render_template()"
    context = {
        "usuario" : usuario,
    }
    return( render_template("IOT.html" , **context) )


#Ruta para Datos cuenta
@app.route("/cuenta")
def cuenta():

    #Obtenemos todos los datos de la session del usuario (ya obtenidos previamente en hello e index)
    IP_usuario = session.get( 'IP_usuario' )
    usuario = session.get("usuario")
    password = session.get("password")
    
    #Los agregamos al contexto para pasarlo al "render_template()"
    context = {
        "IP_usuario" : IP_usuario,
        "usuario" : usuario,
        "password" : password,
    }

    return( render_template("cuenta.html" , **context) )
