import glob
import os

ruta = r"/Users/marcosefrainzunigahernandez/Desktop/Auto-File-Organizer/Data/Origen"

# Aquí es donde ocurre la magia de glob:
# Concatenamos la ruta con el filtro *.txt
filtro = f"{ruta}/*.txt"
archivos_txt = glob.glob(filtro)

print(f"He encontrado {len(archivos_txt)} archivos de texto.")

for archivo in archivos_txt:
    # glob nos da la ruta completa, extraemos solo el nombre para el print
    nombre = os.path.basename(archivo)
    print(f"Nombre del archivo: {nombre}")