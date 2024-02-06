from sqlite3 import Timestamp
from datetime import datetime
from conexion_api import read_data
import json

class Producto:
    def __init__(self, envio, envase, paisOrigen, pesoEspecificado, pesoPreaviso, estadoActual, paisDestino, ultimaModificacion):
        self.envio = envio
        self.envase = envase
        self.paisOrigen = paisOrigen
        self.pesoEspecificado = pesoEspecificado
        self.pesoPreaviso = pesoPreaviso
        self.estadoActual = estadoActual
        self.paisDestino = paisDestino
        self.ultimaModificacion = ultimaModificacion


def construir_producto(var_ID):

    data = read_data(var_ID)


    envio = data.get('envio')
    pesoPreaviso = data.get('pesoPreaviso')
    envase = data.get('envase')
    claseEnvio = data.get('claseEnvio')
    estadoActual = data.get('estadoActual')
    ultimoAcontecimiento = data.get('ultimoAcontecimiento')
    paisOrigen = data.get('paisOrigen')
    paisDestino = data.get('paisDestino')
    ultimaModificacion = data.get('ultimaModificacion')
    identificadorLocal = data.get('identificadorLocal')
    manifiesto = data.get('manifiesto')
    pesoEspecificado = data.get('pesoEspecificado')

    objeto = Producto(envio ,envase, paisOrigen, pesoPreaviso, pesoEspecificado,estadoActual, paisDestino, ultimaModificacion)

    return(objeto)
  