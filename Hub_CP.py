from turtle import tracer
from Front_CP import iniciar_ventana_cp
from tkinter import ttk
import tkinter as tk
from tkinter import *




def hub_cp():
    def abrir_front():
        root_cp.destroy()
        iniciar_ventana_cp()
    

   
    root_cp = tk.Tk()
    root_cp.geometry("500x500")

    """"DEFINICION ESTILO"""
    style = ttk.Style()
    style.theme_create( "MyStyle", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [5, 5, 490, 5] } },
            "TNotebook.Tab": {"configure": {"padding": [5, 5] },}})

    style.theme_use("xpnative")

    """DEFINICION TABS"""
    tabControl = ttk.Notebook(root_cp)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)

    tabControl.add(tab1, text ='EMS', state="disable") 
    tabControl.add(tab2, text ='Encomiendas') 
    tabControl.grid(row=0,column=0)


    """TREEVIEW"""

    treeview = ttk.Treeview(tab2,show="tree",columns=("#0"), height=20)

    #columnas y heading
    treeview.column("#0", anchor="w", minwidth=360, width=242, stretch=YES)


    
    #items que contiene el treeview

    folder_image = tk.PhotoImage(file="icons/folder.png")
    folder_image = folder_image.subsample(15)
    arrow_image = tk.PhotoImage(file="icons/arrow-big-right.png")
   

    item_llegada=treeview.insert("", tk.END,text="   LLegada:", open=TRUE,image=folder_image)
    item_encomiendas = treeview.insert(item_llegada, tk.END, text="   Encomiendas:", open=TRUE,image=folder_image)

    item1 = treeview.insert(item_encomiendas, tk.END,text="Recibe Encomiendas en oficina de Cambio CC y Aduana", image=arrow_image)
    item2 = treeview.insert(item_encomiendas, tk.END,text="Enviar Envios desde Oficina de Cambio Con Manifiesto")
    
    treeview.selection_toggle(item1)

    


    
    
   
    treeview.grid(row=0, column=0,padx=25,pady=10,columnspan=10, sticky="nsew")

    """botones"""
   
    tk.Frame.boton_abrir = ttk.Button(tab2, text="Ejecutar", command=abrir_front)
    tk.Frame.boton_abrir.grid(row=5,column=0,pady=5, ipadx=5)
    tk.Frame.boton_atras =ttk.Button(root_cp, text="atras", width=5).grid(row=0,column=0,pady=4, padx=27, sticky="ne")

    root_cp.mainloop()

if __name__ == "__main__":


    

    hub_cp()