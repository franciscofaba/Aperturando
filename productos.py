from sqlite3 import Timestamp
from datetime import datetime



class Producto:
    def __init__(self, producto_id, contenedor_id, pais, peso, peso_preaviso, estado, pais_destino, fecha):
        self.producto_id = producto_id
        self.contenedor_id = contenedor_id
        self.pais = pais
        self.peso = peso
        self.peso_preaviso = peso_preaviso
        self.estado = estado
        self.pais_destino = pais_destino
        self.fecha = fecha






def construir_producto():
    

    var_producto=input("ingresa producto:")
    var_contenedor=input("ingresa contenedor:")
    var_pais=input("ingresa pais:")
    var_peso=input("ingresa peso:")
    var_peso_preaviso=input("ingresa peso_preaviso:")
    var_estado=input("ingresa estado:")
    var_pais_destino=input("ingresa pais_destino")
    dt = datetime.now()
    var_fecha=dt


    objeto = Producto(var_producto,var_contenedor, var_pais, var_peso, var_peso_preaviso, var_estado, var_pais_destino, var_fecha)
    return(objeto)

    

