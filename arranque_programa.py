import tkinter as tk
from Hub_EMS import hub
from tkinter import ttk
from Hub_CP import hub_cp

def main():

    def abrir_hub_EMS():
        root2.destroy()
        hub()

    def abrir_hub_cp():
        root2.destroy()
        hub_cp()

    def abrir():
        oficina_seleccionada = lista_oficina.get()
        print(oficina_seleccionada)
        if oficina_seleccionada=="CLSCLD (SANTIAGO EMS)":
            abrir_hub_EMS()
        if oficina_seleccionada=="CLSCLE (SANTIAGO OCPI CP)":
            abrir_hub_cp()



    root2 = tk.Tk()
    root2.geometry("370x200")
   



    """widgets"""

    tk.Frame.etiqueta_origen= tk.Label (root2, text="Origen de datos: ").grid(padx=10,pady=10,row=0,column=0, sticky="w")
    lista_origen = ttk.Combobox(
            root2,
            state="disable",
            values=["IPSb4"],
            width=30
        )
    lista_origen.grid(padx=0,pady=10,row=0, column=1, sticky='w')
    lista_origen.set("IPSb4")

    tk.Frame.etiqueta_oficina = tk.Label (root2, text="Oficina: ").grid(padx=10,pady=0,row=2,column=0,sticky="w")
    lista_oficina = ttk.Combobox(
            root2,
            state="readonly",
            values=["CLSCLD (SANTIAGO EMS)","CLSCLE (SANTIAGO OCPI CP)"],
            width=30
        )
    lista_oficina.grid(padx=0,pady=10,row=2, column=1, sticky='w')
    lista_oficina.set("CLSCLD (SANTIAGO EMS)")

    
    tk.Frame.etiqueta_Operador = tk.Label (root2, text="Operador: ").grid(padx=10,pady=0,row=3,column=0,sticky="w")
    lista_Operador = ttk.Combobox(
            root2,
            state="disable",
            values=["CLA (Empresas Correos de Chile)"],
            width=30
        )
    
    lista_Operador.grid(padx=0,pady=0,row=3, column=1, sticky='w')
    lista_Operador.set("CLA (Empresas Correos de Chile)")

    tk.Frame.etiqueta_cat = tk.Label (root2, text="Cate. de correo predet. ").grid(padx=10,pady=0,row=4,column=0,sticky="w")
    lista_cat = ttk.Combobox(
            root2,
            state="disable",
            values=["A(CORREO AERO/PRIORITARIO)"],
            width=30
        )
    lista_cat.grid(padx=0,pady=10,row=4, column=1, sticky='w')
    lista_cat.set("A(CORREO AERO/PRIORITARIO)")


    tk.Frame.boton_abrir = ttk.Button(root2, text="aceptar", command=abrir, width=10)
    tk.Frame.boton_abrir.grid(padx=0,pady=20,row=5,column=1,sticky="w")




    """ ____"""


    style = ttk.Style()
    style.theme_use("xpnative")
    root2.mainloop()

if __name__ == "__main__":

    main()