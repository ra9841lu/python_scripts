import os
import exifread
import json

def extract_gps_and_date(base_folder, output_file):
    metadata_list = []

    for root, _, files in os.walk(base_folder):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.tiff')):
                # Ruta completa y relativa del archivo
                file_path = os.path.join(root, filename)
                relative_path = os.path.relpath(file_path, base_folder)
                
                print(f"Procesando: {relative_path}")
                
                image_metadata = {"relative_path": relative_path, "GPSLatitude": None, "GPSLongitude": None, "DateTimeOriginal": None}
                try:
                    with open(file_path, 'rb') as image_file:
                        # Leer metadatos con exifread
                        tags = exifread.process_file(image_file)
                        
                        # Extraer GPS y fecha si están disponibles
                        image_metadata["GPSLatitude"] = str(tags.get("GPS GPSLatitude", None))
                        image_metadata["GPSLongitude"] = str(tags.get("GPS GPSLongitude", None))
                        image_metadata["DateTimeOriginal"] = str(tags.get("EXIF DateTimeOriginal", None))
                        image_metadata["Image DateTime"] = str(tags.get("Image DateTime", None))

                        #extraer coordenadas
                        image_metadata["EXIF GPSLatitude"] = str(tags.get("EXIF GPSLatitude", None))
                        image_metadata["EXIF GPSLongitude"] = str(tags.get("EXIF GPSLongitude", None))
                        
                        if not tags.get("GPS GPSLatitude") or not tags.get("GPS GPSLongitude"):
                            print(f"⚠️ No se encontraron datos GPS en {relative_path}")
                        if not tags.get("Image DateTime"):
                            print(f"⚠️ No se encontró la fecha en {relative_path}")
                
                except Exception as e:
                    print(f"Error al procesar {relative_path}: {e}")
                    image_metadata["error"] = str(e)
                
                # Añadir los datos al listado
                metadata_list.append(image_metadata)

    # Guardar los resultados en un archivo JSON
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(metadata_list, json_file, indent=4, ensure_ascii=False)
    
    print(f"\nDatos GPS y fecha guardados en: {output_file}")

# Ruta a la carpeta base que contiene las imágenes
base_folder = r"C:\Programming offline\Fotos asfalto marian\Fotos Marian"
# Ruta del archivo JSON de salida
output_file = "1.marian_gps_y_fechas.json"

# Ejecutar la función
extract_gps_and_date(base_folder, output_file)