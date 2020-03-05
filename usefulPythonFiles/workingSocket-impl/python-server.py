from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'wow-super-secret'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "index page"



@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('message')
def message(data):
  print(f"{data}")
  send(data)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    print("Running server")
    socketio.run(app, host="0.0.0.0")

# https://www.google.com/search?rlz=1C1GCEU_enUS884US884&sxsrf=ALeKk01uX_g4OU1_0UcORSDJZjBYKQGyNA%3A1582827253128&ei=9QZYXt-wB8fUtQXR6oXoDA&q=create+socket+with+socketio+flask&oq=create+socket+with+socketio+flask&gs_l=psy-ab.3..33i22i29i30.5748.7317..7465...1.2..1.203.951.0j6j1....2..0....1..gws-wiz.......0i71j33i22i29i30i395j33i10i160j33i10i299.Bl3H_rAxXnc&ved=0ahUKEwif_6aBq_LnAhVHaq0KHVF1Ac0Q4dUDCAs&uact=5#kpvalbx=_CAdYXqGaJ4yEtQXAurDIDQ20
