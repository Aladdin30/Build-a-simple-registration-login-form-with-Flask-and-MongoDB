import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017")

db=myclient["company"]
col=db['customer']

print(myclient.list_database_names())
print(db.list_collection_names())
#--------------------to insert one---------------
# info={"name":"shady","address":"Alex"}
# x=col.insert_one(info)
# for n in col.find({},{ "address": 0 }):
#     print(n)
#--------------------to insert many--------------

# mylist = [
#     { "name": "Amy", "address": "Apple st 652"},
#     { "name": "Hannah", "address": "Mountain 21"},
#     { "name": "Michael", "address": "Valley 345"},
#     { "name": "Sandy", "address": "Ocean blvd 2"},
#     { "name": "Betty", "address": "Green Grass 1"},
#     { "name": "Richard", "address": "Sky st 331"},
#     { "name": "Susan", "address": "One way 98"},
#     { "name": "Vicky", "address": "Yellow Garden 2"},
#     { "name": "Ben", "address": "Park Lane 38"},
#     { "name": "William", "address": "Central st 954"},
#     { "name": "Chuck", "address": "Main Road 989"},
#     { "name": "Viola", "address": "Sideway 1633"}
# ]
# x=col.insert_many(mylist)

#--------------------to find one--------------

# x = col.find_one() #this will return the first one 
# print(x)

#--------------------to find many--------------

# for x in col.find():
#     print(x)

#--------------------to find many--------------
# 0 means will not appear 1 means will appear

# for x in col.find({},{ "_id": 0, "name": 1, "address": 1 }):
#     print(x)

#--------------------Filter the Result--------------

# myquery = { "address": "Park Lane 38" }

# mydoc = col.find(myquery)

# for x in mydoc:
#     print(x)
    
#--------------------Find documents where the address starts with the letter "S" or higher--------------
#use the greater than modifier: {"$gt": "S"}:

# myquery = { "address": {"$gt": "Park Lane 38" }}
# x=col.find(myquery)
# for r in x:
#     print(r)
    
#--------------------Find documents where the address starts with the letter "S"--------------

# myquery = { "address": { "$regex": "^S" } }
# mydoc = col.find(myquery)
# for x in mydoc:
#     print(x)

#--------------------Sort the result alphabetically by name:--------------

# mydoc = col.find().sort("name")
# for x in mydoc:
#     print(x)

#--------------------Sort the result reverse alphabetically by name:--------------

# mydoc = col.find().sort("name", -1)
# for x in mydoc:
#     print(x)
    
#--------------------Delete the document with the address "Mountain 21"--------------

# myquery = { "address": "Mountain 21" }
# col.delete_one(myquery)

#--------------------Delete all documents were the address starts with the letter S--------------

# myquery = { "address": {"$regex": "^S"} }
# x = col.delete_many(myquery)
# print(x.deleted_count, " documents deleted.")

#--------------------Delete all documents in the "customers" collection:--------------

# x = col.delete_many({})
# print(x.deleted_count, " documents deleted.")

#--------------------Delete the "customers" collection:--------------

# col.drop()

#--------------------Change the address from "Valley 345" to "Canyon 123":--------------

# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }
# col.update_one(myquery, newvalues)
# #print "customers" after the update:
# for x in col.find():
#     print(x)

#--------------------Update all documents where the address starts with the letter "S":--------------

# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }
# x = col.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")

#--------------------Limit the result to only return 5 documents:--------------

myresult = col.find().limit(5)
#print the result:
for x in myresult:
    print(x)

