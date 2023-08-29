from flask import flash, redirect, request, render_template

from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def ruta_dojo():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dojos.html', dojos = dojos)
    
@app.route('/crear_dojo', methods=["POST"])
def crear_dojo():
    print("DATOS:", request.form)
    data = {
        'name': request.form['name']
    }
    id = Dojo.save(data)

    flash(f"el dojo fue agregado exitosamente con el ID {id}", "success")
    return redirect("/dojos")

@app.route('/dojos/<id>')
def obtener_dojo(id):

    data = {'id': id}

    dojo = Dojo.get_dojo_with_ninjas(data)

    return render_template("mostrarNinjas.html", dojo=dojo)