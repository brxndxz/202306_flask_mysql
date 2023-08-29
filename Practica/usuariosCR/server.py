from flask import Flask, render_template, request, redirect
# importar la clase de user.py
from user import User
app = Flask(__name__)

@app.route("/users")
def mostrar():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
    print(users)
    return render_template("mostrarUsers.html", all_users = users)

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

if __name__ == "__main__":
    app.run(debug=True)