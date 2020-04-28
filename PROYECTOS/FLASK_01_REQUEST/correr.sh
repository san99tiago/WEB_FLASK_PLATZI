#!/bin/bash

#ARCHIVO TIPO BASH PARA "AUTOMATIZAR" COMANDOS TERMINAL
#Al correrlo, correra estos comandos en terminal por nosotros

#Activar virtual env en caso de que NO este activo
../../env/Scripts/activate

#Definir archivo flask por defecto para correr app
export FLASK_APP=app.py

#Activar modo debug
export FLASK_DEBUG=1

#Correr "servidor" de flask
flask run