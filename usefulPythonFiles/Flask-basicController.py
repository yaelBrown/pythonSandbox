from flask import Flask, Blueprint

Controller = Blueprint('Controller', __name__)

class Controller(): 
  @Controller.route('/test', )
  def test():
    return {'msg': 'this test works'}, s200
