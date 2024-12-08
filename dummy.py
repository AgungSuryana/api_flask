import requests
import random
import time
from datetime import datetime

# URL backend Flask
backend_url = "http://agungPython.pythonanywhere.com/api/sensor"

def send_data_to_backend():
    try:
        # Data dummy
        gas_level = random.randint(100, 500)  # Nilai gasLevel acak antara 100-500
        timestamp = datetime.now().isoformat()  # Tambahkan timestamp otomatis

        # Payload hanya berisi gasLevel dan timestamp
        payload = {
            "gasLevel": gas_level,
            "timestamp": timestamp  # Kirimkan timestamp jika diinginkan
        }

        # Kirim POST request ke backend
        response = requests.post(backend_url, json=payload)

        # Tampilkan respons dari server
        if response.status_code == 200:
            print("Data berhasil dikirim!")
            print("Response:", response.json())
        else:
            print(f"Gagal mengirim data. Status code: {response.status_code}")
            print("Error:", response.text)

    except Exception as e:
        print("Terjadi kesalahan:", e)

if __name__ == "__main__":
    print("Program pengirim data dummy ke backend Flask")
    while True:
        # Kirim data setiap 5 detik
        send_data_to_backend()
        time.sleep(5)  # Jeda 5 detik
