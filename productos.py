

class Producto:
    def __init__(self, producto_id, contenedor_id, pais, peso):
        self.producto_id = producto_id
        self.contenedor_id = contenedor_id
        self.pais = pais
        self.peso = peso




def construir_producto():

    var_producto=input("ingresa producto:")
    var_contenedor=input("ingresa contenedor:")
    var_pais=input("ingresa pais:")
    var_peso=input("ingresa peso:")

    objeto = Producto(var_producto,var_contenedor, var_pais, var_peso)
    return(objeto)

    