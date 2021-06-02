from pymongo import MongoClient

# print("atlas app file is working")

client = MongoClient("mongodb+srv://username:password@peterest-db.fkffd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('Peterest_db')
users_db = db.users

print(users_db.count_documents({}))
