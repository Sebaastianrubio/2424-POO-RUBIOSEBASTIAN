class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivo = open(nombre, 'w')
        print(f"Archivo '{self.nombre}' ha sido abierto.")

    def escribir(self, texto):
        self.archivo.write(texto)
        print(f"Escrito en el archivo '{self.nombre}': {texto}")

    def __del__(self):
        self.archivo.close()
        print(f"Archivo '{self.nombre}' ha sido cerrado.")

# Crear un objeto de la clase Archivo
archivo = Archivo('mi_archivo.txt')

# Escribir en el archivo
archivo.escribir('Hola, mundo!\n')

# El objeto `archivo` se elimina y se llama al destructor cuando el script termina o se elimina la referencia
del archivo

# Forzamos la recolección de basura para asegurar que el destructor se llame de inmediato
import gc
gc.collect()