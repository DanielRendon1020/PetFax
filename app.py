from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the index page"

@app.route('/pets')
def pets():
    return "This is the pets page!!!!"