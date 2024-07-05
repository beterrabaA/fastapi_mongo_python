from pymongo import MongoClient
import os

url = os.environ.get('DATABASE_URL')

client = MongoClient(url)

db = client.todo_db

collection_name = db['collection_todo']
