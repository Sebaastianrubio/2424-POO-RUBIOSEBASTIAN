class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []
        self.archivo = "inventario.txt"
        self._cargar_inventario()

    def _cargar_inventario(self):
        """Carga el inventario desde el archivo al iniciar el sistema."""
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    codigo, nombre, cantidad, precio = linea.strip().split(", ")
                    self.productos.append(Producto(int(codigo), nombre, int(cantidad), float(precio)))
        except FileNotFoundError:
            print(f"Archivo '{self.archivo}' no encontrado. Se creará un nuevo archivo.")
            self._crear_archivo()
        except PermissionError:
            print(f"Error: No se tienen permisos para leer el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def _guardar_inventario(self):
        """Guarda el inventario actual en el archivo."""
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(f"{producto.codigo}, {producto.nombre}, {producto.cantidad}, {producto.precio}\n")
        except PermissionError:
            print(f"Error: No se tienen permisos para escribir en el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def _crear_archivo(self):
        """Crea un nuevo archivo de inventario si no existe."""
        try:
            with open(self.archivo, 'w') as file:
                pass  # Simplemente crea el archivo
            print(f"Archivo '{self.archivo}' creado exitosamente.")
        except PermissionError:
            print(f"Error: No se tienen permisos para crear el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error inesperado al crear el archivo: {e}")

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado al inventario.")
        self._guardar_inventario()

    def actualizar_producto(self, codigo, nueva_cantidad, nuevo_precio):
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.cantidad = nueva_cantidad
                producto.precio = nuevo_precio
                print(f"Producto {producto.nombre} actualizado.")
                self._guardar_inventario()
                return
        print("Producto no encontrado.")

    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                self.productos.remove(producto)
                print(f"Producto {producto.nombre} eliminado del inventario.")
                self._guardar_inventario()
                return
        print("Producto no encontrado.")

    def ver_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


# Uso del sistema de gestión de inventarios
inventario = Inventario()

# Agregar productos
producto1 = Producto(1, "Laptop", 10, 800)
producto2 = Producto(2, "Mouse", 50, 25)
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)

# Ver inventario
print("\nInventario actual:")
inventario.ver_inventario()

# Actualizar un producto
inventario.actualizar_producto(1, 8, 750)

# Ver inventario actualizado
print("\nInventario actualizado:")
inventario.ver_inventario()

# Eliminar un producto
inventario.eliminar_producto(2)

# Ver inventario después de la eliminación
print("\nInventario después de la eliminación:")
inventario.ver_inventario()