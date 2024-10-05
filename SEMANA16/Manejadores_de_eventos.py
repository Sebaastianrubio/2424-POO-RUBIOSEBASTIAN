import tkinter as tk
from tkinter import messagebox

# Funciones
def agregar_tarea():
    tarea = entry.get()
    if tarea != "":
        listbox.insert(tk.END, tarea)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede agregar una tarea vacía.")

def marcar_completada():
    try:
        indice = listbox.curselection()[0]
        tarea = listbox.get(indice)
        listbox.delete(indice)
        listbox.insert(tk.END, f"{tarea} (Completada)")
    except:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def eliminar_tarea():
    try:
        indice = listbox.curselection()[0]
        listbox.delete(indice)
    except:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def cerrar_app(event=None):
    ventana.quit()

# Interfaz gráfica (GUI)
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Campo de entrada
entry = tk.Entry(ventana, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# Botón para agregar tareas
btn_agregar = tk.Button(ventana, text="Agregar tarea", width=20, command=agregar_tarea)
btn_agregar.grid(row=0, column=1, padx=10, pady=10)

# Lista de tareas
listbox = tk.Listbox(ventana, width=50, height=10)
listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para marcar tareas como completadas
btn_completar = tk.Button(ventana, text="Marcar como completada", width=20, command=marcar_completada)
btn_completar.grid(row=2, column=0, padx=10, pady=10)

# Botón para eliminar tareas
btn_eliminar = tk.Button(ventana, text="Eliminar tarea", width=20, command=eliminar_tarea)
btn_eliminar.grid(row=2, column=1, padx=10, pady=10)

# Atajos de teclado
ventana.bind('<Return>', lambda event: agregar_tarea())  # Agregar tarea con Enter
ventana.bind('<Delete>', lambda event: eliminar_tarea()) # Eliminar tarea con Supr
ventana.bind('<Control-c>', lambda event: marcar_completada()) # Marcar como completada con Ctrl + C
ventana.bind('c', lambda event: marcar_completada())  # Marcar como completada con tecla 'C'
ventana.bind('d', lambda event: eliminar_tarea())     # Eliminar tarea con tecla 'D'
ventana.bind('<Escape>', cerrar_app)  # Cerrar aplicación con tecla Escape

# Iniciar la aplicación
ventana.mainloop()