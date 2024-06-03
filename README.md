# ComprimirPDF

Este script de Python comprime archivos pdf creados a partir de documentos escaneados comprimiendo cada una de las imágenes que lo componen de acuerdo a dos parámetros (escala y calidad)

## Requirements

Para correr este script necesitarás:

- Python 3.9 or later
 
- Instalar las siguientes librerías: img2pdf, pypdfium2, pillow

## Instalación

Para instalar las librerías

En la terminal -zsh de VSCode:

```zsh
pip install img2pdf
pdfium2: python -m pip install -U pypdfium2
pillow: pip install pillow 
```

## Utilización

Para usar este script deberás modificar el nombre del archivo pdf a comprimir `pdfOriginal` y el del archivo de salida ya comprimido `pdfComprimido.pdf` (este último no es obligatorio).
Además se deberán elegir los parametros `escala` y `calidad` con la que se quieren comprimir las imágenes del pdf

```python
nombre_pdf = "pdfOriginal.pdf" #línea 22
nombre_pdf_comprimido = "pdfComprimido.pdf" #línea 23
```

```python
escala = 1 #línea 25
```

```python
calidad = 50 #línea 46
```
Una vez que ya se hayan realizado estos pasos, de los que solo el renombrar el archivo pdfOriginal.pdf es obligatorio, se está en disposición de correr el script de python

```zsh
python comprimirPDF.py
```

Entonces se obtendrá un archivo pdf comprimido en la misma carpeta en la que está el archivo pdfOriginal
