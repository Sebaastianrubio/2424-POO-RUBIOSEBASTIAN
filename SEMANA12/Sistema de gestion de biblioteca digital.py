class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', id_usuario='{self.id_usuario}', libros_prestados={self.libros_prestados})"


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.ids_usuarios = set()

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN '{libro.isbn}' ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro '{eliminado.titulo}' eliminado de la biblioteca.")
        else:
            print(f"No se encontró un libro con ISBN '{isbn}'.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado con ID '{usuario.id_usuario}'.")
        else:
            print(f"El ID de usuario '{usuario.id_usuario}' ya está en uso.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            eliminado = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario '{eliminado.nombre}' dado de baja.")
        else:
            print(f"No se encontró un usuario con ID '{id_usuario}'.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.ids_usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")
        else:
            print(f"Préstamo no disponible: Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.ids_usuarios:
            usuario = self.usuarios[id_usuario]
            libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
            if libro:
                usuario.devolver_libro(libro)
                self.libros[isbn] = libro
                print(f"Libro '{libro.titulo}' devuelto por '{usuario.nombre}'.")
            else:
                print(f"El usuario '{usuario.nombre}' no tiene el libro con ISBN '{isbn}'.")
        else:
            print(f"No se encontró un usuario con ID '{id_usuario}'.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if (titulo and titulo.lower() in libro.titulo.lower()) or \
                    (autor and autor.lower() in libro.autor.lower()) or \
                    (categoria and categoria.lower() in libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.libros_prestados
        else:
            print(f"No se encontró un usuario con ID '{id_usuario}'.")
            return []


# Ejemplo de uso
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("1984", "George Orwell", "Distopía", "1234567890")
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Realismo Mágico", "0987654321")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Crear usuario
usuario1 = Usuario("Juan Pérez", "U001")

# Registrar usuario
biblioteca.registrar_usuario(usuario1)

# Prestar un libro
biblioteca.prestar_libro("U001", "1234567890")

# Listar libros prestados por el usuario
print(biblioteca.listar_libros_prestados("U001"))

# Devolver un libro
biblioteca.devolver_libro("U001", "1234567890")

# Buscar libros por autor
resultados_busqueda = biblioteca.buscar_libro(autor="Orwell")
print(resultados_busqueda)