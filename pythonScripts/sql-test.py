import pymysql

con = pymysql.Connect(
  host='localhost', 
  user='root', 
  password='petmeplz', 
  db='peterest_db', 
  charset='utf8', 
  cursorclass=pymysql.cursors.DictCursor, 
  port=3306)

cur = con.cursor()







sql = "Select id, email, password from users where email = %s"

cur.execute(sql, ("yaelster@yaelbrown.com"))

res = cur.fetchone()

print(res)