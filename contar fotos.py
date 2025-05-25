import os

def contar_imagenes_en_subcarpetas(ruta_base, extensiones_imagenes=None):
    if extensiones_imagenes is None:
        #extensiones_imagenes = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}
        extensiones_imagenes = {".jpg"}
    
    contador_total = 0

    for ruta, subcarpetas, archivos in os.walk(ruta_base):
        for archivo in archivos:
            _, extension = os.path.splitext(archivo)
            if extension.lower() in extensiones_imagenes:
                contador_total += 1

    return contador_total

# Cambia 'ruta_base' por la ruta de tu carpeta principal
ruta_base = "C:\Programming offline\Fotos"
numero_imagenes = contar_imagenes_en_subcarpetas(ruta_base)

print(f"Número total de imágenes: {numero_imagenes}")
