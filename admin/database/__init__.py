from pymongo import MongoClient
import sys
from pymongo.errors import ConnectionFailure
import os
dir_path = os.path.dirname(os.path.realpath(__file__)).split("\\")
dir_path="\\".join(x for x in dir_path[:-2])
sys.path.append(dir_path)
from config import MONGO_URL
try:
    mongo_client = MongoClient(MONGO_URL)
    mongo_client.server_info()
except ConnectionFailure:
    print("Invalid Mongo DB URL. Please Check Your Credentials! Exiting...")
    quit(1)


db_x = mongo_client["FC"]
