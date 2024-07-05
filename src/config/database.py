from pymongo import MongoClient
import os

url = os.environ.get('DATABASE_URL')

client = MongoClient(url)

db = client['DATABASE_NAME']

collection_name = db['DATABASE_COLLECTION']
