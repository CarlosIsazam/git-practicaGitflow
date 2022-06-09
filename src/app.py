from ast import Return
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Adios codigo"

@app.route('/Hola')
def greating():
    return "Hola Mundo"