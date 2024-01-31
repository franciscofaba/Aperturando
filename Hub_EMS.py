from tkinter.messagebox import YESNOCANCEL
from turtle import tracer
from Front_EMS import iniciar_ventana
from tkinter import ttk
import tkinter as tk
from tkinter import *

def hub():
    def abrir_front():
        root.destroy()
        iniciar_ventana()

   
    root = tk.Tk()
    root.geometry("500x500")

    """"DEFINICION ESTILO"""
    style = ttk.Style()
    style.theme_create( "MyStyle", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [5, 5, 500, 5] } },
            "TNotebook.Tab": {"configure": {"padding": [20, 20] },}})

    style.theme_use("xpnative")

    """DEFINICION TABS"""
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)

    tabControl.add(tab1, text ='EMS') 
    tabControl.add(tab2, text ='Encomiendas', state="disable") 
    tabControl.grid(row=0,column=0)


    """TREEVIEW"""

    treeview = ttk.Treeview(tab1,show="tree", height=20, columns=("#0"))
    treeview.column("#0", anchor="w", minwidth=360, width=242, stretch=YES)


    #columnas y heading
    
    
    #items que contiene el treeview
    arrow_image = tk.PhotoImage(file="icons/arrow-big-right.png")
   

    item1 = treeview.insert("", tk.END,text="Recibe envios EMS de oficina de Cambio CC y Aduana", image=arrow_image)
    item2 = treeview.insert("", tk.END,text="Registra  Informacion de Entrega de Oficina Central")
    item3 = treeview.insert("", tk.END,text="Enviar Envios desde Oficina de Cambio Con Manifiesto")
    item4 = treeview.insert("", tk.END,text="Registrar Informacion del Destinatario")
    

    treeview.selection_toggle(item1)
    
   
    treeview.grid(row=0, column=0,padx=25,pady=10,columnspan=10)

    """botones"""
   
    tk.Frame.boton_abrir = ttk.Button(tab1, text="Ejecutar", command=abrir_front)
    tk.Frame.boton_abrir.grid(row=5,column=0,pady=5, ipadx=5)

    root.mainloop()

if __name__ == "__main__":

    hub()