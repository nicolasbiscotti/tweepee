'''
Flask application, configuration and database.
'''
DATABSE = 'tweepee.db'

from flask import Flask
from peewee import SqliteDatabase

app = Flask(__name__)

db = SqliteDatabase(DATABSE)




