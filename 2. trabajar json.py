import json

def dms_to_decimal(dms):
    """Convierte coordenadas DMS (grados, minutos, segundos) a decimal"""
    try:
        grados = float(dms[0])
        minutos = float(dms[1])
        segundos = float(eval(str(dms[2])))  # Evalúa divisiones como "6447/250"
        decimal = grados + (minutos / 60) + (segundos / 3600)
        return round(decimal, 6)  # Redondear a 6 decimales
    except Exception as e:
        print(f"Error al convertir DMS a decimal: {e}")
        return None

def parse_gps_value(value):
    """Convierte el valor GPS del formato EXIF a un número decimal"""
    if not value or value == "None":
        return None
    try:
        dms = eval(str(value))  # Convierte el valor EXIF a una lista
        return dms_to_decimal(dms)
    except Exception as e:
        print(f"Error al parsear el valor GPS: {e}")
        return None

def process_json_file(input_file, output_file):
    try:
        # Leer el archivo JSON existente
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        processed_data = []

        for entry in data:
            # Extraer los valores originales
            lat = entry.get("GPSLatitude")
            lon = entry.get("GPSLongitude")
            date = entry.get("Image DateTime", None)

            # Convertir coordenadas GPS a decimal
            lat_decimal = parse_gps_value(lat)
            lon_decimal = parse_gps_value(lon)

            # Crear una nueva estructura con las coordenadas decimales y la fecha
            processed_entry = {
                "relative_path": entry.get("relative_path"),
                "coordinates": [lat_decimal, lon_decimal] if lat_decimal and lon_decimal else None,
                "date": date
            }
            processed_data.append(processed_entry)

        # Guardar los datos procesados en un nuevo archivo JSON
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(processed_data, file, indent=4, ensure_ascii=False)

        print(f"Datos procesados y guardados en: {output_file}")

    except Exception as e:
        print(f"Error al procesar el archivo JSON: {e}")

# Ruta al archivo JSON original y al archivo de salida
input_file = "1.marian_gps_y_fechas.json"  # Reemplaza con el nombre de tu archivo JSON
output_file = "2. marian_imagenes_procesadas.json"

# Procesar el archivo JSON
process_json_file(input_file, output_file)
