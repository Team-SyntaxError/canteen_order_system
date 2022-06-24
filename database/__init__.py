from pymongo import MongoClient

from pymongo.errors import ConnectionFailure

try:
    mongo_client = MongoClient("mongodb://demo:nj7XPPKsAYnXRC26@ac-yxm9bwo-shard-00-00.rxay9px.mongodb.net:27017,ac-yxm9bwo-shard-00-01.rxay9px.mongodb.net:27017,ac-yxm9bwo-shard-00-02.rxay9px.mongodb.net:27017/?ssl=true&replicaSet=atlas-b36efq-shard-0&authSource=admin&retryWrites=true&w=majority")
    mongo_client.server_info()
except ConnectionFailure:
    print("Invalid Mongo DB URL. Please Check Your Credentials! Exiting...")
    quit(1)


db_x = mongo_client["FC"]
