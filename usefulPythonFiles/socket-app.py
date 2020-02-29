from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
​
app = Flask(__name__)
app.config['SECRET_KEY'] = "WOW-SUPER-SECRET"
​
sio = SocketIO(app)
​
@SocketIO.on(sio, 'connect')
def test_connect():
  emit('myResponse', { 'data': 'Connected' })
​
@SocketIO.on(sio, 'disconnect')
def test_disconnect():
  print("Client disconnected")
​
​
​
@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "GET":
    return "Working with GET requests!"
  elif request.method == "POST":
    return "Working with POST requests!"
​
@app.route("/connect", methods=["POST"])
@SocketIO.on(sio, 'connect')
def connect():
  if request.method != "POST":
    return "This must be a post"
  else:
    omn = request.json.get("omn") # omn = Operator Machine Name
​
​
​
if __name__ == '__main__':
  sio.run(app, debug=True)
​
​
# https://www.google.com/search?rlz=1C1GCEU_enUS884US884&sxsrf=ALeKk01uX_g4OU1_0UcORSDJZjBYKQGyNA%3A1582827253128&ei=9QZYXt-wB8fUtQXR6oXoDA&q=create+socket+with+socketio+flask&oq=create+socket+with+socketio+flask&gs_l=psy-ab.3..33i22i29i30.5748.7317..7465...1.2..1.203.951.0j6j1....2..0....1..gws-wiz.......0i71j33i22i29i30i395j33i10i160j33i10i299.Bl3H_rAxXnc&ved=0ahUKEwif_6aBq_LnAhVHaq0KHVF1Ac0Q4dUDCAs&uact=5#kpvalbx=_CAdYXqGaJ4yEtQXAurDIDQ20