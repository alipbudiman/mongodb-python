from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

cluster = "mongodb+srv://<your username>:<user password>@cluster0.9sdvp.mongodb.net/<your database name>?retryWrites=true&w=majority"

"""
how to create cluster?
1. create project
2. build cluster (in cluster in data storage menu view)
3. Chosee a path (i select shared cluster #free) and setting cloud & provider
4. after that. click connect and add your current ip adress.
5. addd your username & password.
6. after create user, klick connect your aplication.
7. selcet driver to python and the version of your python version.
6. the mongodb will send you connection string, and that your cluster (variabel).
"""

client = MongoClient(cluster)

print(client.list_database_names())

db = client.test

print(db.list_collection_names())

todos = db.todos

#---------------------------------///////-------------------------------#

todo1 = {"name":"Adminfxg","text":"my first todo","status":"open",
        "tags":["python","coding"],"date":str(datetime.utcnow())}

result = todos.insert_one(todo1)

"""
insert one database
"""

todo2 = [{"name":"Adminfxg2","text":"my second todo","status":"open",
        "tags":["python","coding"],"date":str(datetime.utcnow())},
        {"name":"Adminfxg3","text":"my third todo","status":"open",
        "tags":["python","coding"],"date":str(datetime.utcnow())}]

result = todos.insert_many(todo2)

"""
insert multiple database
"""

result = todos.find_one()
print(result)

"""find one methode"""

result = todos.find_one({"name":"Adminfxg2","text":"my second todo"})
print(result)

"""find one methode with data"""



result = todos.find_one({"tags":"python"})
print(result)

"""find one methode with data tag"""

result = todos.find_one({"_id": ObjectId("61d5b8a28b09d4e29c0fbbd3")})
print(result)

"""find one methode with object id"""


result = todos.find({"name":"Adminfxg2"})
print(list(result)) #<< for cek out!!
for res in result:
    print(res)

"""find methode with data"""


print(todos.count_documents({}))

"""find total documents"""


print(todos.count_documents({"tags":"python"}))

"""find total documents with data /  tag"""

d = datetime(2021,12,12)
result = todos.find({"date": {"$lt":d}})
for res in result:
    print(res)

"""find data by date"""

d = datetime(2021,12,12)
result = todos.find({"date": {"$lt":d}}).sort("name") #<< shorting with key
for res in result:
    print(res)

"""find data by date"""

result = todos.delete_one({"_id":ObjectId("61d5b6637a2c20e62caf50c7")})

"""remove data by delete_one"""

result = todos.delete_many({"status":"open"})

"""remove data by delete_many"""


result = todos.update_one({"tags":"python"},{"$set":{"status":"close"}})

"""update data by update_one & $set"""

result = todos.update_one({"tags":"python"},{"$unset":{"status":None}})

"""update data by update_many & $unset"""


result = todos.update_one({'tags': 'python'}, {'$push': {'tags': "mongodb"}})
"""update data list by update_one and $push (for adding new value to data arry)"""

result = todos.update_one({'tags': 'python'}, {'$pull': {'tags': "mongodb"}})
"""update data list by update_one and $push (for deleting value from data arry)"""

"""find the referance here : https://docs.mongodb.com/manual/reference/operator/"""

