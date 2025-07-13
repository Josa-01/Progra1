import pyodbc

# Funcion para conectar a la base de datos
def conectar():
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-48STGKI;"
        "DATABASE=ParqueoDB;"
        "Trusted_Connection=yes;"
    )
    return conexion
