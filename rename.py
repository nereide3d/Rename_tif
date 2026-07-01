import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def seleccionar_y_renombrar():
    # Crear una ventana oculta para que no aparezca una ventana principal vacía
    root = tk.Tk()
    root.withdraw()
    
    # Abrir el selector de carpetas
    carpeta_seleccionada = filedialog.askdirectory(title="Selecciona la carpeta con las imágenes")
    
    # Si el usuario cancela (cierra la ventana), salir
    if not carpeta_seleccionada:
        print("Operación cancelada.")
        return

    print(f"Procesando carpeta: {carpeta_seleccionada}")
    
    cambiados = 0
    # Recorrer archivos
    for nombre_archivo in os.listdir(carpeta_seleccionada):
        # Patrón para borrar paréntesis y lo que haya dentro
        if re.search(r'\(.*?\)', nombre_archivo):
            nuevo_nombre = re.sub(r'\(.*?\)', '', nombre_archivo)
            
            # Construir rutas
            viejo_path = os.path.join(carpeta_seleccionada, nombre_archivo)
            nuevo_path = os.path.join(carpeta_seleccionada, nuevo_nombre)
            
            # Renombrar
            os.rename(viejo_path, nuevo_path)
            print(f"✅ Renombrado: {nombre_archivo} -> {nuevo_nombre}")
            cambiados += 1
            
    # Mensaje final
    messagebox.showinfo("Proceso Terminado", f"Se han renombrado {cambiados} archivos con éxito.")
    print(f"\nProceso finalizado. Total de archivos renombrados: {cambiados}")

if __name__ == "__main__":
    seleccionar_y_renombrar()