import requests

base_url = 'http://192.168.56.1:3000/api'


def create_envios(data):
    try:
        url = f'{base_url}/envios'
        response = requests.post(url, json=data)
        return response.json()
    except Exception as e:
        print(f"Error al crear datos: {e}")
        return None

def read_envios(data_id):
    try:
        url = f'{base_url}/envios/{data_id}'
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error al leer datos: {e}")
        return None

def read_all_envios():
    try:
        url = f'{base_url}/envios'
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error al leer todos los datos: {e}")
        return None

def update_envios(data_id, new_data):
    try:
        
        url = f'{base_url}/envios/{data_id}'
        response = requests.patch(url, json=new_data)
        
        return response.json() 
    except Exception as e:
        print(f"Error al actualizar datos: {e}")
        return None
    

def delete_envios(data_id):
    try:
        url = f'{base_url}/envios/{data_id}'
        response = requests.delete(url)
        return response.status_code == 204
    except Exception as e:
        print(f"Error al eliminar datos: {e}")
        return False

def read_envios_by_lotes(data_id):
    try:
        url = f'{base_url}/envios/lotes/{data_id}'
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error al leer todos los datos: {e}")
        return None
    
def read_all_en_proceso():
    try:
        url = f'{base_url}/envios1/proceso/'
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error al leer todos los datos: {e}")
        return None
    
def read_all_en_proceso_cp():
    try:
        url = f'{base_url}/envios1/procesocp/'
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error al leer todos los datos: {e}")
        return None
    
def read_all_en_proceso_ems():
    try:
        url = f'{base_url}/envios1/procesoems/'
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error al leer todos los datos: {e}")
        return None