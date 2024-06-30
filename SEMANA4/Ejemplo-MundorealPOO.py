class Coche:
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El coche {self.marca} {self.modelo} ha sido encendido.")
        else:
            print(f"El coche {self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"El coche {self.marca} {self.modelo} ha sido apagado.")
        else:
            print(f"El coche {self.marca} {self.modelo} ya está apagado.")

    def acelerar(self):
        if self.encendido:
            print(f"El coche {self.marca} {self.modelo} está acelerando.")
        else:
            print(f"El coche {self.marca} {self.modelo} está apagado, no puede acelerar.")

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Color: {self.color}")


# Crear una instancia de la clase Coche
mi_coche = Coche("Toyota", "fortuner", 2020, "Rojo")

# Mostrar información del coche
mi_coche.mostrar_info()

# Encender el coche
mi_coche.encender()

# Acelerar el coche
mi_coche.acelerar()

# Apagar el coche
mi_coche.apagar()
