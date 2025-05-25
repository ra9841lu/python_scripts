import os
import exifread

def extract_metadata_from_images(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff', '.bmp')):
            file_path = os.path.join(folder_path, filename)
            
            print(f"\nMetadatos de la imagen: {filename}")
            try:
                with open(file_path, 'rb') as image_file:
                    # Leer metadatos con exifread
                    tags = exifread.process_file(image_file)
                    if tags:
                        for tag, value in tags.items():
                            print(f"{tag}: {value}")
                    else:
                        print("No se encontraron metadatos EXIF.")
            except Exception as e:
                print(f"Error al procesar {filename}: {e}")

# Ruta a la carpeta que contiene las imágenes
folder_path = r"C:\Programming offline\Fotos paderborn\2022_01"
extract_metadata_from_images(folder_path)
