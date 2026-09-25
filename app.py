from flask import Flask
from waitress import serve
import json
import psutil

def create_data_json():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    return {'cpu_usage': cpu_usage, 'total_ram': ram.total/(1024**3), 'available_ram': ram.available/(1024**3), 'used_ram': ram.used/(1024**3), 'ram_usage': ram.percent}

app = Flask(__name__)

@app.route('/')
def main():
    text = ""
    with open('templates/index.html','r') as f:
        for baris in f:
            text = text + baris
    return text

@app.route('/api/stats')
def stats():
    return create_data_json()

if __name__ == '__main__':
    serve(app, host='192.168.1.5', port=5000)