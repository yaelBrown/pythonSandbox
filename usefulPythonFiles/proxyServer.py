from flask import Flask, Response
from flask_cors import CORS

import requests

app = Flask(__name__)
CORS(app)

url = "https://www.newegg.com"

@app.route('/test', methods=['GET'])
def getTest():
  r = requests.get(url, stream=True)
  print(r)
  print("HEADERS=", r.headers)
  return Response(r.iter_content(chunk_size=10*1024),
                    content_type=r.headers['Content-Type'])

if __name__ == "__main__":
  app.run(debug=True)