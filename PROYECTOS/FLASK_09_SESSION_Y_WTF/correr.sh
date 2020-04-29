#!/bin/bash

#ARCHIVO TIPO BASH PARA "AUTOMATIZAR" COMANDOS TERMINAL
#Al correrlo, correra estos comandos en terminal por nosotros

#Activar virtual env en caso de que NO este activo
../../env/Scripts/activate

#Definir archivo flask por defecto para correr app (nombre archivo python)
set FLASK_APP=app.py

#Activar modo debug para verificar errores y tener mas control
export FLASK_DEBUG=1

#Permitie activar el entorno "development" en app
set FLASK_ENV=development

#Correr "servidor" de flask
flask run