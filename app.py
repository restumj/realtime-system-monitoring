from flask import Flask
from waitress import serve
import json
import psutil

def create_data_json():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    return {'cpu_usage': f'{cpu_usage:.2f}%', 'total_ram': f'{ram.total/(1024**3):.2f} GB', 'available_ram': f'{ram.available/(1024**3):.2f} GB', 'used_ram': f'{ram.used/(1024**3):.2f} GB', 'ram_usage': f'{ram.percent:.2f}%'}

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