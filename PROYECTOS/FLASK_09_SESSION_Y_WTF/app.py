#---------------------------------------------------------------------------------------
#APP PARA EXTENDER UTILIDAD DE FLASK Y AGREGAR LLAVE SECRETA Y SESSION "PERSONAL" Y WTF
#Santiago Garcia Arango
#---------------------------------------------------------------------------------------
#Nota: Ademas de este archivo, ver "correr.sh" para correr con respectivos comandos...
#...en terminal, para correr servidor flask adecuadamente.
#(ademas de indicarlos, permite automatizar proceso tedioso repetitivo en terminal)


from flask import Flask , request , make_response , redirect , render_template , session

#Libreria flask-wtf nos permitira crear facilmente los requerimientos para validar un usuario
#NOTA: se deben importar estas librerias para correcto manejo de ingreso de datos y contrasenna
from flask_wtf import FlaskForm
from wtforms.fields import StringField , PasswordField , SubmitField
from wtforms.validators import DataRequired



#Vector que pasaremos hacia flask (para mostrar ciclos a traves de Jinja2 en HTML)
vector_cool = [1,1,2,3,5,8,13,21,34,55,89,144]


#Indicamos que app va a tener como parametro el nomre de este archivo
app = Flask( __name__ )

#Agregamos la posibilidad de configurar una "SECRET_KEY" para encriptar session y cuidar info (evitar cookies)
#Cuando se saque app de Flask a produccion, se debe generar esta llave mejor (mas adelante se explicara)
app.config['SECRET_KEY'] = "LLAVE SUPER SECRETA SANTI"


#Creamos clase para trabajar y manejar los "FORMS", a traves de herencia desde libreria flask-wtk ( FlaskForm )
class LoginForm( FlaskForm ):
    #Usuario se crea con StringField y PasswordField importados previamente (facilitan trabajo con forms)
    #NOTA: es importante agregar el DataRequired() e inicializarlo en los validators para correcto funcionamiento
    usuario = StringField( "Nombre de usuario" , validators=[ DataRequired() ] )
    password = PasswordField( "Password" , validators=[ DataRequired() ])
    submit = SubmitField( "Ingresar" )


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


#Ruta que va a re-dirigir index, y recibira la respuesta, junto con la cookie
@app.route("/hello")
def hello():
    #Obtenemos ahora el IP_usuario a traves de la info de la session actual del usuario (diferente de cookie)
    IP_usuario = session.get( 'IP_usuario' )

    #Creamos objeto con ayuda de clase para manejar los logins creado arriba
    login_form = LoginForm()

    #Como empezamos a tener muchos parametros, es buena practica enviarlos a render_template...
    #...en un diccinarios de "contexto" que tenga todos estos parametros respectivos
    context = {
        "IP_usuario" : IP_usuario,
        "vector_cool" : vector_cool,
        "login_form": login_form,
    }

    #Indicamos un render_template que permite indicar el HTML al que queremos ir, ademas de la variable IP_usuario
    #NOTA: al indicar **context , nos aprovechamos de python para expandir diccionario "context" y enviar cada...
    #...uno de sus keys y keywords hacia flask (equivalente a enviar todos uno a uno por aparte)
    return( render_template("hello.html", **context) )