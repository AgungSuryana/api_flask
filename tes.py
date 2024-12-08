from pymongo import MongoClient

client = MongoClient("mongodb+srv://agungMq135:agungmq135@cluster0.h9eyb.mongodb.net/?retryWrites=true&w=majority")
db = client["sensor_data"]
collection = db["mq135"]

print(collection.find_one())
