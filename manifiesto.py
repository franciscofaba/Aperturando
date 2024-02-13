
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime
from barcode import Code128
from barcode.writer import ImageWriter
from crud_envios import read_envios_by_lotes
import base64
import code128
import base64
import io
from os.path import dirname, join
from PIL import Image, ImageDraw, ImageFont

def cargar(id_lote):
        lista_productos = read_envios_by_lotes(id_lote)
        print(lista_productos)
        return lista_productos


def generate_barcode(id_lote):
        barcode_param = str(id_lote)
        barcode_text = str(id_lote)

        barcode_image = code128.image(barcode_param, height=100)
        w, h = barcode_image.size
        margin = 20
        new_h = h + (2 * margin) 
        new_image = Image.new('RGB', (w, new_h), (255, 255, 255))
        new_image.paste(barcode_image, (0, margin))
        draw = ImageDraw.Draw(new_image)
        draw.text((20, new_h - 10), barcode_text, fill=(0, 0, 0))#, font=fnt)  # 
        path='manifiesto_bin/barcode.png'
        new_image.save(path, 'PNG')
        

def generate_manifest(id_lote,estado_aduana):
        generate_barcode(id_lote)
        
        imagen_path=f'manifiesto_bin/barcode.png'
        pdf_path = f"manifiesto_bin/documento.pdf"
        print(imagen_path)
        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.drawImage(imagen_path, 340, 700, width=200, height=100)
        hora_actual = datetime.now().strftime("Hora: %H:%M:%S  Fecha: %d-%m-%Y")
        c.drawString(100, 770, f"estado_aduana: {estado_aduana}")
        c.drawString(100, 730, f"{hora_actual}")
        c.drawString(100, 750, f"ID:     {id_lote}")
        c.drawString(100, 710, f"Estado del lote:  EN ESPERA")
        c.drawString(0, 690, f"__________________________________________________________________________________________________________________________________________-")
        lista = cargar(id_lote)
        c.drawString(50, 670, f"CONTENIDO DEL LOTE:")
        contador = 650
        for i in lista:
                c.drawString(100, contador, f"| ID envio: {i.get("envio")} | ID Envase: {i.get("envase")}")
                contador-=20
        
        
        c.save()

        