from flask import Flask, render_template
from wtforms import Form, TextField, SelectField, validators

app = Flask("umbrella") #nuevo objeto

class SearchForm(Form):
    text= TextField("text",[validators.required()])

@app.route('/',methods=["GET"]) #wrap ruta donde puede acceder el usuario
def index ():
    form = SearchForm()
    return render_template("index.html", form=form)

if __name__ == '__main__':
  app.run(debug = True, port = 3000) #Ejecuta el localhost
