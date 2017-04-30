from flask import Flask, render_template
from wtforms import Form, TextField, SelectField, validators
from flask_mysqldb import MySQL

app = Flask("umbrella") #nuevo objeto
mysql = MySQL(app)

class SearchForm(Form):
    text= TextField("text",[validators.required()])

@app.route('/',methods=["GET"]) #wrap ruta donde puede acceder el usuario
def index ():
    form = SearchForm()
    return render_template("index.html", form=form)

def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT lmunozm, host FROM mysql.lmunozm''')
    rv = cur.fetchall()
    return str(rv)

if __name__ == '__main__':
  app.run(debug = True, port = 3000) #Ejecuta el localhost
