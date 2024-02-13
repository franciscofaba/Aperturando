import tkinter as tk
from tkinter import *
from tkinter import ttk
from crud_lotes import read_all_lotes
from crud_envios import read_envios_by_lotes
import sys
from Actualizar_lotes import actualizar_lotes

def main_lotes(root):
    
# ____Funciones: 
    def cerrar_ventana():
            sys.exit()    
            ROOT_CP.destroy()

    def cargar():
        tree.delete(*tree.get_children())
        id_lotes = lista_lotes.get()
        lista_productos = read_envios_by_lotes(id_lotes)
        print(lista_productos)
        for item in lista_productos:
           
            tree.insert('', 'end', text="1", values=(item.get('envio'), item.get('envase'),item.get('paisOrigen'), item.get('pesoEspecificado'), item.get('pesoPreaviso'), item.get('estadoActual'), item.get('paisDestino'), item.get('ultimaModificacion')))
    def volver():
        root.deiconify() 
        ROOT_lotes.destroy()
        
    def act_dspcho():
        tree.delete(*tree.get_children())
        id =lista_lotes.get()
        actualizar_lotes(id)
        
        
        
    def desplegar(lista):
        json_lotes = read_all_lotes()
        
        for i in json_lotes:
            id_lote=i.get("id_lote")
            lista.append(id_lote)
        return(lista)

# ____ Iniciar la ventana: 
    # llamar ventana
    ROOT_lotes = Toplevel()
    ROOT_lotes.title("Nuevo IPS")
    # datos para las dimesiones
    w = 740
    h = 400
    ws = ROOT_lotes.winfo_screenwidth()
    hs = ROOT_lotes.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)


    # geometria de la ventana
    ROOT_lotes.geometry('%dx%d+%d+%d' % (w, h, x, y))
    ROOT_lotes.protocol("WM_DELETE_WINDOW", cerrar_ventana)
    ROOT_lotes.resizable(0,0)
    
    style = ttk.Style()
    style.theme_use('clam')
    
    ROOT_lotes
#________________________



    # Lista desplegable 
    
    lista=[]
    try:
        lista = desplegar(lista)
    except Exception as e:
        print("Ocurrió un error:", e)
    
    etiqueta_lotes= tk.Label(ROOT_lotes, text="Lotes disponibles para despacho:").place(x=50,y=30)
    lista_lotes = ttk.Combobox(
        ROOT_lotes,
        state="readonly",
        values=lista,
        width=50
    )
    try:
        lista_lotes.current(0)
    except Exception as e:
        print("Ocurrió un error:", e)
        
    lista_lotes.place(x=50,y=55)

    
    boton_cargar = ttk.Button(ROOT_lotes, text="Cargar", command=cargar , width=10).place(x=50, y=80)
    
    tree = ttk.Treeview(ROOT_lotes, column=("c1", "c2", "c3","c4","c5","c6","c7","c8"), show='headings', height=6)
    tree.column("# 1", anchor=CENTER, minwidth=0, width=80, stretch=NO)
    tree.heading("# 1", text="Envio")
    tree.column("# 2", anchor=CENTER, minwidth=0, width=80, stretch=NO)
    tree.heading("# 2", text="Envase")
    tree.column("# 3", anchor=CENTER, minwidth=0, width=80, stretch=NO)
    tree.heading("# 3", text="Pais de Origen")
    tree.column("# 4", anchor=CENTER, minwidth=0, width=80, stretch=NO)
    tree.heading("# 4", text="Peso Real(kg.)")
    tree.column("# 5", anchor=CENTER, minwidth=0, width=80, stretch=YES)
    tree.heading("# 5", text="Peso con Preaviso (kg.)")
    tree.column("# 6", anchor=CENTER, minwidth=0, width=80, stretch=NO)
    tree.heading("# 6", text="Estado Actual")
    tree.column("# 7", anchor=CENTER, minwidth=0, width=80, stretch=NO)
    tree.heading("# 7", text="Pais de Destino")
    tree.column("# 8", anchor=CENTER, minwidth=0, width=80, stretch=NO)
    tree.heading("# 8", text="Ultima Modificacion")
    tree.place(x=50, y=120)
    
    
    boton_atras = tk.Button(ROOT_lotes, text="Volver" , width=8, command=volver).place(x=625, y=20)
    boton = ttk.Button(ROOT_lotes, text="Proceder Despacho" , width=18, command = act_dspcho).place(x=580, y=340)
    ROOT_lotes.mainloop()
    
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    main_lotes(root)