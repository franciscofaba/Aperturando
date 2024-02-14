
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime
from crud_envios import read_envios_by_lotes
import code128
from os.path import dirname, join
from PIL import Image, ImageDraw, ImageFont
import subprocess


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
        c = canvas.Canvas(pdf_path, pagesize=A4)
        w, h = A4
        
        c.drawImage(imagen_path, 320, 725, width=200, height=100)
        hora_actual = datetime.now().strftime("Hora: %H:%M:%S  Fecha: %d-%m-%Y")
        c.drawString(70, 800, f"Estado Aduana: {estado_aduana}")
        c.drawString(70, 760, f"{hora_actual}")
        c.drawString(70, 780, f"ID:     {id_lote}")
        c.drawString(70, 740, f"Estado del lote:  EN ESPERA")
        c.rect(50, 700, 495, 130)
        c.rect(50, 100, 495, 580)
        lista = cargar(id_lote)
        c.drawString(55, 668, f"CONTENIDO DEL LOTE:")
        c.rect(50, 645, 495, 20)
        c.line(200, 100, 200, 100 + 565)
        
        c.drawString(60, 650, f"ID envio:")
        c.drawString(220, 650, f"ID envase:")
        
        contador = 620
        for i in lista:
                id_envios = c.drawString(60, contador, f"{i.get("envio")}")
                id_envios.setFont("Times-Roman", 12)
                id_envase = c.drawString(220, contador, f"{i.get("envase")}")
                id_envase.setFont("Times-Roman", 12)
                contador-=20
        
        
        c.save()



def imprimir_pdf(ruta_pdf):
        ruta_archivo_pdf = 'ruta/al/archivo.pdf'
        imprimir_pdf(ruta_archivo_pdf)
        comando = ['lp', ruta_pdf]
        proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida, error = proceso.communicate()

        if error:
                print("Ocurrió un error al imprimir el archivo:")
                print(error.decode('utf-8'))
        else:
                print("El archivo se ha enviado a imprimir correctamente.")

        # Llamar a la función e indicar la ruta del archivo PDF a imprimir
