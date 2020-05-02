#ARCHIVO PARA MANEJO CORRECTO DE FORMULARIOS EN APP DE FLASK

#Libreria flask-wtf nos permitira crear facilmente los requerimientos para validar un usuario
#NOTA: se deben importar estas librerias para correcto manejo de ingreso de datos y contrasenna
from flask_wtf import FlaskForm
from wtforms.fields import StringField , PasswordField , SubmitField
from wtforms.validators import DataRequired


#Creamos clase para trabajar y manejar los "FORMS", a traves de herencia desde libreria flask-wtk ( FlaskForm )
class LoginForm( FlaskForm ):
    #Usuario se crea con StringField y PasswordField importados previamente (facilitan trabajo con forms)
    #NOTA: es importante agregar el DataRequired() e inicializarlo en los validators para correcto funcionamiento
    usuario = StringField( "Nombre de usuario" , validators=[ DataRequired() ] )
    password = PasswordField( "Password" , validators=[ DataRequired() ])