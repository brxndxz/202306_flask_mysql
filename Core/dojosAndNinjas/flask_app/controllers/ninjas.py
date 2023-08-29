from flask import flash, redirect, request, render_template

from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    return render_template("crearNinja.html", dojos = Dojo.get_all())

@app.route('/crear_ninja', methods=["POST"])
def crear_ninja():
    print("DATOS:", request.form)

    id = Ninja.save(request.form)

    flash(f"El Ninja fue agregada exitosamente con el ID {id}", "success")
    return redirect("/dojos")