import requests
base_url = 'http://192.168.56.1:3000/api'

def create_lotes(data):
    try:
        url = f'{base_url}/lotes'
        response = requests.post(url, json=data)
        return response.json()
    except Exception as e:
        print(f"Error al crear datos: {e}")
        return None

def read_lotes(data_id):
    try:
        url = f'{base_url}/lotes/{data_id}'
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error al leer datos: {e}")
        return None

def read_all_lotes():
    try:
        url = f'{base_url}/lotes'
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error al leer todos los datos: {e}")
        return None

def update_lotes(data_id, new_data):
    try:
        url = f'{base_url}/lotes/{data_id}'
        response = requests.patch(url, json=new_data)
        return response.json()
    except Exception as e:
        print(f"Error al actualizar datos: {e}")
        return None

def delete_lotes(data_id):
    try:
        url = f'{base_url}/lotes/{data_id}'
        response = requests.delete(url)
        return response.status_code == 204
    except Exception as e:
        print(f"Error al eliminar datos: {e}")
        return False
