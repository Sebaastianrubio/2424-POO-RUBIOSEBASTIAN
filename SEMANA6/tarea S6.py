# Definición de clase base
class Animal:
    # Constructor
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo encapsulado
        self.__edad = edad      # Atributo encapsulado

    # Método para obtener el nombre
    def obtener_nombre(self):
        return self.__nombre

    # Método para obtener la edad
    def obtener_edad(self):
        return self.__edad

    # Método para hacer sonido (a ser sobrescrito en subclases)
    def hacer_sonido(self):
        pass

# Definición de clase derivada
class Perro(Animal):
    # Constructor
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.__raza = raza              # Atributo encapsulado

    # Método para obtener la raza
    def obtener_raza(self):
        return self.__raza

    # Sobrescribir el método hacer_sonido
    def hacer_sonido(self):
        return "Guau"

# Definición de otra clase derivada
class Gato(Animal):
    # Constructor
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.__color = color            # Atributo encapsulado

    # Método para obtener el color
    def obtener_color(self):
        return self.__color

    # Sobrescribir el método hacer_sonido
    def hacer_sonido(self):
        return "Miau"

# Crear objetos de las clases
perro = Perro("Firulais", 5, "Labrador")
gato = Gato("Whiskers", 3, "Blanco")

# Mostrar información y sonidos
print(f"El perro se llama {perro.obtener_nombre()}, tiene {perro.obtener_edad()} años, es de raza {perro.obtener_raza()} y hace '{perro.hacer_sonido()}'")
print(f"El gato se llama {gato.obtener_nombre()}, tiene {gato.obtener_edad()} años, es de color {gato.obtener_color()} y hace '{gato.hacer_sonido()}'")

# Polimorfismo en acción
animales = [perro, gato]
for animal in animales:
    print(f"El animal {animal.obtener_nombre()} hace '{animal.hacer_sonido()}'")