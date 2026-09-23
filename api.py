import json
import psutil

def crete_data_json():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    data = {'cpu': cpu_usage, 'total_ram': ram.total/(1024**3), 'available_ram': ram.available/(1024**3), 'used_ram': ram.used/(1024**3), 'ram_usage_percentage': ram.percent}
    with open('api.json','w') as f:
        json.dump(data,f,indent=4)