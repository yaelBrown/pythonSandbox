import requests
from bs4 import BeautifulSoup
import sqlite3
import gzip

filename="\\Local\\Google\\Chrome\\User Data\\Default\\Cookies" #EDIT ME
connection = sqlite3.connect(filename)
cursor = connection.cursor()
cursor.execute("SELECT * FROM cookies;")
results = cursor.fetchall()

for r in results:
    site=r[1]
    type=r[2]
    code=str(r[12])
    vSite=site.find("ENTER WEBSITE")
    if vSite > -1:
        print(site+': '+'\t'+type+'\n'+'\n'+code+'\n')
cursor.close()
connection.close()