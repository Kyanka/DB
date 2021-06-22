import pymongo

client = pymongo.MongoClient("mongodb+srv://kyanka:123@courseworkdb.szutq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client['courseworkDB']
# client = pymongo.MongoClient("mongodb+srv://kyanka:123@courseworkdb.szutq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test

