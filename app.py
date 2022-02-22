from flask import Flask, render_template, redirect, url_for, request
from db import insertNewPerson
from person import Person


app=Flask(__name__)

@app.route("/insertar_datos", methods=["GET","POST"])

def newdata():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        persona = Person(name, email)
        insertNewPerson(persona)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    

if __name__ == '__main__':
    app.run(debug=True)
    
    