from flask import Flask, render_template
from wtforms import Form, TextField, SelectField, validators
from flask_mysqldb import MySQL

app = Flask("umbrella") #nuevo objeto

app.config['MYSQL_DATABASE_USER'] = 'st0263'
app.config['MYSQL_DATABASE_PASSWORD'] = 'st0263.2017'
app.config['MYSQL_DATABASE_DB'] = 'st0263'
app.config['MYSQL_DATABASE_HOST'] = '10.131.137.188'
mysql.init_app(app)

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
