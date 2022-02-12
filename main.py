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

myquery = { "address": "Park Lane 38" }
mydoc = todos.find(myquery)

for x in todos:
  print(x)

"""
find query
"""

# Find documents where the address starts with the letter "S" or higher:
myquery = { "address": { "$gt": "S" } }

mydoc = todos.find(myquery)

for x in todos:
  print(x)

'''
Advanced Query
To make advanced queries you can use modifiers as values in the query object.

E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:
'''

#To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}:

myquery = { "address": { "$regex": "^S" } }

mydoc = todos.find(myquery)

for x in todos:
  print(x)

'''
Filter With Regular Expressions
You can also use regular expressions as a modifier.
[!] Regular expressions can only be used to query strings.
'''

#Sort the result reverse alphabetically by name:

mydoc = todos.find().sort("name")

for x in todos:
  print(x)

'''
Sort the Result
Use the sort() method to sort the result in ascending or descending order.

The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).
'''

#Sort the result reverse alphabetically by name:

mydoc = todos.find().sort("name", -1)

for x in todos:
  print(x)

'''
Sort Descending & Ascending
Use the value -1 or 1 as the second parameter to sort descending.
exmp:
sort("name", 1) #ascending
sort("name", -1) #descending
'''

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


#Delete the document with the address "Mountain 21":
myquery = { "address": "Mountain 21" }

todos.delete_one(myquery)

'''
Delete Document
To delete one document, we use the delete_one() method.

The first parameter of the delete_one() method is a query object defining which document to delete.

Note: If the query finds more than one document, only the first occurrence is deleted.
'''

#Delete all documents were the address starts with the letter S:
myquery = { "address": {"$regex": "^S"} }

x = todos.delete_many(myquery)

print(x.deleted_count, " documents deleted.")

'''
Delete Many Documents
To delete more than one document, use the delete_many() method.

The first parameter of the delete_many() method is a query object defining which documents to delete.
'''
#Delete all documents in the "customers" collection:


x = todos.delete_many({})

print(x.deleted_count, " documents deleted.")

'''
Delete All Documents in a Collection
To delete all documents in a collection, pass an empty query object to the delete_many() method:
'''

#Delete the "customers" collection:

todos.drop()

'''
Delete Collection
You can delete a table, or collection as it is called in MongoDB, by using the drop() method.
'''



#Limit the result to only return 5 documents:



myresult = todos.find().limit(5)

#print the result:
for x in myresult:
  print(x)

'''
Limit the Result
To limit the result in MongoDB, we use the limit() method.

The limit() method takes one parameter, a number defining how many documents to return.

Consider you have a "customers" collection:
'''



"""find the referance here : https://docs.mongodb.com/manual/reference/operator/"""
