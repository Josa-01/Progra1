import pyodbc #libreria para accesar DBs

servidor = 'DESKTOP-48STGKI'
base_datos = 'Examen2'
tabla = 'palabras'

# conexion
conexion = (
    "DRIVER={SQL Server};"
    "SERVER=" + servidor + ";"
    "DATABASE=" + base_datos + ";"
    "Trusted_Connection=yes;"
)

conexion_db = pyodbc.connect(conexion)
cursor = conexion_db.cursor()

consulta = "SELECT * FROM " + tabla
cursor.execute(consulta)

print("Registros encontrados en la tabla:")
for fila in cursor.fetchall():
    print(fila)

# Cerrar conexión
conexion_db.close()
