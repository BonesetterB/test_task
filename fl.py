from flask import Blueprint, render_template, redirect, url_for,Flask,request, session, flash
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy 
from db import connect_to_database
import model
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
app.config["SESSION_TYPE"]= "filesystem"
Session(app)
db=SQLAlchemy(app)



@app.route("/", methods=['GET', 'POST','DELETE','PUT'])
def home():
    return  render_template("home.html")

@app.route("/", methods=['GET', 'POST','DELETE','PUT'])
def client():
    pass

@app.route("/", methods=['GET', 'POST'])
def message():
    pass
app.run(debug=True)