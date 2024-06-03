# Script escrito en VS Code por Pedro J. Ramón Torregrosa
# El objetivo de este código es comprimir archivos pdf pesados controlando la ratio de compresión de las imágenes
# Para ello lo que vamos a hacer es comprimir todas las páginas tomadas como imagen (documentos escaneados) 
# recorriendo todas las páginas del pdf y almacenándolas primero como imágenes y luego recomponiendo el pdf original 
# pero con las imágenes ya comprimidas


# Antes de utilizar el código deberás instalar las librerías
### img2pdf: pip install img2pdf
### pdfium2: python -m pip install -U pypdfium2
### pillow: pip install pillow


import pypdfium2 as pdfium
from pathlib import Path
from PIL import Image
import img2pdf
import os

# En primer lugar definiremos las variables

nombre_pdf = "ArchivoPrueba.pdf"
nombre_pdf_comprimido = "PdfComprimido.pdf"
nombre_pdf_sin_extension = Path(nombre_pdf).stem
escala = 1 # Escala para convertir PDF a imagen. Hay que tener cuidado porque también afecta a las imágenes

# Extraemos cada página del PDF como imagen y las almacenamos de manera independiente

pdf = pdfium.PdfDocument(nombre_pdf)
cantidad_paginas = len(pdf)
imagenes = []
for indice_pagina in range(cantidad_paginas):
    numero_pagina = indice_pagina+1 #Recuerda que al numerar Python empieza en 0 por lo que la primera página del doc será 0+1
    nombre_imagen = f"{nombre_pdf_sin_extension}_{numero_pagina}.jpg"
    imagenes.append(nombre_imagen)
    print(f"Extrayendo página {numero_pagina} de {cantidad_paginas}")
    pagina = pdf.get_page(indice_pagina)
    imagen_para_pil = pagina.render(scale=escala).to_pil() #pillow es la libreria que nos vav a permitir comprimir las imágenes extraídas del pdf 
    imagen_para_pil.save(nombre_imagen)

imagenes_comprimidas = []

# Ahora comprimimos todas las imágenes anteriores.
# Debemos buscar un compromiso entre la razon de compresión y la calidad de las imágenes resultantes
# Para ello definimos el parámetro "calidad"
calidad = 50 # Este valor se mueve entre 0 (nada) y 100 (imagen sin comprimir)
for nombre_imagen in imagenes:
    print(f"Comprimiendo {nombre_imagen}...")
    nombre_imagen_sin_extension = Path(nombre_imagen).stem
    nombre_imagen_salida = nombre_imagen_sin_extension + \
        "_comprimida" + nombre_imagen[nombre_imagen.rfind("."):]
    imagen = Image.open(nombre_imagen)
    imagen.save(nombre_imagen_salida, optimize=True, quality=calidad)
    imagenes_comprimidas.append(nombre_imagen_salida)

# Ahora creamos el pdf comprimido con las imágenes comprimidas según el parámetro calidad

print("Creando PDF comprimido...")
with open(nombre_pdf_comprimido, "wb") as documento:
    documento.write(img2pdf.convert(imagenes_comprimidas))

# Como habíamos creado muchas imágenes temporales debemos borrarlas

for imagen in imagenes + imagenes_comprimidas:
    os.remove(imagen)
