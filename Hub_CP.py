from Front_CP import iniciar_ventana_cp
from Front_Lotes import main_lotes
from tkinter import ttk
import tkinter as tk
from tkinter import *
import sys
from ttkthemes import ThemedTk


def hub_cp(firstROOT):
    
# ____Funciones: 
    def cerrar_ventana():
            sys.exit()    
            ROOT_CP.destroy()
    def abrir_front():
        cp_HubROOT.withdraw()
        iniciar_ventana_cp(cp_HubROOT)
        
    def salir():
        sys.exit() 
        firstROOT.destroy()

    def volver():
        
        firstROOT.deiconify() 
        cp_HubROOT.destroy()
        
    def abrir_lotes():
        cp_HubROOT.withdraw()
        main_lotes(cp_HubROOT)

        
# ____ Iniciar la ventana: 

    # llamar ventana hija de la ventana de arranque
    cp_HubROOT = Toplevel()
    cp_HubROOT.title("Nuevo IPS")
    
    # datos para las dimesiones
    w = 525
    h = 545 
    ws = cp_HubROOT.winfo_screenwidth()
    hs = cp_HubROOT.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)


    # geometria de la ventana y funciones
    cp_HubROOT.geometry('%dx%d+%d+%d' % (w, h, x, y))
    cp_HubROOT.protocol("WM_DELETE_WINDOW", cerrar_ventana)
    cp_HubROOT.resizable(0,0)




# ____ Fijar estilo:
    style = ttk.Style()
    style.configure('TButton', font=('American typewriter', 10), foreground='black')
    style.configure('TLabel', font=('calibri', 10, 'bold'), foreground='black')




# ____ Manejo de viñetas:
    
    #definir las tabs de la ventana
    tabControl = ttk.Notebook(cp_HubROOT, style='TNotebook', padding=5)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    
    style.configure('TNotebook.Tab', foreground='black')
    #abrir y modificar imagenes que van en las viñetas
    ems_logo = tk.PhotoImage(file="icons/Ems-Logo-old.png")
    ems_logo = ems_logo.subsample(28)
    packagelogo= tk.PhotoImage(file="icons/packages.png")
    packagelogo= packagelogo.subsample(16)

    
    #colcar el texto y la imagen sobre la viñeta. luego desplegar
    tabControl.add(tab2, text ='Encomiendas (CP)',image=packagelogo,compound='left') 
    tabControl.add(tab1, image=ems_logo, state="disable", compound='right') 
    
    tabControl.grid(row=0,column=0)



# ____ widget: TREEVIEW

    #definir el treeview 
    treeview = ttk.Treeview(tab2,show="tree",columns=("#0"), height=20)

    #fijar solamente una columna. esto permite modificar el ancho del treeview, dentro de la columna no hay nada realmente.
    treeview.column("#0", anchor="w", minwidth=380, width=230, stretch=YES)


    #abrir y modificar iconos que se despliegan en el treeview
    folder_image_open = tk.PhotoImage(file="icons/folder-open.png")
    folder_image_open = folder_image_open.subsample(2)
    folder_image = tk.PhotoImage(file="icons/folder.png")
    folder_image = folder_image.subsample(2)
    mouse_pointer = tk.PhotoImage(file="icons/mouse-pointer-square.png")
    mouse_pointer = mouse_pointer.subsample(2)


    #arbol de items que se desplegaran en el treeview
    item_salida = treeview.insert("", tk.END,text="   Salida:", open=TRUE,image=folder_image_open)
    item_encomienda = treeview.insert(item_salida, tk.END, text="   Encomiendas", open=TRUE,image=folder_image)
    item_despachos = treeview.insert(item_salida, tk.END, text="   Despachos:", open=TRUE,image=folder_image)
    item_llegada=treeview.insert("", tk.END,text="   LLegada:", open=TRUE,image=folder_image_open)
    item_encomiendas = treeview.insert(item_llegada, tk.END, text="   Encomiendas", open=TRUE,image=folder_image_open)
    item_recibe = treeview.insert(item_encomiendas, tk.END,'item1',text="  Recibe Encomiendas en oficina de Cambio CC y Aduana", image=mouse_pointer)
    item_enviar = treeview.insert(item_encomiendas, tk.END,text="  Enviar Envios desde Oficina de Cambio Con Manifiesto", image=mouse_pointer)

    
    #seleccionar por default el iten recibe 'encomiendas en oficinas de cambio cc y aduana'
    treeview.selection_toggle(item_recibe)
    
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

    tk.Frame.boton_atras = ttk.Button(cp_HubROOT, text="Lotes en espera", command=abrir_lotes, width= 18)
    tk.Frame.boton_atras.place(x=340,y=8)
    tk.Frame.boton_abrir = ttk.Button(tab2, text="Ejecutar", command=abrir_front)
    tk.Frame.boton_abrir.grid(row=5,column=0,pady=5, ipadx=5)
    tk.Frame.boton_salir = ttk.Button(tab2, text="Salir", command=salir)
    tk.Frame.boton_salir.place(x=405,y=453 )
    tk.Frame.boton_ayuda = ttk.Button(tab2, text="Volver", command=volver)
    tk.Frame.boton_ayuda.place(x=310,y=453)



#  desplegar ventana .
    cp_HubROOT.mainloop()



if __name__ == "__main__":
    root = ThemedTk(theme='arc')
    root.set_theme_advanced('arc', brightness=1.0, saturation=2.0, hue=1.0, preserve_transparency=False, output_dir=None)
    
    root.withdraw()
    hub_cp(root)
