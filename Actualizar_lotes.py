from crud_envios import read_envios_by_lotes, update_envios
from crud_lotes import  update_lotes

def actualizar_lotes(id):
    
    lote = read_envios_by_lotes(id)
    
    data_updt= {
        "estado_despacho":"Despachado"
    }
    update_lotes(id,data_updt)
    
    
    
    for item in lote:
        data= {
        "estado_aduana":"",
        "id_lotes":""
        }
        
        update_envios(item.get("envio"), data)
        
    