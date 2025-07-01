from pymongo import MongoClient


MONGO_URI = "mongodb://localhost:27017"
MONGO_DB = "notes"
MONGO_COLLECTION = "notes"


conn = MongoClient(MONGO_URI)
db = conn[MONGO_DB]
collection = db[MONGO_COLLECTION]


def get_collection():
    return collection