'''
Database models for use with peewee, business logic, etc.
models import app, but app does not import models...
'''

from peewee import *
from app import db

class BaseModel(Model):
  class Meta:
    database = db # Models that extends BaseModel uses the tweepee.db database

class User(BaseModel):
  username = CharField()
