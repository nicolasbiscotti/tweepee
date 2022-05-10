'''
This is a single entry-point the resolves the import dependencies.

When we want to run the app, you point to main.py
'''

from app import app, db 
from models import *

def create_tables():
  # Create table for each model if it does not exist.
  db.create_tables([User], safe=True)

def drop_tables():
  # Drop table for each model if it does exist.
  db.drop_tables([User])

if __name__ == '__main__':
  create_tables()
  app.run(host='localhost', port=5000)
