from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import datetime

app = Flask(__name__)
CORS(app)

# Koneksi ke MongoDB
try:
    client = MongoClient("mongodb+srv://agungMq135:agungmq135@cluster0.h9eyb.mongodb.net/?retryWrites=true&w=majority")
    db = client["sensor_data"]
    collection = db["mq135"]
    print("MongoDB connected successfully")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Endpoint untuk menerima data dari ESP32
@app.route('/api/sensor', methods=['POST'])
def receive_sensor_data():
    try:
        data = request.get_json()
        if "gasLevel" not in data:
            return jsonify({"error": "Data tidak lengkap"}), 400

        gas_level = data["gasLevel"]
        timestamp = datetime.datetime.now()
        collection.insert_one({
            "gasLevel": gas_level,
            "timestamp": timestamp
        })
        return jsonify({"message": "Data berhasil disimpan"}), 200

    except Exception as e:
        print(f"Error while saving data: {e}")
        return jsonify({"error": "Failed to save data"}), 500

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
