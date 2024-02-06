from turtle import width
import tkinter as tk
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




    def init_ui(self):
        
    # Funciones: ____________________________________________________________
    
    
    #esta funcion pasa los atributos desde los campos de texto al treeview
    
        def funcion_guardar(event=None):          
            if campo_de_texto_producto.get():
                primer_producto = self.lista_productos[0]
                item=tree.insert('', 'end', text="1", values=(primer_producto.envio, primer_producto.envase, primer_producto.paisOrigen, primer_producto.pesoEspecificado, primer_producto.pesoPreaviso, primer_producto.estadoActual, primer_producto.paisDestino, primer_producto.ultimaModificacion))
                campo_de_texto_producto.delete(0,100)
                campo_de_texto_receptaculo.delete(0,100)
                campo_de_texto_pais.delete(0,100)
                campo_de_texto_peso.delete(0,100)
                self.lista_productos.pop(0)


    #esta funcion se supone que envia los productos pero solo los borra realmente
    
        def funcion_enviar(event=None): 
            tree.delete(*tree.get_children())
            return


    #funcion para borrar solamente un producto
    
        def delete(event=None): 
            selected_item = tree.selection()[0]
            tree.delete(selected_item)


    #funcion para editar productos
    
        def set_cell_value(event): 
            
         #funcion para guardar producto editado
            def saveedit():
                if entryedit.get():
                    tree.set(item, column=column, value=entryedit.get())
                    entryedit.destroy()
                    okb.destroy()
                    salir_boton.destroy()
                else:
                    entryedit.destroy()
                    okb.destroy()
                    salir_boton.destroy()
                    
          #funcion para salir de la edicion          
            def salir(): 
                entryedit.destroy()
                okb.destroy()
                salir_boton.destroy()
                
                
            for item in tree.selection(): #permite encontrar el numero de la columna y el numero de la fila del item seleccionado
                item_text = tree.item(item, "values")
                column = tree.identify_column(event.x)
                row = tree.identify_row(event.y)
            
            #estas variables convierten el valor de las columnas y filas a int
            cn = int(str(column).replace('#', ''))
            rn = int(str(row).replace('I', ''))
            
            #campo de texto donde se modificar el elemento
            entryedit = tk.Entry (self.parent, width=50)
            entryedit.grid(pady=30, row=19, column=3, columnspan=2, sticky=S+N+W)
            
            #boton de ok para guardar el edit
            okb = ttk.Button(self.parent, text='OK', width=4, command=saveedit)
            okb.grid(pady=30, row=19, column=3, sticky="e")
            
            #boton de salir para salir del modo edicion
            salir_boton = tk.Button(self.parent, text='Salir de editar', width=10, command=salir)
            salir_boton.grid(pady=30,row=19, column=2, columnspan=1,  sticky="w")
            
            #se inserta el elemento que se quiere modificar en el campo de texto para que sea mas facil para el usuario 
            entryedit.insert(0,tree.item(tree.selection())['values'][cn-1])
            
            
    #esta funcion permite que al apretar Enter sobre el campo_de_texto_producto se llame a la api o se ejecute la funcion guardar dependiendo si ya se llamo o no a la api
        
        def on_enter(id): 
    
            print("Se presionó Enter")
            if campo_de_texto_pais.get():
                funcion_guardar()
                return
            else:
                nuevo_producto = construir_producto(id)
                campo_de_texto_receptaculo.insert(0,nuevo_producto.envase)
                campo_de_texto_pais.insert(0,nuevo_producto.paisOrigen)
                campo_de_texto_peso.insert(0,nuevo_producto.pesoPreaviso)
                self.lista_productos.append(nuevo_producto)
                return
            
            
    #esta funcion permite limitar a solo 13 caracteres el campo de texto de producto
    
        def limitar_longitud(*args):
            max_chars = 13  # Establece el número máximo de caracteres permitidos
            current_text = campo_de_texto_producto.get()
            if len(current_text) > max_chars:
                new_text = current_text[:max_chars]
                campo_de_texto_producto.delete(0, tk.END)
                campo_de_texto_producto.insert(0, new_text)

                

# WiDGET: ________________________________________________________________________


    # titulo de la ventana
        self.parent.title("Aperturacion")
        etiqueta_titulo= tk.Label(self.parent, text="Aperturacion", underline=8 ,padx=20, pady=10)
        etiqueta_titulo.grid(row=1, column=1)
    

    # primer campo de texto (Envio)
        etiqueta_producto= tk.Label(self.parent, text="Codigo de Envio: ")
        etiqueta_producto.grid(row=3, column=2, columnspan=2, sticky='w')
        campo_de_texto_producto= tk.Entry(self.parent, width=50)
        campo_de_texto_producto.grid(row=4, column=2,columnspan=2, sticky='w')
        campo_de_texto_producto.bind("<KeyRelease>", limitar_longitud)
        try:
            campo_de_texto_producto.bind("<Return>", lambda event: on_enter(campo_de_texto_producto.get()))
        except Exception as e:
            print("sigue...", e)
        

    # segundo campo de texto (Envase)
        etiqueta_receptaculo= tk.Label(self.parent, text="ID Envase: ")
        etiqueta_receptaculo.grid(row=5, column=2,columnspan=2, sticky='w')
        campo_de_texto_receptaculo= tk.Entry(self.parent, width=50)
        campo_de_texto_receptaculo.grid(row=6, column=2,columnspan=2, sticky='w')
        campo_de_texto_receptaculo.get()
        
        
    # tercer campo de texto (Pais de origen)
        etiqueta_pais= tk.Label(self.parent, text="País de origen:")
        etiqueta_pais.grid(row=7, column=2,columnspan=2, sticky='w')
        campo_de_texto_pais= tk.Entry(self.parent, width=50)
        campo_de_texto_pais.grid(row=8, column=2,columnspan=2 , sticky='w')
        campo_de_texto_pais.get()
        
        
    # cuarto campo de texto (Peso)
        etiqueta_peso= tk.Label(self.parent, text="Peso (Kg):")
        etiqueta_peso.grid( row=9, column=2,columnspan=2, sticky='w')
        campo_de_texto_peso= tk.Entry(self.parent, width=50)
        campo_de_texto_peso.grid(row=10, column=2,columnspan=2, sticky='w')
        
        
    # Botones 
        boton_guardar = tk.Button(self.parent, text="guardar", command=funcion_guardar, width=10).grid(padx=10, pady=10, row=11, column=2,columnspan=2, sticky='w')
        boton_enviar = tk.Button(self.parent, text="Enviar!", command=funcion_enviar , width=10).grid(pady=20, row=14, column=3 , sticky='e')
        boton_delete = tk.Button(self.parent, text="Borrar seleccion", command=delete , width=15).grid(padx=0, pady=10, row=14, column=2,columnspan=2, sticky='w')
        

    # bin de teclas
        self.parent.bind("<Right>",funcion_guardar)
        self.parent.bind("<Up>",funcion_enviar)
        
        
    #Primera Lista desplegable (Estado del producto)
        etiqueta_destino_producto= tk.Label(self.parent, text="Status:").grid(row=3, column=3,columnspan=2, sticky='w')
        lista_destino_producto = ttk.Combobox(
            self.parent,
            state="readonly",
            values=["MINL Normal", "MIMS Mal encaminado", "MIAT En Transito", "MIRD Retornado/Reencaminado en Transito", "MIRT Retornado"],
            width=50
        )
        lista_destino_producto.grid(row=4, column=3,columnspan=3, sticky='w')
        lista_destino_producto.set("MINL Normal")


    #Segunda lista desplegable (Condicion del producto)
        etiqueta_condicion_producto= tk.Label(self.parent, text="Condicion del producto:").grid(row=5, column=3,columnspan=2, sticky='w')
        lista_condicion_producto = ttk.Combobox(
            self.parent,
            state="readonly",
            values=["30 Envio Recibido en Buena Condicion", "31 Envio Dañado o Roto", "32 Envio Violado"],
            width=50
        )
        lista_condicion_producto.grid(row=6, column=3,columnspan=3, sticky='w')
        lista_condicion_producto.set("30 Envio Recibido en Buena Condicion")



    #Etiqueta con tipo de paquete    
        etiqueta_envio= tk.Label(self.parent, text="Tipo de Envio:").grid(row=7, column=3, sticky='w')
        etiqueta_envio_respuesta= tk.Label(self.parent, text="EMS",fg='#003').grid(padx=10,row=8, column=3,columnspan=2, sticky='w')
    
    
    #Etiqueta con tipo de oficina
        etiqueta_oficina= tk.Label(self.parent, text="Oficina:").grid(row=9, column=3, sticky="w")
        etiqueta_oficina_respuesta= tk.Label(self.parent, text="CLSCLD", fg='#003').grid(padx=10,row=10, column=3, sticky='w')


    #Etiqueta que no se ve pero que sirve para la estructura
        """not tocar es estructural"""
        etiqueta_tree= Label(self.parent, text="Lista de productos").grid(row=12, column=2)



    
    
# widget: TREEVIEW ______
        
    # abrir y posicionar el treeview
        tree = ttk.Treeview(self.parent, column=("c1", "c2", "c3","c4","c5","c6","c7","c8"), show='headings', height=6)
        tree.column("# 1", anchor=CENTER, minwidth=0, width=100, stretch=NO)
        tree.heading("# 1", text="Envio")
        tree.column("# 2", anchor=CENTER, minwidth=0, width=160, stretch=TRUE)
        tree.heading("# 2", text="Envase")
        tree.column("# 3", anchor=CENTER, minwidth=0, width=0, stretch=NO)
        tree.heading("# 3", text="Pais de Origen")
        tree.column("# 4", anchor=CENTER, minwidth=0, width=70, stretch=NO)
        tree.heading("# 4", text="Peso Real(kg.)")
        tree.column("# 5", anchor=CENTER, minwidth=0, width=90, stretch=YES)
        tree.heading("# 5", text="Peso con Preaviso (kg.)")
        tree.column("# 6", anchor=CENTER, minwidth=0, width=90, stretch=NO)
        tree.heading("# 6", text="Estado Actual")
        tree.column("# 7", anchor=CENTER, minwidth=0, width=90, stretch=NO)
        tree.heading("# 7", text="Pais de Destino")
        tree.column("# 8", anchor=CENTER, minwidth=0, width=90, stretch=NO)
        tree.heading("# 8", text="Ultima Modificancion")
        tree.grid( pady=10 ,row=12, column=2,columnspan=2, sticky='w')
        

    # bind para hacer doble click en un producto y modificarlo
        tree.bind('<Double-1>', set_cell_value)
    
    
    #seleccionar el estilo de la ventana
        s = ttk.Style()
        s.theme_use('clam')
        
        
    #abrir y posicionar el scrollbar del treeview
        vsb = ttk.Scrollbar(self.parent, orient="vertical", command=tree.yview)
        vsb.place(x=805, y=263, height=149)
        tree.configure(yscrollcommand=vsb.set)
        
 #widget: Footer : ______

    #etiqueta con las indicaciones para editar un item del treeview
        etiqueta_edit= Label(self.parent, text="Consejo:  para editar, seleccione el elemento que desea cambiar y haga doble clic en él.",padx=0, pady=0)
        etiqueta_edit.grid(row=17, column=2, columnspan=3)
        etiqueta_edit.config(fg="grey")

    #datos del usuario que se colocaran en el futer
        Usuario = "Usuario.apellido/(Normal)"
        Grupo = 'CORREOINTERNO/'
        fecha_usuario=datetime.now()

    #etiqueta que hace de footer
        sbar = Label(self.parent, text='CLSCLD              |              '+str(Grupo)+"NOT-860195-055              |              "+str(Grupo)+str(Usuario)+"              |              "+str(fecha_usuario),relief=SUNKEN, anchor="w")
        sbar.place(x=0, y=630, height=20, width=950)


#____________________________________________________________________#





#esta funcion permite iniciar la venta desde otros Scrypts.

def iniciar_ventana():
    def cerrar_ventana():
        sys.exit()    
        ROOT_EMS.destroy()

    # llamar ventana
    ROOT_EMS = tk.Tk()
    
    # datos para las dimesiones
    w = 950
    h = 650 
    ws = ROOT_EMS.winfo_screenwidth()
    hs = ROOT_EMS.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # especificaciones de la ventana
    ROOT_EMS.geometry('%dx%d+%d+%d' % (w, h, x, y))
    ROOT_EMS.protocol("WM_DELETE_WINDOW", cerrar_ventana)
    ROOT_EMS.resizable(0,0)

    # abrir la ventana
    lista_productos = []
    APP = UI(lista_productos,parent=ROOT_EMS)
    APP.mainloop()


    
if __name__ == "__main__":
    iniciar_ventana()
        