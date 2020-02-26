import base64

def urlEncoder(oid):
  return str(base64.b64encode(f"{oid}\x00c\x00mysql".encode()))[2:-1]
print(urlEncoder(33))