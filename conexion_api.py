import requests

base_url = 'http://192.168.56.1:3000/api/envios'

def create_data(data):
    url = f'{base_url}'
    response = requests.post(url, json=data)
    return response.json()

def read_data(data_id):
    url = f'{base_url}/{data_id}'
    response = requests.get(url)
    return response.json()

def read_all_data():
    url = f'{base_url}'
    response = requests.get(url)
    return response.json()

def update_data(data_id, new_data):
    url = f'{base_url}/{data_id}'
    response = requests.patch(url, json=new_data)
    return response.json()

def delete_data(data_id):
    url = f'{base_url}/{data_id}'
    response = requests.delete(url)
    return response.status_code == 204  # 204 significa 'No Content', indicando éxito sin respuesta




