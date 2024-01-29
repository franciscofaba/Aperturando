from productos import Producto
from Front import UI
import tkinter as tk
import sys


"""lista de prueba"""

producto1 = Producto("1", "A1", "USA", "10")
producto2 = Producto("2", "B1", "Canada", "15")
producto3 = Producto("3", "C1", "Mexico", "8")

lista_productos = [producto1,producto2,producto3]



"""iniciar ventana tkinter"""

def cerrar_ventana():
    sys.exit()    
    ROOT.destroy()



ROOT = tk.Tk()
ROOT.geometry("1000x600")
ROOT.protocol("WM_DELETE_WINDOW", cerrar_ventana)
app = UI(lista_productos, parent=ROOT)


ROOT.mainloop() 











