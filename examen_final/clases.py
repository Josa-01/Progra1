import json
import sqlite3
import unicodedata


# Clase 1: json
class LectorJSON:
    def __init__(self, archivo):
        self.__archivo = archivo
        self.__data = None

    def leer(self):
        try:
            with open(self.__archivo, "r", encoding="utf-8") as f:
                self.__data = json.load(f)
            print("Archivo JSON cargado correctamente.")
        except FileNotFoundError:
            raise ValueError("No se encontró el archivo JSON.")

    def mostrar_estudiantes(self):
        if not self.__data:
            raise ValueError("Primero debe cargar el archivo.")
        for est in self.__data["estudiantes"]:
            print(est["nombre"], est["apellido"], est["consecutivo"])

    def buscar(self, nombre):
        if not self.__data:
            raise ValueError("Primero debe cargar el archivo.")
        for est in self.__data["estudiantes"]:
            if nombre.strip().upper() in est["nombre"].upper():
                return est
        raise ValueError("El estudiante no fue encontrado.")


# Clase 2: BD
class BaseDatos:
    def __init__(self, script_sql):
        self.__script_sql = script_sql
        self.__conn = None

    def __normalizar(self, texto):
        """Normaliza texto eliminando caracteres raros y asegurando UTF-8."""
        if texto is None:
            return None
        return unicodedata.normalize("NFC", texto)

    def conectar(self):
        self.__conn = sqlite3.connect(":memory:")
        cursor = self.__conn.cursor()

        with open(self.__script_sql, "r", encoding="latin-1") as f:
            sql_script = f.read()

        sql_script = sql_script.replace("CREATE DATABASE ExamenFinal", "")
        sql_script = sql_script.replace("USE ExamenFinal", "")
        sql_script = sql_script.replace("GO", "")

        cursor.executescript(sql_script)
        self.__conn.commit()
        print("Base de datos creada en memoria.")
        return self.__conn

    def consultar_mensaje(self, pk):
        cursor = self.__conn.cursor()
        cursor.execute("SELECT mensaje, mision_1, mision_2, mision_3 FROM estudiante WHERE id = ?", (pk,))
        fila = cursor.fetchone()
        if fila:
            return tuple(self.__normalizar(campo) for campo in fila)
        return None


# Clase 3: Mision
class Mision:
    def __init__(self, mensaje, m1, m2, m3):
        self.mensaje = mensaje
        self.misiones = [m1, m2, m3]
        self.aplicadas = []

    def resolver(self):
        frase = self.mensaje

        for m in self.misiones:
            if "Eliminar espacios al inicio" in m:
                frase = frase.lstrip()
                self.aplicadas.append("lstrip()")

            if "Reemplazar guiones por espacios" in m:
                frase = frase.replace("-", " ")
                self.aplicadas.append("replace()")

            if "Eliminar caracteres especiales al final" in m:
                frase = frase.rstrip(".*$")
                self.aplicadas.append("rstrip()")

            if "Eliminar caracteres especiales al inicio" in m:
                frase = frase.lstrip("@#$*&")
                self.aplicadas.append("lstrip()")

            if "Capitalizar la primera letra" in m:
                frase = frase.capitalize()
                self.aplicadas.append("capitalize()")

            if "Corregir la capitalización" in m:
                frase = frase.capitalize()
                self.aplicadas.append("capitalize()")

            if "Verificar el punto final" in m:
                if not frase.endswith("."):
                    frase += "."
                self.aplicadas.append("endswith() + concatenación")

        return frase, self.aplicadas


def f(n):
    return (n % 42) + 1


if __name__ == "__main__":
    lector = LectorJSON("archivo1.json")
    lector.leer()
    lector.mostrar_estudiantes()

    try:
        estudiante = lector.buscar("Josafath")
        print("\nEstudiante encontrado:", estudiante)

        consecutivo = estudiante["consecutivo"]
        pk = f(consecutivo)
        print("Consecutivo:", consecutivo, " -> PK en la BD:", pk)
        
        bd = BaseDatos("script1.sql")
        bd.conectar()
        fila = bd.consultar_mensaje(pk)

        if fila:
            mensaje, m1, m2, m3 = fila
            print("\nMensaje original:", mensaje)

            mision = Mision(mensaje, m1, m2, m3)
            frase_final, usadas = mision.resolver()

            print("\nFrase corregida:", frase_final)
        else:
            print("No se encontro ese registro en la BD.")

    except ValueError as e:
        print("Error:", e)
