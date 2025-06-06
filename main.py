#importar la libería de flask
from flask import Flask, render_template

#inicializar la variable ap con flask
app = Flask(__name__)

#inicializar el servidor de flask
#en mac: export FLASK_APP=main.py
#en windows: set FLASK_APP=main.py

#comando para ejecutar el servidor
#flask --app main run

#Comando para ejecutar el servidor en otro puerto diferente por defecto es el 5000
#flask --app main run -p 5002

#Comando para ejeutar el servidor en modo debug, para realizar cambios en tiempo real 
#flask --app main --debug run

@app.route("/hola")
def hello_world():
    return "Hola mundo, mundo flask!"

#ejercicio una ruta que devualva una lista de frutas el path sería /frutas
@app.route("/frutas")
def lista_frutas():
    list_fruta = ["Platano","Melon","Naranja","Melocoton","Fresa","Piña"]
    return list_fruta

#ejemplo para enviar parametros en las rutas
@app.route("/nombre/<n>/apellido<a>/edad<int:e>")
def tunombre(n,a,e):
    return f"hola {n} {a} tienes {e} años de edad"

#ejercicio2 realizar una ruta que devualva el cuadrado de un numero dado,/numero/<parametro>
@app.route("/numero/<int:parametro>")
def cuadrado(parametro):
    #parametro = int(parametro)
    return f"El cuadrado de {parametro} es {parametro*parametro}"

#ejercicio3, realizar una ruta, que dinamicamente pueda soliciar o realizar 
#operaciones de suma, resta, multiplicación y division segun los parametros pasados en la ruta
@app.route("/operaciones/<float:op1>/<float:op2>/<string:ope>")
def calcualdora(op1,op2,ope):
    if ope == "sum":
        return f"La suma de {op1} y  {op2} es {op1+op2}"
    elif ope == "rest":
        return f" La resta de {op1} y {op2} es {op1-op2}"
    elif ope == "mult":
        return f"La multiplicación de {op1} y {op2} es {op1*op2}"
    elif ope == "div":
        return f"La división de {op1} y {op2} es {op1/op2}"
    
@app.route("/<nombre>")
def llamarhtml(nombre):
    list_fruta = ["Platano","Melon","Naranja","Melocoton","Fresa","Piña"]
    return render_template("hola.html",name=nombre, fruta= list_fruta)
