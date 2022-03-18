from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models.ninjas import Ninja
from flask_app.models.dojos import Dojo




@app.route("/nuevoninja")
def plantilla():
    dojos= Dojo.muestra_dojo()
    ninjas= Ninja.mostrar_usuarios()
    return render_template("nuevoninja.html", dojos=dojos, ninjas=ninjas)

@app.route("/agregar", methods=["POST"])
def nuevo():
    Ninja.guardar(request.form)
    return redirect("/")


    

    
