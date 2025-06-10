from clase_secreta import ClaseSecreta
from tabla_interceptar import TablaInterceptar

class ControlCentral:
    def __init__(self):
        self.artefactos = ClaseSecreta()
        self.interceptar = TablaInterceptar()
        self.en_operacion = True

    def mostrar_menu(self):
        while self.en_operacion:
            print("\n--- MENU CENTRAL ---")
            print("1. Crear señal")
            print("2. Enviar señal")
            print("3. Ver coincidencias")
            print("4. Reiniciar ")
            print("5. Finalizar ")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.artefactos.crear_tablas()
                print("Nuevos listas generadas ")
                self.artefactos.mostrar_tablas()

            elif opcion == "2":
                codigo = self.interceptar.emitir_senal()
                if codigo is None:
                    print("Todas las señales fueron emitidas!")
                else:
                    print("Señal enviada:", codigo)
                    if self.interceptar.verificar(codigo, self.artefactos):
                        print(">>> Ccoindidencia detectada!")
                    else:
                        print("no coincidencias encontradas.")

            elif opcion == "3":
                self.artefactos.mostrar_tablas()
                self.interceptar.mostrar_senales()

            elif opcion == "4":
                print("Reiniciando misión...")
                self.__init__()

            elif opcion == "5":
                print("Finalizando operación...")
                self.en_operacion = False

            else:
                print("Opción inválida.")