
from crud_envios import read_envios

class Producto:
    def __init__(self, envio, envase, paisOrigen, pesoEspecificado, pesoPreaviso, estadoActual, paisDestino, ultimaModificacion, destino_cl, destino_aduana, id_lote):
        self.envio = envio
        self.envase = envase
        self.paisOrigen = paisOrigen
        self.pesoEspecificado = pesoEspecificado
        self.pesoPreaviso = pesoPreaviso
        self.estadoActual = estadoActual
        self.paisDestino = paisDestino
        self.ultimaModificacion = ultimaModificacion
        self.destino_cl = destino_cl
        self.destino_aduana = destino_aduana
        self.id_lote = id_lote

def llamar_producto(var_ID):

    data = read_envios(var_ID)
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
    destino_cl=data.get('destino_cl')
    destino_aduana = data.get('destino_aduana')
    id_lote = data.get('id_lote')

    objeto = Producto(envio, envase, paisOrigen, pesoPreaviso, pesoEspecificado, estadoActual, paisDestino, ultimaModificacion, destino_cl,destino_aduana, id_lote)

    return(objeto)
  