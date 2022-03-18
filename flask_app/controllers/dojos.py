from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/')
def index():
    return redirect("/dojos")

@app.route("/dojos")
def principal():
    dojos= Dojo.muestra_dojo()
    return render_template("dojos.html", dojos=dojos)

@app.route("/adherir", methods=["POST"])
def adherir():
    Dojo.agregar(request.form)
    return redirect("/")


@app.route("/dojoshow/<int:id>")
def show(id):
    datos = {
        "id": id
    }
   
    return render_template("dojoshow.html", dojo=Dojo.depurar(datos))