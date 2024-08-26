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
        self.archivos="inventario.txt"
        self.cargar_inventario()
    def _cargar_inventario__(self):
   def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado al inventario.")

    def actualizar_producto(self, codigo, nueva_cantidad, nuevo_precio):
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.cantidad = nueva_cantidad
                producto.precio = nuevo_precio
                print(f"Producto {producto.nombre} actualizado.")
                return
        print("Producto no encontrado.")

    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                self.productos.remove(producto)
                print(f"Producto {producto.nombre} eliminado del inventario.")
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