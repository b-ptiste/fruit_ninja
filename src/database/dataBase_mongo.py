from pymongo import MongoClient
#Creating a pymongo client

def connect_to_db():
    client = MongoClient('localhost', 27017)
    return client

def disconect_to_db(client):
    client.close()

def add_score(db, name, score):
    coll = db['scores']
    #Inserting document into a collection
    doc = {"name": name, "score": score}
    coll.insert_one(doc)
    
