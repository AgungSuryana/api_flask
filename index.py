from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://agungMq135:agungmq135@cluster0.h9eyb.mongodb.net/?retryWrites=true&w=majority")
db = client["sensor_data"]
collection = db["mq135"]

@app.route('/data', methods=['GET'])
def get_data():
    data = collection.find()
    return dumps(data)  # Convert Mongo data to JSON

@app.route('/data', methods=['POST'])
def add_data():
    new_data = request.get_json()
    collection.insert_one(new_data)
    return jsonify({"message": "Data added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
