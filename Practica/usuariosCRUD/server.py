from flask import Flask, render_template, request, redirect, flash, url_for
# importar la clase de user.py
from user import User
app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route("/users")
def mostrar():
    users = User.get_all()
    print(users)
    return render_template("mostrarUsers.html", users = users)

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "em" : request.form["em"]
    }

    User.save(data)
    return redirect('/users')

@app.route("/users/new")
def formulario():
    return render_template("formulario.html")

@app.route("/users/<id>")
def result(id):
    user = User.get(id)
    return render_template("usuario.html", user = user)

@app.route("/delete/<id>/destroy")
def delete(id):

    print("USUARIO A ELIMINAR", id)

    delete_user = User.get(id)
    delete_user.delete()

    flash("User deleted", "success")
    return redirect("/users")

@app.route('/users/<id>/edit')
def edit_user(id):

    user = User.get(id)

    return render_template( 'editar.html', user = user )

@app.route("/process_edit_user/<id>", methods=['POST'])
def process_edit_user(id):
    print("DATOS:", request.form)

    user = User.get(id)
    user.fname = request.form['fname']
    user.lname = request.form['lname']
    user.em = request.form['em']
    user.update()
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)