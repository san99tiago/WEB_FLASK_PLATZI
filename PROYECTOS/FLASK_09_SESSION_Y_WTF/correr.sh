#!/bin/bash

#ARCHIVO TIPO BASH PARA "AUTOMATIZAR" COMANDOS TERMINAL
#OJO:formato de estos archivos es similar al de GNU (CAMBIA SINTAXIS)
#por lo tanto, si se fueran a correr en windows terminal, ver equivalencia
#Al correrlo, correra estos comandos en terminal por nosotros

#Activar virtual env en caso de que NO este activo
#(en windows cmd:  >>../../env/Scripts/activate)
source ../../env/Scripts/activate

#Definir archivo flask por defecto para correr app (nombre archivo python)
#(en windows cmd:  >>set FLASK_APP=app.py)
export FLASK_APP=app.py

#Activar modo debug para verificar errores y tener mas control
#(en windows cmd:  >>set FLASK_DEBUG=1)
export FLASK_DEBUG=1

#Permitie activar el entorno "development" en app
#(en windows cmd:  >>set FLASK_ENV=development)
export FLASK_ENV=development

#Correr "servidor" de flask (igual en windows)
# OJO: al agregar --host=0.0.0.0 estamos permitiendo distribucion a IP locales de LAN
flask run --host=0.0.0.0