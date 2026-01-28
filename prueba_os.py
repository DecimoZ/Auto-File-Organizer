import os

# Cambia esto por una ruta real de tu PC (usa la 'r' antes de las comillas)
mi_ruta = r"C:\Users\Marcos\Desktop\Auto-File-Organizer\Data\Origen"

# Paso 1: Listar el contenido
contenido = os.listdir(mi_ruta)
print(f"He encontrado {len(contenido)} elementos.")

# Paso 2: Diferenciar archivos de carpetas
for nombre in contenido:
    # Pegamos la ruta para poder analizarla
    ruta_completa = os.path.join(mi_ruta, nombre)
    
    if os.path.isfile(ruta_completa):
        print(f"📄 ARCHIVO: {nombre}")
    else:
        print(f"📁 CARPETA: {nombre}")