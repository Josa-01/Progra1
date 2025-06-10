import random

class ClaseSecreta:
    def __init__(self):
        self.tabla1 = []
        self.tabla2 = []
        self.crear_tablas()

    def crear_tablas(self):
        self.tabla1 = random.sample(range(1, 21), 5)
        self.tabla2 = random.sample(range(1, 21), 5)

    def mostrar_tablas(self):
        print("\nTabla 1:", self.tabla1)
        print("Tabla 2:", self.tabla2)