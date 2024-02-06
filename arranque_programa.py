import tkinter as tk
from Hub_EMS import hub_ems
from tkinter import ttk
from Hub_CP import hub_cp
from tkinter import *

def main():
    
# ____Funciones: 


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
    firstROOT = tk.Tk()

    # datos para las dimesiones
    w = 370
    h = 200
    ws = firstROOT.winfo_screenwidth()
    hs = firstROOT.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)


    # geometria de la ventana
    firstROOT.geometry('%dx%d+%d+%d' % (w, h, x, y))



#____ widgets: listas

    #primera lista
    tk.Frame.etiqueta_origen= tk.Label (firstROOT, text="Origen de datos: ").grid(padx=10,pady=10,row=0,column=0, sticky="w")
    lista_origen = ttk.Combobox(
            firstROOT,
            state="disable",
            values=["IPSb4"],
            width=30
        )
    lista_origen.grid(padx=0,pady=10,row=0, column=1, sticky='w')
    lista_origen.set("IPSb4")


    #segunda lista
    tk.Frame.etiqueta_oficina = tk.Label (firstROOT, text="Oficina: ").grid(padx=10,pady=0,row=2,column=0,sticky="w")
    lista_oficina = ttk.Combobox(
            firstROOT,
            state="readonly",
            values=["CLSCLD (SANTIAGO EMS)","CLSCLE (SANTIAGO OCPI CP)"],
            width=30
        )
    lista_oficina.grid(padx=0,pady=10,row=2, column=1, sticky='w')
    lista_oficina.set("CLSCLD (SANTIAGO EMS)")


    #tercera lista
    tk.Frame.etiqueta_Operador = tk.Label (firstROOT, text="Operador: ").grid(padx=10,pady=0,row=3,column=0,sticky="w")
    lista_Operador = ttk.Combobox(
            firstROOT,
            state="disable",
            values=["CLA (Empresas Correos de Chile)"],
            width=30
        )
    
    lista_Operador.grid(padx=0,pady=0,row=3, column=1, sticky='w')
    lista_Operador.set("CLA (Empresas Correos de Chile)")
    
    
    #cuarta lista
    tk.Frame.etiqueta_cat = tk.Label (firstROOT, text="Cate. de correo predet. ").grid(padx=10,pady=0,row=4,column=0,sticky="w")
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


# widget: estilo ____

    style = ttk.Style()
    style.theme_use("vista")
    
# desplegar ventana .
    firstROOT.mainloop()

if __name__ == "__main__":

    main()