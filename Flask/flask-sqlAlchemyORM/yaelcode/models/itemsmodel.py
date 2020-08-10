import sqlite3 

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class ItemModel: 
  # constructor
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def json(self):
    return {'name': self.name, 'price': self.price }

  @classmethod
  def find_by_name(cls, name):
    pass
    # define connection to db
    # define cursor

    # query
    # create variable for return
    # get one user from results
    # close connection

    #construct output