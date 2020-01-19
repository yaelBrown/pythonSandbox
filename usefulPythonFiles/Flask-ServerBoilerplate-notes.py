# import flask after installing it
from flask import Flask, redirect, url_for

# Create the instance of the flask application
app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>Hello from Flask!</h1>"

@app.route("/<name>")
def user(name):
  return f"Hello {name}"

@app.route("/admin")
def admin():
  return redirect(url_for(home))

# if this file is directly ran, it will run app.run()
if __name__ == "__main__":
  app.run()

"""
Change the port:
  app.port(port=6969)

"""
