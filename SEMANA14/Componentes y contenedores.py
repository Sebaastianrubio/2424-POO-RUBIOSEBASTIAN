import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Lista de eventos
        self.eventos = []

        # Crear la interfaz gráfica
        self.crear_widgets()

    def crear_widgets(self):
        # Etiqueta del título
        self.label_titulo = tk.Label(self.root, text="Agenda Personal", font=("Helvetica", 16))
        self.label_titulo.grid(row=0, column=0, columnspan=4, pady=10)

        # Etiquetas y campos de entrada
        tk.Label(self.root, text="Fecha (DD/MM/YYYY):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_fecha = tk.Entry(self.root)
        self.entry_fecha.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Hora (HH:MM):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_hora = tk.Entry(self.root)
        self.entry_hora.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Descripción:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_descripcion = tk.Entry(self.root, width=40)
        self.entry_descripcion.grid(row=3, column=1, padx=10, pady=5)

        # Botón para agregar evento
        self.btn_agregar = tk.Button(self.root, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=4, column=0, columnspan=2, pady=10)

        # Crear Treeview para mostrar los eventos
        self.tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

        # Botón para eliminar evento
        self.btn_eliminar = tk.Button(self.root, text="Eliminar Evento", command=self.eliminar_evento)
        self.btn_eliminar.grid(row=6, column=0, columnspan=2, pady=10)

    def agregar_evento(self):
        # Obtener los valores de los campos de entrada
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()

        # Validar los datos
        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
            return

        # Agregar evento a la lista de eventos y al Treeview
        self.eventos.append((fecha, hora, descripcion))
        self.actualizar_lista()

        # Limpiar los campos de entrada
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)

        messagebox.showinfo("Éxito", "Evento agregado exitosamente")

    def eliminar_evento(self):
        # Obtener el evento seleccionado en el Treeview
        seleccionado = self.tree.selection()
        if seleccionado:
            evento = self.tree.item(seleccionado, "values")
            respuesta = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el evento: {evento[2]}?")
            if respuesta:
                self.eventos.remove(evento)
                self.actualizar_lista()
                messagebox.showinfo("Éxito", "Evento eliminado exitosamente")
        else:
            messagebox.showwarning("Selección", "Por favor seleccione un evento para eliminar")

    def actualizar_lista(self):
        # Limpiar el Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Agregar eventos al Treeview
        for evento in self.eventos:
            self.tree.insert("", tk.END, values=evento)


# Crear la ventana principal de Tkinter
root = tk.Tk()

# Crear la instancia de la aplicación
app = AgendaApp(root)

# Ejecutar el bucle principal de la aplicación
root.mainloop()