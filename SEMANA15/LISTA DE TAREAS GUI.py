
import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")

# Lista para almacenar las tareas
tareas = []

# Función para añadir una nueva tarea
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        tareas.append(tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, introduce una tarea.")

# Función para marcar una tarea como completada
def marcar_completada():
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(tarea_seleccionada)
        lista_tareas.delete(tarea_seleccionada)
        lista_tareas.insert(tarea_seleccionada, f"{tarea} ✔")
    except:
        messagebox.showwarning("Selección inválida", "Por favor, selecciona una tarea para marcarla como completada.")

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        lista_tareas.delete(tarea_seleccionada)
    except:
        messagebox.showwarning("Selección inválida", "Por favor, selecciona una tarea para eliminarla.")

# Widgets de la interfaz
# Campo de entrada para nueva tarea
entrada_tarea = tk.Entry(root, width=30)
entrada_tarea.pack(pady=10)

# Botón para añadir tarea
btn_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

# Lista para mostrar las tareas
lista_tareas = tk.Listbox(root, height=10, width=35)
lista_tareas.pack(pady=10)

# Botón para marcar tarea como completada
btn_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

# Botón para eliminar tarea
btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()


