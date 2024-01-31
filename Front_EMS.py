from turtle import width
from six.moves import tkinter as tk
from tkinter import *
from productos import construir_producto
from tkinter import ttk
from datetime import datetime
import sys
from pathlib import Path
from productos import Producto



class UI(tk.Frame):

    def __init__(self, lista_productos, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()
        self.lista_productos = lista_productos
        self.actualizar_lista_periodicamente()
        
        

    def actualizar_lista_periodicamente(self):
        self.verificar_y_actualizar()
        self.parent.after(1000, self.actualizar_lista_periodicamente)
        

    def verificar_y_actualizar(self):
        nuevo_producto = construir_producto()
        self.lista_productos.append(nuevo_producto)


        

    def init_ui(self):

        """ funciones."""
    
        def funcion_guardar(event=None):
            if campo_de_texto_producto.get():
                primer_producto = self.lista_productos[0]
                item=tree.insert('', 'end', text="1", values=(primer_producto.producto_id, primer_producto.contenedor_id, primer_producto.pais, primer_producto.peso, primer_producto.peso_preaviso, primer_producto.estado, primer_producto.pais_destino, primer_producto.fecha))
                campo_de_texto_producto.delete(0,100)
                campo_de_texto_receptaculo.delete(0,100)
                campo_de_texto_pais.delete(0,100)
                campo_de_texto_peso.delete(0,100)
                self.lista_productos.pop(0)
                

        def funcion_insertar(event=None):
            if campo_de_texto_producto.get():
                return

            else:
                try:
                    primer_producto = self.lista_productos[0]
                    campo_de_texto_producto.insert(0,primer_producto.producto_id)
                    campo_de_texto_receptaculo.insert(0,primer_producto.contenedor_id)
                    campo_de_texto_pais.insert(0,primer_producto.pais)
                    campo_de_texto_peso.insert(0,primer_producto.peso)
                except IndexError:
                    print("Error: no hay nada en la lista")


        def funcion_enviar(event=None): #esta funcion se supone que envia los productos pero solo los borra realmente
            tree.delete(*tree.get_children())

            return

        def delete(event=None): #funcion para borrar solamente un producto
            selected_item = tree.selection()[0]
            tree.delete(selected_item)

        def set_cell_value(event): #funcion para editar productos
            for item in tree.selection():
                item_text = tree.item(item, "values")
                column = tree.identify_column(event.x)
                row = tree.identify_row(event.y)

            cn = int(str(column).replace('#', ''))
            rn = int(str(row).replace('I', ''))
            entryedit = tk.Entry (self.parent, width=50)
            entryedit.grid(pady=30, row=19, column=3, columnspan=2, sticky=S+N+W)
            
            def saveedit(): #funcion para guardar producto editado
                
                if entryedit.get():
                    tree.set(item, column=column, value=entryedit.get())
                    entryedit.destroy()
                    okb.destroy()
                    salir_boton.destroy()
                else:
                    entryedit.destroy()
                    okb.destroy()
                    salir_boton.destroy()

            def salir(): #funcion para salir de la edicion
                entryedit.destroy()
                okb.destroy()
                salir_boton.destroy()



            
            okb = ttk.Button(self.parent, text='OK', width=4, command=saveedit)
            okb.grid(pady=30, row=19, column=3, sticky="e")
            salir_boton = tk.Button(self.parent, text='Salir de editar', width=10, command=salir)
            salir_boton.grid(pady=30,row=19, column=2, columnspan=1,  sticky="w")
            entryedit.insert(0,tree.item(tree.selection())['values'][cn-1])


        """ widgets."""

        self.parent.title("Aperturacion")
        etiqueta_titulo= tk.Label(self.parent, text="Aperturacion", underline=8 ,padx=20, pady=10,)
        etiqueta_titulo.grid(row=1, column=1)
        


        etiqueta_producto= tk.Label(self.parent, text="Codigo de Envio: ")
        etiqueta_producto.grid(row=3, column=2, columnspan=2, sticky='w')
        campo_de_texto_producto= tk.Entry(self.parent, width=50)
        campo_de_texto_producto.grid(row=4, column=2,columnspan=2, sticky='w')
        campo_de_texto_producto.get()
        
        

        etiqueta_receptaculo= tk.Label(self.parent, text="ID Envase: ")
        etiqueta_receptaculo.grid(row=5, column=2,columnspan=2, sticky='w')
        campo_de_texto_receptaculo= tk.Entry(self.parent, width=50)
        campo_de_texto_receptaculo.grid(row=6, column=2,columnspan=2, sticky='w')
        campo_de_texto_receptaculo.get()
        
        

        etiqueta_pais= tk.Label(self.parent, text="País de origen:")
        etiqueta_pais.grid(row=7, column=2,columnspan=2, sticky='w')
        campo_de_texto_pais= tk.Entry(self.parent, width=50)
        campo_de_texto_pais.grid(row=8, column=2,columnspan=2 , sticky='w')
        campo_de_texto_pais.get()
        
        

        etiqueta_peso= tk.Label(self.parent, text="Peso (Kg):")
        etiqueta_peso.grid( row=9, column=2,columnspan=2, sticky='w')
        campo_de_texto_peso= tk.Entry(self.parent, width=50)
        campo_de_texto_peso.grid(row=10, column=2,columnspan=2, sticky='w')
        campo_de_texto_peso.get()
        
        
        
        """botones"""

        boton_insert = tk.Button(self.parent, text="insertar", command=funcion_insertar,  width=15).grid(pady=20, row=1, column=3 , sticky='e')
        boton_guardar= tk.Button(self.parent, text="guardar", command=funcion_guardar, width=10).grid(padx=10, pady=10, row=11, column=2,columnspan=2, sticky='w')
        boton_enviar= tk.Button(self.parent, text="Enviar!", command=funcion_enviar , width=10).grid(pady=20, row=14, column=3 , sticky='e')
        boton_delete= tk.Button(self.parent, text="Borrar seleccion", command=delete , width=15).grid(padx=0, pady=10, row=14, column=2,columnspan=2, sticky='w')
        

        """Bind de teclas"""
        self.parent.bind("<Left>",funcion_insertar)
        self.parent.bind("<Right>",funcion_guardar)
        self.parent.bind("<Up>",funcion_enviar)
        
        """listas desplegables"""
        etiqueta_destino_producto= tk.Label(self.parent, text="Status:").grid(row=3, column=3,columnspan=2, sticky='w')
        lista_destino_producto = ttk.Combobox(
            self.parent,
            state="readonly",
            values=["MINL Normal", "MIMS Mal encaminado", "MIAT En Transito", "MIRD Retornado/Reencaminado en Transito", "MIRT Retornado"],
            width=50
        )
        lista_destino_producto.grid(row=4, column=3,columnspan=3, sticky='w')
        lista_destino_producto.set("MINL Normal")

        etiqueta_condicion_producto= tk.Label(self.parent, text="Condicion del producto:").grid(row=5, column=3,columnspan=2, sticky='w')
        lista_condicion_producto = ttk.Combobox(
            self.parent,
            state="readonly",
            values=["30 Envio Recibido en Buena Condicion", "31 Envio Dañado o Roto", "32 Envio Violado"],
            width=50
        )
        lista_condicion_producto.grid(row=6, column=3,columnspan=3, sticky='w')
        lista_condicion_producto.set("30 Envio Recibido en Buena Condicion")



        """etiquetas"""
        
        etiqueta_envio= tk.Label(self.parent, text="Tipo de Envio:").grid(row=7, column=3, sticky='w')
        etiqueta_envio_respuesta= tk.Label(self.parent, text="EMS",fg='#003').grid(padx=10,row=8, column=3,columnspan=2, sticky='w')

        etiqueta_oficina= tk.Label(self.parent, text="Oficina:").grid(row=9, column=3, sticky="w")
        etiqueta_oficina_respuesta= tk.Label(self.parent, text="CLSCLD", fg='#003').grid(padx=10,row=10, column=3, sticky='w')



        """not tocar es estructural"""
        etiqueta_tree= Label(self.parent, text="Lista de productos").grid(row=12, column=2)
        "__________"



        """triewview (cuadrado donde se depliegan los productos)"""

        tree = ttk.Treeview(self.parent, column=("c1", "c2", "c3","c4","c5","c6","c7","c8"), show='headings', height=6)
        s = ttk.Style()
        s.theme_use('clam')

        
        tree.column("# 1", anchor=CENTER, minwidth=0, width=100, stretch=NO)
        tree.heading("# 1", text="ID producto")
        tree.column("# 2", anchor=CENTER, minwidth=0, width=160, stretch=TRUE)
        tree.heading("# 2", text="Codigo de Envio")
        tree.column("# 3", anchor=CENTER, minwidth=0, width=0, stretch=NO)
        tree.heading("# 3", text="Pais de Origen")
        tree.column("# 4", anchor=CENTER, minwidth=0, width=70, stretch=NO)
        tree.heading("# 4", text="Peso (kg.)")
        tree.column("# 5", anchor=CENTER, minwidth=0, width=90, stretch=YES)
        tree.heading("# 5", text="Peso con Preaviso (kg.)")
        tree.column("# 6", anchor=CENTER, minwidth=0, width=90, stretch=NO)
        tree.heading("# 6", text="Estado")
        tree.column("# 7", anchor=CENTER, minwidth=0, width=90, stretch=NO)
        tree.heading("# 7", text="Pais de Destino")
        tree.column("# 8", anchor=CENTER, minwidth=0, width=90, stretch=NO)
        tree.heading("# 8", text="Fecha")

        tree.grid( pady=10 ,row=12, column=2,columnspan=2, sticky='w')

        tree.bind('<Double-1>', set_cell_value)
        vsb = ttk.Scrollbar(self.parent, orient="vertical", command=tree.yview)
        vsb.place(x=805, y=290, height=149)
        tree.configure(yscrollcommand=vsb.set)
        

        etiqueta_edit= Label(self.parent, text="Consejo:  para editar, seleccione el elemento que desea cambiar y haga doble clic en él.",padx=0, pady=0)
        etiqueta_edit.grid(row=17, column=2, columnspan=3)
        etiqueta_edit.config(fg="grey")


        Usuario = "Usuario.apellido/(Normal)"
        Grupo = 'CORREOINTERNO/'
        fecha_usuario=datetime.now()

        sbar = Label(self.parent, text='CLSCL              |              '+str(Grupo)+"NOT-860195-055              |              "+str(Grupo)+str(Usuario)+"              |              "+str(fecha_usuario),relief=SUNKEN, anchor="w")
        sbar.place(x=0, y=630, height=20, width=950)
        

def iniciar_ventana():
        dt = datetime.now()
        producto1 = Producto("CH199487439US", "USJFKACLSCLEACN30467007900083", "US (United States of America (the))", "10","12","aperturado","CL (Chile)",dt)
        producto2 = Producto("CH198402940US", "USLAXACLSCLEACN30593005900046", "US (United States of America (the))", "15","12","aperturado","Cl (Chile)",dt)
        producto3 = Producto("CH198884460US", "USLAXACLSCLEACN30626002900063", "US (United States of America (the))", "8","12","aperturado","CL (Chile)",dt)
        producto4 = Producto("CP435601315DE", "DEFRAACLSCLGBCN31094003000149", "DE (Germany)", "20", "12", "aperturado", "CL (Chile)", dt)
        producto5 = Producto("CY138411900US", "USORDACLSCLEACN30546005900113", "US (United States of America (the))", "12", "12", "aperturado", "CL (Chile)", dt)
        producto6 = Producto("CJ499175876US", "USLAXACLSCLEACN30593002900034", "US (United States of America (the))", "18", "12", "aperturado", "CL (Chile)", dt)
        producto7 = Producto("CH198767327US", "USLAXACLSCLEACN30626003900101", "US (United States of America (the))", "14", "12", "aperturado", "CL (Chile)", dt)
        producto8 = Producto("CS235292097DE", "DEFRAACLSCLGBCN31113005000023", "DE (Germany)", "16", "12", "aperturado", "CL (Chile)", dt)
        producto9 = Producto("CC021361557ES", "ESMADCCLSCLGBCN30346012010150", "ES (Spain)", "9", "12", "aperturado", "CL (Chile)", dt)
        producto21 = Producto("FR123456789FR", "FRPARACLSCLEACN30467007900083", "FR (France)", "10", "12", "aperturado", "CL (Chile)", dt)
        producto22 = Producto("AU987654321AU", "AUSYDACLSMELACN30593005900046", "AU (Australia)", "15", "12", "aperturado", "CL (Chile)", dt)
        producto23 = Producto("IT456789012IT", "ITROMACLSCLEACN30626002900063", "IT (Italy)", "8", "12", "aperturado", "CL (Chile)", dt)
        producto24 = Producto("JP654321987JP", "JPTKOAACLSTKOACN31094003000149", "JP (Japan)", "20", "12", "aperturado", "CL (Chile)", dt)
        producto25 = Producto("UK321987654UK", "UKLONACLSCLEACN30546005900113", "UK (United Kingdom)", "12", "12", "aperturado", "CL (Chile)", dt)
        producto26 = Producto("BR789012345BR", "BRGRUAACLSGRUACN30593002900034", "BR (Brazil)", "18", "12", "aperturado", "CL (Chile)", dt)
        producto27 = Producto("MX987654321MX", "MXMEXACLSCLEACN30626003900101", "MX (Mexico)", "14", "12", "aperturado", "CL (Chile)", dt)
        producto28 = Producto("CA123456789CA", "CATORACLSCLEACN31113005000023", "CA (Canada)", "16", "12", "aperturado", "CL (Chile)", dt)
        producto29 = Producto("RU789012345RU", "RUMOSACLSCLEACN30346012010150", "RU (Russia)", "9", "12", "aperturado", "CL (Chile)", dt)
        producto30 = Producto("IN987654321IN", "INBOMACLSCLEACN30467003900112", "IN (India)", "22", "12", "aperturado", "CL (Chile)", dt)
        producto31 = Producto("SA789012345SA", "SARUHACLSCLEACN30563005000095", "SA (Saudi Arabia)", "24", "12", "aperturado", "CL (Chile)", dt)
        producto32 = Producto("KR987654321KR", "KRSELACLSCLEACN30546002900155", "KR (South Korea)", "26", "12", "aperturado", "CL (Chile)", dt)
        producto33 = Producto("AR789012345AR", "ARBUEACLSCLEACN30593003900036", "AR (Argentina)", "28", "12", "aperturado", "CL (Chile)", dt)
        producto34 = Producto("EG987654321EG", "EGCAIAACLSLXN30546001010123", "EG (Egypt)", "30", "12", "aperturado", "CL (Chile)", dt)
        producto35 = Producto("NG789012345NG", "NGLOSAACLSCLEACN31094003000011", "NG (Nigeria)", "32", "12", "aperturado", "CL (Chile)", dt)
        producto36 = Producto("ZA987654321ZA", "ZACPTACLSCLEACN30467001900173", "ZA (South Africa)", "34", "12", "aperturado", "CL (Chile)", dt)
        producto37 = Producto("ID789012345ID", "IDJKTACLSCLEACN30626002900122", "ID (Indonesia)", "36", "12", "aperturado", "CL (Chile)", dt)
        producto38 = Producto("TH987654321TH", "THBKKACLSCLEACN30563005000136", "TH (Thailand)", "38", "12", "aperturado", "CL (Chile)", dt)
        producto39 = Producto("PH789012345PH", "PHMNLACLSCLEACN30546005900164", "PH (Philippines)", "40", "12", "aperturado", "CL (Chile)", dt)
        producto40 = Producto("MY987654321MY", "MYKULACLSCLEACN30346012010011", "MY (Malaysia)", "42", "12", "aperturado", "CL (Chile)", dt)

        lista_productos = [producto1, producto2, producto3, producto4, producto5, producto6, producto7, producto8, producto9,producto21,producto22,producto23,producto24,producto25,producto26,producto27,producto28,producto29,producto30,producto31,producto32,producto33,producto34,producto35,producto36,producto37,producto38,producto39,producto40]
        def cerrar_ventana():
            sys.exit()    
            ROOT.destroy()

        ROOT = tk.Tk()
        ROOT.geometry("950x650")
        ROOT.protocol("WM_DELETE_WINDOW", cerrar_ventana)
        ROOT.resizable(0,0)
        APP = UI(lista_productos,parent=ROOT)

        APP.mainloop()
        ROOT.destroy()



    
if __name__ == "__main__":
    iniciar_ventana()
        