from pymongo import MongoClient

mongo_client = None
mongo_db = None

def init_mongo(host, port, db_name):
	global mongo_client, mongo_db
	mongo_client = MongoClient(host, port)
	mongo_db = mongo_client[db_name]

