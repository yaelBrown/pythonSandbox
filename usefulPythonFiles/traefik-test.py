import base64

l = [
        {
            "yaell-2-operator-1" : "192.168.1.2"
        }
    ]

# print("asdf" + str(l) + "affdsa")

# ovm = [{'vm_name': 'yael-1-apache-guacamole', 'ip': '10.128.15.221', 'vm_hash': 'eWFlbC0xLWFwYWNoZS1ndWFjYW1vbGU='}, {'vm_name': 'yael-1-elastic-stack', 'ip': '10.128.15.220', 'vm_hash': 'eWFlbC0xLWVsYXN0aWMtc3RhY2s='}]

operators = [{ "vm_name" : "yael-1-operator-1" }, { "vm_name" : "yael-1-operator-30"}]

# oid = operators[1]["vm_name"][-2:len(operators[1]["vm_name"])]
# oid = int(oid)
# if oid < 0:
#     oid = abs(oid)

# print(oid)

# b64 = str(base64.b64encode(f"{oid}\x00c\x00mysql".encode()))[2:-1]
# url = f"http://localhost:8085/guacamole/#/client/{b64}?username=guacadmin&password=o7paFdT$F7cH!atq"

# print(url)

# traefikOutput = []
# for o in operators:
#   oid = operators[1]["vm_name"][-2:len(operators[1]["vm_name"])]
#   oid = int(oid)
#   if oid < 0:
#       oid = abs(oid)
#   b64 = str(base64.b64encode(f"{oid}\x00c\x00mysql".encode()))[2:-1]
#   url = f"http://localhost:8085/guacamole/#/client/{b64}?username=guacadmin&password=o7paFdT$F7cH!atq"
#   out = {
#     "FE_Path" : o["vm_hash"],
#     "BE_Path" : url
#   }
#   traefikOutput.add(out)

traefikOutput = [{'FE_Path': 'eWFlbC0xLW9wZXJhdG9yLTE', 'BE_Path': 'http://localhost:8085/guacamole/#/client/MQBjAG15c3Fs?username=guacadmin&password=o7paFdT$F7cH!atq'}]

if len(traefikOutput) == 1:
  # asdf
  pass
else:
  pass


print(len(traefikOutput))