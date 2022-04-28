from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/consumo", methods=['GET','POST'])
def consumo():
    if request.method=='GET':
        return render_template("consumo.html")
    if request.method=='POST':
        valor = request.form['cant-gas']
        if request.form['MPGkml']:
            resultado = valor * 0.425144
        if request.form['MPG100']:
             resultado = 235.215 / valor
        if request.form['kmlMPG']:
            resultado = valor * 2.352
        if request.form['kml100']:
            resultado = 100 / valor
        if request.form['100MPG']:
            resultado = 235.215 / valor
        if request.form['100kml']:
            resultado = 100 / valor
        return render_template("consumo.html", res=resultado)


if __name__ == "__main__":
    app.run(debug=True)