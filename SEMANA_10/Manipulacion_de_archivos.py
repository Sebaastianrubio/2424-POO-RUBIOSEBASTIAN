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
        self.productos = {}
        self.archivo = "inventario.txt"
        self._cargar_inventario()

    def _cargar_inventario(self):
        """Carga el inventario desde el archivo al iniciar el sistema."""
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    codigo, nombre, cantidad, precio = linea.strip().split(", ")
                    self.productos[int(codigo)] = Producto(int(codigo), nombre, int(cantidad), float(precio))
        except FileNotFoundError:
            # Si el archivo no existe, se crea uno nuevo.
            with open(self.archivo, 'w'):
                pass

    def _guardar_inventario(self):
        """Guarda el inventario actual en el archivo."""
        with open(self.archivo, 'w') as file:
            for producto in self.productos.values():
                file.write(f"{producto.codigo}, {producto.nombre}, {producto.cantidad}, {producto.precio}\n")

    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print(f"Error: Ya existe un producto con el código {producto.codigo}.")
        else:
            self.productos[producto.codigo] = producto
            print(f"Producto {producto.nombre} agregado al inventario.")
            self._guardar_inventario()

    def actualizar_producto(self, codigo, nueva_cantidad=None, nuevo_precio=None):
        if codigo in self.productos:
            producto = self.productos[codigo]
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            print(f"Producto {producto.nombre} actualizado.")
            self._guardar_inventario()
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            producto = self.productos.pop(codigo)
            print(f"Producto {producto.nombre} eliminado del inventario.")
            self._guardar_inventario()
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        productos_encontrados = [producto for producto in self.productos.values() if producto.nombre.lower() == nombre.lower()]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def ver_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
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
inventario.actualizar_producto(1, nueva_cantidad=8, nuevo_precio=750)

# Ver inventario actualizado
print("\nInventario actualizado:")
inventario.ver_inventario()

# Buscar producto por nombre
print("\nBuscar productos por nombre:")
inventario.buscar_por_nombre("Mouse")

# Eliminar un producto
inventario.eliminar_producto(2)

# Ver inventario después de la eliminación
print("\nInventario después de la eliminación:")
inventario.ver_inventario()