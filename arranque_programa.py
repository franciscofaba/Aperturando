import tkinter as tk
from Hub_EMS import hub_ems
from tkinter import ttk
from Hub_CP import hub_cp
from tkinter import *
import sys
from ttkthemes import ThemedTk


def main():
    
# ____Funciones: 
    def cerrar_ventana():
        sys.exit()    
        ROOT_CP.destroy()

    def abrir_hub_EMS():
        firstROOT.withdraw()
        hub_ems(firstROOT)

    def abrir_hub_cp():
        firstROOT.withdraw()
        hub_cp(firstROOT)

    def abrir():
        oficina_seleccionada = lista_oficina.get()
        print(oficina_seleccionada)
        if oficina_seleccionada=="CLSCLD (SANTIAGO EMS)":
            abrir_hub_EMS()
        if oficina_seleccionada=="CLSCLE (SANTIAGO OCPI CP)":
            abrir_hub_cp()

    

# ____ Iniciar la ventana: 


    # llamar ventana
    
    firstROOT = ThemedTk(theme="arc")
    firstROOT.set_theme_advanced("arc", brightness=1.0, saturation=2.0, hue=1.0, preserve_transparency=False, output_dir=None)
    firstROOT.title("Nuevo IPS")
    style = ttk.Style()
    # datos para las dimesiones
    w = 370
    h = 225
    ws = firstROOT.winfo_screenwidth()
    hs = firstROOT.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)


    # geometria de la ventana y funciones
    firstROOT.geometry('%dx%d+%d+%d' % (w, h, x, y))
    firstROOT.protocol("WM_DELETE_WINDOW", cerrar_ventana)
    firstROOT.resizable(0,0)


#____ widgets: listas

    #primera lista
    tk.Frame.etiqueta_origen= ttk.Label (firstROOT, text="Origen de datos: ").grid(padx=10,pady=10,row=0,column=0, sticky="w")
    lista_origen = ttk.Combobox(
            firstROOT,
            state="disable",
            values=["IPSb4"],
            width=30
        )
    lista_origen.grid(padx=0,pady=10,row=0, column=1, sticky='w')
    lista_origen.set("IPSb4")


    #segunda lista
    tk.Frame.etiqueta_oficina = ttk.Label (firstROOT, text="Oficina: ", foreground="black").grid(padx=10,pady=0,row=2,column=0,sticky="w")
    lista_oficina = ttk.Combobox(
            firstROOT,
            state="readonly",
            values=["CLSCLD (SANTIAGO EMS)","CLSCLE (SANTIAGO OCPI CP)"],
            width=30, 
            foreground="black"
        )
    lista_oficina.grid(padx=0,pady=10,row=2, column=1, sticky='w')
    lista_oficina.set("CLSCLD (SANTIAGO EMS)")


    #tercera lista
    tk.Frame.etiqueta_Operador = ttk.Label (firstROOT, text="Operador: ").grid(padx=10,pady=0,row=3,column=0,sticky="w")
    lista_Operador = ttk.Combobox(
            firstROOT,
            state="disable",
            values=["CLA (Empresas Correos de Chile)"],
            width=30
        )
    
    lista_Operador.grid(padx=0,pady=0,row=3, column=1, sticky='w')
    lista_Operador.set("CLA (Empresas Correos de Chile)")
    
    
    #cuarta lista
    tk.Frame.etiqueta_cat = ttk.Label (firstROOT, text="Cate. de correo predet. ").grid(padx=10,pady=0,row=4,column=0,sticky="w")
    lista_cat = ttk.Combobox(
            firstROOT,
            state="disable",
            values=["A(CORREO AERO/PRIORITARIO)"],
            width=30
        )
    lista_cat.grid(padx=0,pady=10,row=4, column=1, sticky='w')
    lista_cat.set("A(CORREO AERO/PRIORITARIO)")



# widgets: botones ____

    tk.Frame.boton_abrir = ttk.Button(firstROOT, text="aceptar", command=abrir, width=10)
    tk.Frame.boton_abrir.grid(padx=0,pady=20,row=5,column=1,sticky="w")
    style.configure('TButton', font=('American typewriter', 10), foreground='black')

# widget: estilo ____

    
    

# desplegar ventana .
    
    firstROOT.mainloop()


main()