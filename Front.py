
from turtle import width
from six.moves import tkinter as tk
from tkinter import *
from productos import construir_producto
from tkinter import ttk
import sys
from datetime import datetime
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
    
        def funcion_guardar():
            primer_producto = self.lista_productos[0]
            item=tree.insert('', 'end', text="1", values=(primer_producto.producto_id, primer_producto.contenedor_id, primer_producto.pais, primer_producto.peso, primer_producto.peso_preaviso, primer_producto.estado, primer_producto.pais_destino, primer_producto.fecha))
            campo_de_texto_producto.delete(0,10)
            campo_de_texto_receptaculo.delete(0,10)
            campo_de_texto_pais.delete(0,10)
            campo_de_texto_peso.delete(0,10)
            self.lista_productos.pop(0)
            
            return(item)
        def funcion_insertar():
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


        def funcion_enviar():
            tree.delete(*tree.get_children())

            return

        def delete():
            # Get selected item to Delete
            selected_item = tree.selection()[0]
            tree.delete(selected_item)

        def set_cell_value(event):
            for item in tree.selection():
                item_text = tree.item(item, "values")
                column = tree.identify_column(event.x)
                row = tree.identify_row(event.y)
            cn = int(str(column).replace('#', ''))
            rn = int(str(row).replace('I', ''))
            entryedit = tk.Entry (self.parent, width=30)
            entryedit.grid( row=18, column=2,columnspan=1, sticky="w")
            

            def saveedit():
                print(entryedit.get())
                if entryedit.get():
                    tree.set(item, column=column, value=entryedit.get())
                    entryedit.destroy()
                    okb.destroy()
                    salir_boton.destroy()
                    etiqueta_edit.destroy()
                else:
                    entryedit.destroy()
                    okb.destroy()
                    salir_boton.destroy()
                    etiqueta_edit.destroy()
            def salir():
                entryedit.destroy()
                okb.destroy()
                salir_boton.destroy()
                etiqueta_edit.destroy()


            global etiqueta_edit
            etiqueta_edit= Label(self.parent, text="Editar:",padx=0, pady=10,)
            etiqueta_edit.grid(row=17, column=1)
            okb = ttk.Button(self.parent, text='OK', width=4, command=saveedit)
            okb.grid( row=18, column=2,)
            salir_boton = tk.Button(self.parent, text='Salir de editar', width=10, command=salir)
            salir_boton.grid(row=18, column=1, columnspan=1,  sticky="e")


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
        
        
        

        boton_insert = tk.Button(self.parent, text="insertar", command=funcion_insertar,  width=15).grid(pady=20, row=1, column=3 , sticky='e')
        boton_guardar= tk.Button(self.parent, text="guardar", command=funcion_guardar, width=10).grid(padx=10, pady=10, row=11, column=2,columnspan=2, sticky='w')
        boton_enviar= tk.Button(self.parent, text="Enviar!", command=funcion_enviar , width=10).grid(padx=10, pady=10, row=14, column=2,columnspan=2)
        boton_delete= tk.Button(self.parent, text="Borrar seleccion", command=delete , width=15).grid(padx=100, pady=10, row=14, column=1,columnspan=2, sticky='w')
        

        etiqueta_destino_producto= tk.Label(self.parent, text="Status:").grid(row=3, column=3,columnspan=2, sticky='w')
        lista_destino_producto = ttk.Combobox(
            state="readonly",
            values=["MINL Normal", "MIMS Mal encaminado", "MIAT En Transito", "MIRD Retornado/Reencaminado en Transito", "MIRT Retornado"],
            width=50
        )
        lista_destino_producto.grid(row=4, column=3,columnspan=3, sticky='w')
        lista_destino_producto.set("MINL Normal")


        etiqueta_condicion_producto= tk.Label(self.parent, text="Condicion del producto:").grid(row=5, column=3,columnspan=2, sticky='w')
        lista_condicion_producto = ttk.Combobox(
            state="readonly",
            values=["30 Envio Recibido en Buena Condicion", "31 Envio Dañado o Roto", "32 Envio Violado"],
            width=50
        )
        lista_condicion_producto.grid(row=6, column=3,columnspan=3, sticky='w')
        lista_condicion_producto.set("30 Envio Recibido en Buena Condicion")


        
        etiqueta_tree= Label(self.parent, text="Lista de productos").grid(row=12, column=2)
        tree = ttk.Treeview(self.parent, column=("c1", "c2", "c3","c4","c5","c6","c7","c8"), show='headings', height=6)
        s = ttk.Style()
        s.theme_use('clam')

        tree.column("# 1", anchor=CENTER, minwidth=0, width=100, stretch=NO)
        tree.heading("# 1", text="ID producto")
        tree.column("# 2", anchor=CENTER, minwidth=0, width=100, stretch=NO)
        tree.heading("# 2", text="Codigo de Envio")
        tree.column("# 3", anchor=CENTER, minwidth=0, width=100, stretch=NO)
        tree.heading("# 3", text="Pais de Origen")
        tree.column("# 4", anchor=CENTER, minwidth=0, width=100, stretch=NO)
        tree.heading("# 4", text="Peso (kg.)")
        tree.column("# 5", anchor=CENTER, minwidth=0, width=100, stretch=NO)
        tree.heading("# 5", text="Peso con Preaviso (kg.)")
        tree.column("# 6", anchor=CENTER, minwidth=0, width=100, stretch=NO)
        tree.heading("# 6", text="Estado")
        tree.column("# 7", anchor=CENTER, minwidth=0, width=100, stretch=NO)
        tree.heading("# 7", text="Pais de Destino")
        tree.column("# 8", anchor=CENTER, minwidth=0, width=100, stretch=NO)
        tree.heading("# 8", text="Fecha")

        tree.grid( pady=10 ,row=12, column=2,columnspan=2, sticky='w')

        tree.bind('<Double-1>', set_cell_value)
        

if __name__ == "__main__":



    dt = datetime.now()
    producto1 = Producto("1", "A1", "USA", "10","12","aperturado","Chile",dt)
    producto2 = Producto("2", "B1", "Canada", "15","12","aperturado","Chile",dt)
    producto3 = Producto("3", "C1", "Mexico", "8","12","aperturado","Chile",dt)

    lista_productos = [producto1,producto2,producto3]




    def cerrar_ventana():
        sys.exit()    
        ROOT.destroy()

    ROOT = tk.Tk()
    ROOT.geometry("1000x600")
    ROOT.protocol("WM_DELETE_WINDOW", cerrar_ventana)
    APP = UI(lista_productos,parent=ROOT)
    APP.pack()
    APP.mainloop()
    ROOT.destroy()


