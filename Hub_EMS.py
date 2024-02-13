from Front_EMS import iniciar_ventana
from Front_Lotes import main_lotes
from tkinter import ttk
import tkinter as tk
from tkinter import *
import sys


def hub_ems(firstROOT):

# ____Funciones: 
    def cerrar_ventana():
            sys.exit()    
            ROOT_CP.destroy()

    def abrir_front():
        ems_HubROOT.withdraw()
        iniciar_ventana(ems_HubROOT)
        
    def salir():
        sys.exit() 
        firstROOT.destroy()
        
    def volver():
        style.theme_use("clam")
        firstROOT.deiconify() 
        ems_HubROOT.destroy()
        
    def abrir_lotes():
        ems_HubROOT.withdraw()
        main_lotes(ems_HubROOT)


        
# ____ Iniciar la ventana: 


    # llamar ventana hija de la ventana de arranque
    ems_HubROOT = Toplevel()
    ems_HubROOT.title("Nuevo IPS")
    
    # datos para las dimesiones
    w = 500
    h = 515 
    ws = ems_HubROOT.winfo_screenwidth()
    hs = ems_HubROOT.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)


    # geometria de la ventana y funciones
    ems_HubROOT.geometry('%dx%d+%d+%d' % (w, h, x, y))
    ems_HubROOT.protocol("WM_DELETE_WINDOW", cerrar_ventana)
    ems_HubROOT.resizable(0,0)


# ____ Fijar estilo:


    style = ttk.Style()
    style.theme_use("clam")



# ____ Manejo de viñetas:
    
    
    #definir las tabs de la ventana
    tabControl = ttk.Notebook(ems_HubROOT)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    
    
    #abrir y modificar imagenes que van en las viñetas
    ems_logo = tk.PhotoImage(file="icons/Ems-Logo.png")
    ems_logo = ems_logo.subsample(26)
    packagelogo= tk.PhotoImage(file="icons/packages.png")
    packagelogo= packagelogo.subsample(16)

    #colcar el texto y la imagen sobre la viñeta. luego desplegar
    tabControl.add(tab1, image=ems_logo, compound='right') 
    tabControl.add(tab2, text ='Encomiendas (CP)',image=packagelogo, state="disable",compound='left') 
    tabControl.grid(row=0,column=0)


# ____ widget: TREEVIEW


    #definir el treeview 
    treeview = ttk.Treeview(tab1,show="tree", height=20, columns=("#0"))
    
    
    #fijar solamente una columna. esto permite modificar el ancho del treeview, dentro de la columna no hay nada realmente.
    treeview.column("#0", anchor="w", minwidth=360, width=242, stretch=YES)


    #abrir y modificar iconos que se despliegan en el treeview
    mouse_pointer = tk.PhotoImage(file="icons/mouse-pointer-square.png")
    mouse_pointer = mouse_pointer.subsample(2)
   
   
    #arbol de items que se desplegaran en el treeview
    item1 = treeview.insert("", tk.END,'item1',text="  Recibe envios EMS de oficina de Cambio CC y Aduana", image=mouse_pointer)
    item2 = treeview.insert("", tk.END,text="  Registra  Informacion de Entrega de Oficina Central", image=mouse_pointer)
    item3 = treeview.insert("", tk.END,text="  Enviar Envios desde Oficina de Cambio Con Manifiesto", image=mouse_pointer)
    item4 = treeview.insert("", tk.END,text="  Registrar Informacion del Destinatario", image=mouse_pointer)
    

    #seleccionar por default el iten recibe 'Recibe envios EMS de oficina de Cambio CC y Aduana'
    treeview.selection_toggle(item1)
    
   #Posicionar el treeview en la ventana
    treeview.grid(row=0, column=0,padx=25,pady=10,columnspan=10)



# ____ widget: funcion que permite desactivar el boton de abrir si no esta en el item seleccionado correcto (item_recibe)
    
    
    def on_select(event):
        selected_item = treeview.selection()
        if 'item1' in selected_item:
            tk.Frame.boton_abrir.config(state=tk.NORMAL)
        else:
            tk.Frame.boton_abrir.config(state=tk.DISABLED)
    treeview.bind("<<TreeviewSelect>>", on_select)



# ____ widget: botones
    
    tk.Frame.boton_abrir = ttk.Button(tab1, text="Ejecutar", command=abrir_front)
    tk.Frame.boton_abrir.grid(row=5,column=0,pady=5, ipadx=5)
    tk.Frame.boton_salir = ttk.Button(tab1, text="Salir", command=salir)
    tk.Frame.boton_salir.place(x=395,y=425 )
    tk.Frame.boton_atras = ttk.Button(tab1, text="Volver", command=volver)
    tk.Frame.boton_atras.place(x=315,y=425)
    tk.Frame.boton_desp = ttk.Button(ems_HubROOT, text="Lotes en espera", command=abrir_lotes, width= 18)
    tk.Frame.boton_desp.place(x=340,y=8)
    
    
#  desplegar ventana .
    ems_HubROOT.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    hub_ems(root)