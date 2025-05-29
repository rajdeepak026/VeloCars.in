from flask import Flask, render_template, redirect, request, session
from flask import current_app as app 
from .models import *

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/services")
def offer():
    return render_template("services.html")