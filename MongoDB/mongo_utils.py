from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["items"]

def create_item(item):
    result = collection.insert_one(item)
    return str(result.inserted_id)

def read_item(item_id):
    result = collection.find_one({"_id": ObjectId(item_id)})
    result["_id"] = str(result["_id"])
    return result

def update_item(item_id, update_data):
    collection.update_one({"_id": ObjectId(item_id)}, {"$set": update_data})
    return read_item(item_id)

def delete_item(item_id):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0
