#importar la libería de flask
from flask import Flask

#inicializar la variable ap con flask
app = Flask(__name__)

#inicializar el servidor de flask
#en mac: export FLASK_APP=main.py
#en windows: set FLASK_APP=main.py

#comando para ejecutar el servidor
#flask --app main

#Comando para ejecutar el servidor en otro puerto diferente por default es el 5000
#flask --app main run -p 5002

#Comando para ejeutar el servidor en modo debug, para realizar cambios en tiempo real 
#flask --app main --debug run

@app.route("/hola")
def hello_world():
    return "Hello, World, mundo flask!"

#ejercicio una ruta que devualva una lista de frutas el path sería /frutas
@app.route("/frutas")
def lista_frutas():
    list_fruta = ["Platano","Melon","Naranja","Melocoton","Fresa","Piña"]
    return list_fruta

#ejemplo para enviar parametros en las rutas
@app.route("/nombre/<n>/")
def tunombre(n):
    return f"hola {n} como estás"

#ejercicio2 realizar una ruta que devualva el cuadrado de un numero dado,/numero/<parametro>
@app.route("/numero/<int:parametro>")
def cuadrado(parametro):
    #parametro = int(parametro)
    return f"El cuadrado de {parametro} es {parametro*parametro}"

#ejercicio3, realizar una ruta, que dinamicamente pueda soliciar o realizar 
#operaciones de suma, resta, multiplicación y division segun los parametros pasods en la ruta