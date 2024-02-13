
from crud_envios import update_envios
from crud_lotes import create_lotes


def updt_prod_lot(lista_producto,estado_aduana,timedata):
    id_lote = timedata.strftime("LOTE-%Y%m%d%H%M%S")
    print(lista_producto)
    for item in lista_producto:
        
        id = item.get('envio')
        datos = {
        "estado_aduana": estado_aduana,
        "id_lotes": id_lote,
        "en_proceso": ""
        }

        update_envios(id, datos)
        
        
    
        
    param_lotes = {
    "id_lote": id_lote,
    "estado_aduana":estado_aduana,
    "estado_despacho": "en espera"
    }
    
    lotes = create_lotes(param_lotes)
    
    return id_lote