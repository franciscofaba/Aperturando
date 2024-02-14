from calendar import c
from Front_Lotes import main_lotes
import tkinter as tk
from tkinter import *
from manifiesto import generate_manifest
from productos import llamar_producto
from tkinter import ttk
import datetime
from guardar import updt_prod_lot
import sys
from crud_envios import read_all_en_proceso, read_all_envios, read_envios, update_envios
from tkinter import messagebox
import openpyxl
from manifiesto import generate_manifest
from ttkthemes import ThemedTk
from balanza import leer_balanza


class UI(tk.Frame):
    def __init__(self, root,lista_productos, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.lista_productos = lista_productos
        self.init_ui(root)
        
        


    def init_ui(self, root):
        
    # Funciones: ____________________________________________________________
        def volver():
            root.deiconify() 
            self.parent.destroy()
    
    #esta funcion pasa los atributos desde los campos de texto al treeview
        def abrir_lotes():
            self.parent.withdraw()
            main_lotes(self.parent)
    
        def funcion_guardar(event=None):          
            if campo_de_texto_producto.get():
                
                primer_producto = self.lista_productos[0]
                item=tree.insert('', 'end', text="1", values=(primer_producto.envio, primer_producto.envase, primer_producto.paisOrigen, primer_producto.pesoEspecificado, primer_producto.pesoPreaviso, primer_producto.estadoActual, primer_producto.paisDestino, primer_producto.ultimaModificacion, primer_producto.destino_cl))
                campo_de_texto_producto.delete(0,100)
                campo_de_texto_receptaculo.delete(0,100)
                campo_de_texto_pais.delete(0,100)
                campo_de_texto_peso.delete(0,100)
                
                
                if primer_producto.destino_cl == 'santiago':
                    tree.item(item, tags=('santiago',))
                elif primer_producto.destino_cl == 'Santiago':
                    tree.item(item, tags=('santiago',))
                elif primer_producto.destino_cl== 'Carteroresto':
                    tree.item(item, tags=('carteroresto',))
                elif primer_producto.destino_cl== 'carteroresto':
                    tree.item(item, tags=('carteroresto',))
                    
                id_envio = primer_producto.envio
                json_en_proceso = {
                    "en_proceso":"si"
                }
                update_envios(id_envio, json_en_proceso)
                print(update_envios)
                self.lista_productos.pop(0)
                quitar_destino()

        def quitar_destino():
            global global_label
            
            
            if global_label:
                global_label.destroy()
                global_label = None
                        
                


    #esta funcion se supone que envia los productos pero solo los borra realmente
    
        def funcion_enviar(event=None):
            
            lista = [] 
            for child in tree.get_children():
                item=tree.item(child)["values"]
                objeto = read_envios(item[0])
                lista.append(objeto)
                
            estado_aduana = estado_var.get()
            
            if estado_aduana:
                hora_actual = datetime.datetime.now()
                id_lote = updt_prod_lot(lista,estado_aduana,hora_actual)
                generate_manifest(id_lote,estado_aduana)
                messagebox.showinfo(message="Apertura exitosa! (lote quedo en estado de espera para ser despachado)", title="APERTURA")
                tree.delete(*tree.get_children())
                return
            else:
                messagebox.showwarning(message="Seleccione Liberado o Retenido para continuar.", title="APERTURA/warning")


    #funcion para borrar solamente un producto
    
        def delete(event=None): 
            selected_item = tree.selection()[0]
            enviodelete = tree.item(tree.selection())['values'][0] 
            
            tree.delete(selected_item)
            
            datos = {
                    "en_proceso": ""
                    }
                    
            update = update_envios(enviodelete, datos)


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
            entryedit = ttk.Entry (self.parent, width=75, foreground="black")
            entryedit.place(x=425,y=265)
            
            #boton de ok para guardar el edit
            okb = ttk.Button(self.parent, text='OK', width=4, command=saveedit)
            okb.configure(padding=(3, 0))
            okb.place(x=890,y=265)
            
            #boton de salir para salir del modo edicion
            salir_boton = ttk.Button(self.parent, text='Salir de editar', command=salir)
            salir_boton.configure(padding=(3, 0))
            salir_boton.place(x=310,y=264)
            
            #se inserta el elemento que se quiere modificar en el campo de texto para que sea mas facil para el usuario 
            entryedit.insert(0,tree.item(tree.selection())['values'][cn-1])
            
            
    
        def display_destino():
            global global_label
            var_envio = self.lista_productos[0]
            
            if var_envio.destino_cl== 'santiago':
                global_label = ttk.Label(self.parent, text="DESTINO:   SANTIAGO",background="green", font=("Arial", 30))
                global_label.place(x=270,y=500)
            elif var_envio.destino_cl== 'Santiago':
                global_label = ttk.Label(self.parent, text="DESTINO:   SANTIAGO",background="green", font=("Arial", 30))
                global_label.place(x=270,y=500)
            elif var_envio.destino_cl== 'Carteroresto':
                global_label = ttk.Label(self.parent, text="DESTINO:   REGIÓN",background="BLUE", font=("Arial", 30))
                global_label.place(x=270,y=500)
            elif var_envio.destino_cl== 'carteroresto':
                global_label = ttk.Label(self.parent, text="DESTINO:   REGIÓN",background="BLUE", font=("Arial", 30))
                global_label.place(x=270,y=500)
    

            
            
    #esta funcion permite que al apretar Enter sobre el campo_de_texto_producto se llame a la api o se ejecute la funcion guardar dependiendo si ya se llamo o no a la api  
        def on_enter(id): 
            if campo_de_texto_pais.get():
                funcion_guardar()
                return
            else:
                nuevo_producto = llamar_producto(id)
                campo_de_texto_receptaculo.insert(0,nuevo_producto.envase)
                campo_de_texto_pais.insert(0,nuevo_producto.paisOrigen)
                peso = leer_balanza()
                campo_de_texto_peso.insert(0,peso)
                self.lista_productos.append(nuevo_producto)
                display_destino()
                return
            
            
    #esta funcion permite limitar a solo 13 caracteres el campo de texto de producto
    
        def limitar_longitud(*args):
            max_chars = 13  # Establece el número máximo de caracteres permitidos
            current_text = campo_de_texto_producto.get()
            if len(current_text) > max_chars:
                new_text = current_text[:max_chars]
                campo_de_texto_producto.delete(0, tk.END)
                campo_de_texto_producto.insert(0, new_text)
                
        def comprobar_guardado():
            en_proceso = read_all_en_proceso()
            if en_proceso:
                respuesta_messagebox=(messagebox.askyesno(message="No se guardo correctamente la sesion anterior ¿Desea continuar?", title="ALERTA"))
                print(respuesta_messagebox)
                if respuesta_messagebox==True:
                    for envio in en_proceso:
                        insertar_recuperacion(envio)
        
                if respuesta_messagebox==False:
                    
                    datos = {
                    "en_proceso": ""
                    }
                    
                    for envio in en_proceso:
                        id = envio.get("envio")
                        update = update_envios(id, datos)
                    
                    
        def insertar_recuperacion(objeto_envio):
            item = tree.insert('', 'end', text="1", values=(
            objeto_envio.get('envio'), 
            objeto_envio.get('paisOrigen'), 
            objeto_envio.get('pesoEspecificado'), 
            objeto_envio.get('envase'), 
            objeto_envio.get('pesoPreaviso'), 
            objeto_envio.get('estadoActual'), 
            objeto_envio.get('paisDestino'), 
            objeto_envio.get('ultimaModificacion'),
            objeto_envio.get('destino_cl')))
            
            if objeto_envio.get('destino_cl') == 'santiago':
                tree.item(item, tags=('santiago',))
            elif objeto_envio.get('destino_cl') == 'Santiago':
                tree.item(item, tags=('santiago',))
            elif objeto_envio.get('destino_cl')== 'Carteroresto':
                tree.item(item, tags=('carteroresto',))
            elif objeto_envio.get('destino_cl')== 'carteroresto':
                tree.item(item, tags=('carteroresto',))
            

# WiDGET: ________________________________________________________________________
        #seleccionar el estilo de la ventana
        
        style = ttk.Style()
        style.configure('TButton', font=('American typewriter', 10), foreground='black')
        style.configure('TLabel', font=('calibri', 10, 'bold'), foreground='black')

        
        
    # titulo de la ventana
        self.parent.title("Aperturacion")

        self.ems_logo = tk.PhotoImage(file="icons/Ems-Logo.png")
        self.ems_logo = self.ems_logo.subsample(15)
        button_imagen= tk.Button(self.parent, text="",image=self.ems_logo, height=20, relief="flat")
        
        button_imagen.place(x=5, y=0)
        
    # primer campo de texto (Envio)
        
        etiqueta_producto= ttk.Label(self.parent, text="Codigo de Envio: ")
        etiqueta_producto.place(x=80,y=35)
        campo_de_texto_producto= ttk.Entry(self.parent, width=50, foreground='black')
        campo_de_texto_producto.place(x=80,y=55)
        campo_de_texto_producto.bind("<KeyRelease>", limitar_longitud)
        try:
            
            campo_de_texto_producto.bind("<Return>", lambda event: on_enter(campo_de_texto_producto.get()))
        except Exception as e:
            print("sigue...", e)
        

    # segundo campo de texto (Envase)
        etiqueta_receptaculo= ttk.Label(self.parent, text="ID Envase: ")
        etiqueta_receptaculo.place(x=80,y=85)
        campo_de_texto_receptaculo= ttk.Entry(self.parent, width=50, foreground='black')
        campo_de_texto_receptaculo.place(x=80,y=105)
        campo_de_texto_receptaculo.get()
        
        
    # tercer campo de texto (Pais de origen)
        etiqueta_pais= ttk.Label(self.parent, text="País de origen:")
        etiqueta_pais.place(x=80,y=135)
        campo_de_texto_pais= ttk.Entry(self.parent, width=50, foreground='black')
        campo_de_texto_pais.place(x=80,y=155)
        campo_de_texto_pais.get()
        
        
    # cuarto campo de texto (Peso)
        etiqueta_peso= ttk.Label(self.parent, text="Peso:")
        etiqueta_peso.place(x=80,y=185)
        campo_de_texto_peso= ttk.Entry(self.parent, width=50)
        campo_de_texto_peso.place(x=80,y=205)
        
        
    # Botones 
        boton_guardar = ttk.Button(self.parent, text="guardar", command=funcion_guardar, width=10).place(x=80,y=250)
        boton_enviar = ttk.Button(self.parent, text="Enviar!", command=funcion_enviar , width=10).place(x=835,y=480)
        boton_delete = ttk.Button(self.parent, text="Borrar seleccion", command=delete , width=15).place(x=80,y=480)
        boton_lotes= ttk.Button(self.parent, text="Lotes en espera", command=abrir_lotes, width= 18).place(x=800,y=580)
        boton_lotes= ttk.Button(self.parent, text="volver", command=volver, width= 12).place(x=830,y=10)
    #radiobotones
        estado_var = tk.StringVar()
        rb_liberado = ttk.Radiobutton(self.parent, text="Liberado", variable=estado_var, value="Liberado")
        rb_liberado.place(x=570,y=175)
        rb_retenido = ttk.Radiobutton(self.parent, text="Retenido", variable=estado_var, value="Retenido")
        rb_retenido.place(x=650,y=175)
        
        style.configure("TRadiobutton", font=('Calibri', 9), foreground="black")

    
    
    
    
    # bin de teclas
        self.parent.bind("<Right>",funcion_guardar)
        self.parent.bind("<Up>",funcion_enviar)
        

    #Primera Lista desplegable (Estado del producto)
        etiqueta_destino_producto= ttk.Label(self.parent, text="Status:").place(x=450,y=35)
        lista_destino_producto = ttk.Combobox(
            self.parent,
            state="readonly",
            values=["MINL Normal", "MIMS Mal encaminado", "MIAT En Transito", "MIRD Retornado/Reencaminado en Transito", "MIRT Retornado"],
            width=50,
            foreground='black'
        )
        lista_destino_producto.place(x=450,y=55)
        lista_destino_producto.set("MINL Normal")


    #Segunda lista desplegable (Condicion del producto)
        etiqueta_condicion_producto= ttk.Label(self.parent, text="Condicion del producto:").place(x=450,y=95)
        lista_condicion_producto = ttk.Combobox(
            self.parent,
            state="readonly",
            values=["30 Envio Recibido en Buena Condicion", "31 Envio Dañado o Roto", "32 Envio Violado"],
            width=50,
            foreground='black'
        )
        lista_condicion_producto.place(x=450,y=115)
        lista_condicion_producto.set("30 Envio Recibido en Buena Condicion")


    
    #Etiqueta con tipo de oficina
        etiqueta_oficina= ttk.Label(self.parent, text="Estado Aduana:").place(x=450,y=175)
       


 



    
    
# widget: TREEVIEW ______
        
    # abrir y posicionar el treeview
        tree = ttk.Treeview(self.parent, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9"), show='headings', height=6, style="mystyle.Treeview")
        tree.column("# 1", anchor=CENTER, minwidth=0, width=90, stretch=NO)
        tree.heading("# 1", text="Envio")
        tree.column("# 2", anchor=CENTER, minwidth=0, width=90, stretch=TRUE)
        tree.heading("# 2", text="Envase")
        tree.column("# 3", anchor=CENTER, minwidth=0, width=90, stretch=NO)
        tree.heading("# 3", text="Pais de Origen")
        tree.column("# 4", anchor=CENTER, minwidth=0, width=90, stretch=NO)
        tree.heading("# 4", text="Peso con Preaviso")
        tree.column("# 5", anchor=CENTER, minwidth=0, width=90, stretch=YES)
        tree.heading("# 5", text="Peso")
        tree.column("# 6", anchor=CENTER, minwidth=0, width=90, stretch=NO)
        tree.heading("# 6", text="Estado Actual")
        tree.column("# 7", anchor=CENTER, minwidth=0, width=90, stretch=NO)
        tree.heading("# 7", text="Pais de Destino")
        tree.column("# 8", anchor=CENTER, minwidth=0, width=90, stretch=NO)
        tree.heading("# 8", text="Ultima Modificancion")
        tree.column("# 9", anchor=CENTER, minwidth=0, width=90, stretch=NO)
        tree.heading("# 9", text="dest. en Chile")
        tree.place(x=80, y=300, height=170)
        
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 9), foreground="black")
        tree.bind("<<TreeviewSelect>>", display_destino)
    # bind para hacer doble click en un producto y modificarlo
        tree.bind('<Double-1>', set_cell_value)
            
        
    #abrir y posicionar el scrollbar del treeview
        vsb = ttk.Scrollbar(self.parent, orient="vertical", command=tree.yview)
        vsb.place(x=920, y=300, height=170)
        
        tree.configure(yscrollcommand=vsb.set)
        
        tree.tag_configure('santiago', background='green', foreground='white')
        tree.tag_configure('carteroresto', background='blue', foreground='white')
        
 #widget: Footer : ______

    #etiqueta con las indicaciones para editar un item del treeview
        style.configure("BW.TLabel", foreground="grey")
        
        etiqueta_edit= ttk.Label(self.parent, text="Consejo:  para editar seleccione el elemento que desea cambiar y haga doble clic en él.", style="BW.TLabel")
        etiqueta_edit.place(x=425,y=235)
        

    #datos del usuario que se colocaran en el futer
        Usuario = "Usuario.apellido/(Normal)"
        Grupo = 'CORREOINTERNO/'
        fecha_usuario=datetime.datetime.now()

    #etiqueta que hace de footer
        sbar = ttk.Label(self.parent, text='CLSCLD              |              '+str(Grupo)+"NOT-860195-055              |              "+str(Grupo)+str(Usuario)+"              |              "+str(fecha_usuario),relief=SUNKEN, anchor="w", foreground="grey")
        sbar.place(x=0, y=630, height=20, width=1000)
    
# variables globales: ________

        global_label = None
        comprobar_guardado()        
#____________________________________________________________________#

        
        
        



#esta funcion permite iniciar la venta desde otros Scrypts.

def iniciar_ventana(root):
   
    def cerrar_ventana():
        sys.exit()    
        ROOT_EMS.destroy()

    # llamar ventana
    
    ROOT_EMS = Toplevel()
    color = ttk.Style().lookup("TFrame", "background", default="white")
    
    ROOT_EMS.configure(bg=color)
    # datos para las dimesiones
    w = 1000
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
    APP = UI(root,lista_productos,parent=ROOT_EMS)
    #seleccionar el estilo de la ventana
    APP.mainloop()


    
if __name__ == "__main__":
    root = ThemedTk(theme='arc')
    root.set_theme_advanced('arc', brightness=1.0, saturation=2.0, hue=1.0, preserve_transparency=False, output_dir=None)
    
    root.withdraw()
    iniciar_ventana(root)
        