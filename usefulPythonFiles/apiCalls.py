import requests

data = requests.get("https://api.thecatapi.com/v1/images/search?size=full")
data = data.json()
print(data[0]["url"])