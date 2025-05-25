import json

def convert_json_to_js(input_file, output_file):
    try:
        # Leer el archivo JSON
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Formatear los datos al formato requerido
        js_data = []
        for entry in data:
            relative_path = entry.get("relative_path")
            date = entry.get("date")
            coordinates = entry.get("coordinates")

            if coordinates:
                js_data.append([relative_path, date, coordinates[0], coordinates[1]])

        # Escribir el archivo JS con el formato adecuado
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("const myData = ")
            json.dump(js_data, file, indent=4)
            file.write(";")

        print(f"Datos convertidos y guardados en: {output_file}")

    except Exception as e:
        print(f"Error al convertir el archivo JSON a JS: {e}")

# Rutas de los archivos de entrada y salida
input_file = "2. marian_imagenes_procesadas.json"  # Reemplaza con el nombre de tu archivo JSON
output_file = "3. marian_data.js"   # Nombre para el archivo .js

# Convertir el archivo JSON a JS
convert_json_to_js(input_file, output_file)
