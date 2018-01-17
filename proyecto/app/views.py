# -*- coding: utf-8 -*-
from flask import request, redirect, render_template, url_for
from app import app
from random import randint

@app.route('/')
def index():
	return render_template(
        'index.html'
    )
# Declaramos la variable random.
adiviname = randint(1,100)
# Declaramos la variable que nos mostrará los intentos al final de la partida.
intentos = 0
# Ruta donde esta el juego
@app.route('/ludopata', methods=["GET","POST"])
def game():
    # Declaramos global para definir que son las variables de arriba
    global adiviname
    global intentos
    # Mensaje principal
    mensaje = u"Adivina un numero entre 1 y 100"
    if request.method == "POST":
        num = int(request.form["number"])
        if num==adiviname:
        	mensaje = "Has acertado! y has hecho "+str(intentos)+" intentos."
		adiviname = randint(1,100)
		intentos = 0
        elif num<adiviname:
		intentos = intentos + 1
        	mensaje = u"El número a adivinar es major de "+str(num)       
	elif num>adiviname:
		intentos = intentos + 1
        	mensaje = u"El número a adivinar es menor de "+str(num)
    # renderizamos el template.
    return render_template( "adivina.html", missatge=mensaje )

