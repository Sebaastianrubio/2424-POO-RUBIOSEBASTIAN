import json

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        """Convierte el objeto Producto a un diccionario."""
        return {
            'codigo': self.codigo,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio,
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Producto a partir de un diccionario."""
        return Producto(data['codigo'], data['nombre'], data['cantidad'], data['precio'])

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}
        self.archivo = "inventario.json"
        self._cargar_inventario()

    def _cargar_inventario(self):
        """Carga el inventario desde el archivo JSON al iniciar el sistema."""
        try:
            with open(self.archivo, 'r') as file:
                data = json.load(file)
                for codigo, prod_data in data.items():
                    self.productos[int(codigo)] = Producto.from_dict(prod_data)
        except FileNotFoundError:
            print(f"Archivo '{self.archivo}' no encontrado. Se creará un nuevo archivo.")
            self._guardar_inventario()
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON '{self.archivo}'.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def _guardar_inventario(self):
        """Guarda el inventario actual en un archivo JSON."""
        try:
            with open(self.archivo, 'w') as file:
                json.dump({codigo: producto.to_dict() for codigo, producto in self.productos.items()}, file, indent=4)
        except PermissionError:
            print(f"Error: No se tienen permisos para escribir en el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print(f"Error: Ya existe un producto con el código {producto.codigo}.")
        else:
            self.productos[producto.codigo] = producto
            print(f"Producto {producto.nombre} agregado al inventario.")
            self._guardar_inventario()

    def actualizar_producto(self, codigo, nueva_cantidad, nuevo_precio):
        if codigo in self.productos:
            producto = self.productos[codigo]
            producto.cantidad = nueva_cantidad
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
producto3 = Producto (3,"Teclado",23,18)
producto4 = Producto(4,"Parlantes",12,6)
inventario.agregar_producto(producto1)



# Ver inventario
print("\nInventario actual:")
inventario.ver_inventario()

# Actualizar un producto
inventario.actualizar_producto(1, 8, 750)
inventario.actualizar_producto(2,56,70)
inventario.actualizar_producto(3,23,45)
inventario.actualizar_producto(4,55,79)

# Ver inventario actualizado
print("\nInventario actualizado:")
inventario.ver_inventario()

# Buscar productos por nombre
print("\nBuscar productos por nombre:")
inventario.buscar_por_nombre("Teclado")
inventario.buscar_por_nombre("Mouse")
inventario.buscar_por_nombre("CPU")

# Eliminar un producto
inventario.eliminar_producto(0)


# Ver inventario después de la eliminación
print("\nInventario después de la eliminación:")
inventario.ver_inventario()
