#ESTE PERMITIRA CORRER CORRECTAMENTE ESTE PAQUETE DE PYTHON...
#Ademas es importante tener en cuenta que al importarlo, correra primero este
#  __init__.py es la forma de indicar correctamente el "paquete"


from flask import Flask


from .config import configurar_app

#Nos aprovecharemos del __init__.py para la funcion "crear_app()"
def crear_app():
    #Indicamos que app va a tener como parametro el nomre de este archivo
    app = Flask( __name__ )

    #De esta manera accedemos a OBJETO creado para las configuraciones
    app.config.from_object( configurar_app )


    return( app )
