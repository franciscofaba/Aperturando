
from six.moves import tkinter as tk
from tkinter import *
from productos import construir_producto



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
            texto= f'  ID Producto: {primer_producto.producto_id}  |  ID Envase: {primer_producto.contenedor_id}  |  País: {primer_producto.pais}  |  Peso: {primer_producto.peso}'
            listbox.insert(0,texto )
            campo_de_texto_producto.delete(0,10)
            campo_de_texto_receptaculo.delete(0,10)
            campo_de_texto_pais.delete(0,10)
            campo_de_texto_peso.delete(0,10)
            self.lista_productos.pop(0)
            
            return
        def funcion_insertar():
            if campo_de_texto_producto.get():
                return

            else:
                primer_producto = self.lista_productos[0]
                campo_de_texto_producto.insert(0,primer_producto.producto_id)
                campo_de_texto_receptaculo.insert(0,primer_producto.contenedor_id)
                campo_de_texto_pais.insert(0,primer_producto.pais)
                campo_de_texto_peso.insert(0,primer_producto.peso)


        def funcion_enviar():
            listbox.delete(0,10)

            return

        
        
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
        


        etiqueta_listbox= Label(self.parent, text="Lista de productos").grid(row=12, column=2)
        listbox = Listbox(self.parent, width=70)
        listbox.grid( pady=10 ,row=12, column=2,columnspan=2, sticky='w')
        



if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("600x500")
    APP = UI([],parent=ROOT)
    APP.pack()
    APP.mainloop()
    ROOT.destroy()


