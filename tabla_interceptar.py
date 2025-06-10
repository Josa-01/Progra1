import random

class TablaInterceptar:
    def __init__(self):
        self.senales = []

    def emitir_senal(self):
        disponibles = [i for i in range(1, 21) if i not in self.senales]
        if disponibles:
            nueva = random.choice(disponibles)
            self.senales.append(nueva)
            return nueva
        else:
            return None

    def verificar(self, codigo, artefactos):
        return codigo in artefactos.tabla1 or codigo in artefactos.tabla2

    def mostrar_senales(self):
        print("\nSeñales enviadas:", self.senales)