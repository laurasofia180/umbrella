from flask import Flask, render_template
from wtforms import Form, TextField, SelectField, validators
import MySQLdb

app = Flask("umbrella") #nuevo objeto

class SearchForm(Form):
    text= TextField("text",[validators.required()])

@app.route('/',methods=["GET"]) #Route for the index and search
def index ():
    form = SearchForm()
    return render_template("index.html", form=form)

@app.route('/words',methods=["GET"]) #Route for all db content
def words():
    db = MySQLdb.connect(host="10.131.137.188", user="st0263", passwd="st0263.2017", db="st0263")
    cur = db.cursor()
    cur.execute(''' SELECT * FROM lmunozm ''')
    rv = cur.fetchall()
    return str(rv)

if __name__ == '__main__':
  app.run(debug = True, port = 3000,host="0.0.0.0") #Ejecuta el localhost
