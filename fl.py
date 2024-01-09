from flask import Blueprint, render_template, redirect, url_for,Flask,request, session, flash
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy 
from config import settings
from db import connect_to_db
import cloudinary
import cloudinary.uploader
import os
import asyncpg

app = Flask(__name__)
app.config["SESSION_TYPE"]= "filesystem"
Session(app)
db=SQLAlchemy(app)



@app.route("/")
def home():
    return  render_template("home.html")