#ARCHIVO PARA CONFIG DE LA APP DE FLASK
#Es mejor "modularizarlos", porque a medida de que las apps se van...
#...aumentando y complicando, se debe mantener el orden


#Creamos clase para lograr configurar la app correctamente al crearla
class configurar_app:

    #Agregamos la posibilidad de configurar una "SECRET_KEY" para encriptar session y cuidar info (evitar cookies)
    #Cuando se saque app de Flask a produccion, se debe generar esta llave mejor (mas adelante se explicara)
    #Si utilizamos FORMS de WTF tambien es necesaria esta llave secreta
    SECRET_KEY = "LLAVE SUPER SECRETA SANTI"