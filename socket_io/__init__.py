import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
SQLITE_DB = os.path.join(os.getcwd(), "fastfingers.db")
APP.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + SQLITE_DB
database = SQLAlchemy(APP)
