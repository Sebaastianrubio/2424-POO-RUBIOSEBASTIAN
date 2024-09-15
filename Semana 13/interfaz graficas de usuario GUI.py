import tkinter as tk
from tkinter import messagebox

# Funciones
def agregar_datos():
    dato = entrada.get()  # Obtener el dato de la entrada de texto
    if dato:
        lista_datos.insert(tk.END, dato)  # Agregar el dato al Listbox
        entrada.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato")

def limpiar_datos():
    lista_datos.delete(0, tk.END)  # Limpiar todos los datos de la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("TAREA SEMANA 13")
ventana.geometry("300x300")

# Crear una entrada de texto
entrada = tk.Entry(ventana)
entrada.pack(pady=10)

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="AÑADIR", command=agregar_datos)
boton_agregar.pack(pady=5)

# Botón para limpiar datos
boton_limpiar = tk.Button(ventana, text="ELIMINAR", command=limpiar_datos)
boton_limpiar.pack(pady=5)

# Listbox para mostrar los datos agregados
lista_datos = tk.Listbox(ventana)
lista_datos.pack(pady=10)

# Iniciar el loop principal
ventana.mainloop()
