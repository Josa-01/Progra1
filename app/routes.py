from flask import Blueprint, render_template, request, redirect
from .database import conectar

routes = Blueprint('routes', __name__)

@routes.route('/')
def inicio():
    return redirect('/registrar')

@routes.route('/registrar', methods=['GET', 'POST'])
def registrar():
    mensaje = ""
    total_espacios = 10
    espacios_disponibles = 0

    conexion = conectar()
    cursor = conexion.cursor()

    # Ver cuántos espacios ya están ocupados
    cursor.execute("SELECT COUNT(*) FROM Reservaciones WHERE hora_salida IS NULL")
    ocupados = cursor.fetchone()[0]
    espacios_disponibles = total_espacios - ocupados

    if request.method == 'POST':
        if espacios_disponibles <= 0:
            mensaje = "No hay espacios disponibles en el parqueo 😢"
        else:
            # Obtener datos del formulario
            cedula = request.form['cedula']
            nombre = request.form['nombre']
            telefono = request.form['telefono']
            direccion = request.form['direccion']
            placa = request.form['placa']
            marca = request.form['marca']
            modelo = request.form['modelo']

            # Insertar persona
            cursor.execute("""
                INSERT INTO Personas (cedula, nombre, telefono, direccion)
                VALUES (?, ?, ?, ?)
            """, (cedula, nombre, telefono, direccion))
            conexion.commit()

            cursor.execute("SELECT @@IDENTITY")
            persona_id = cursor.fetchone()[0]

            # Insertar vehículo
            cursor.execute("""
                INSERT INTO Vehiculos (placa, marca, modelo, propietario)
                VALUES (?, ?, ?, ?)
            """, (placa, marca, modelo, persona_id))
            conexion.commit()

            cursor.execute("SELECT @@IDENTITY")
            vehiculo_id = cursor.fetchone()[0]

            # Revisar espacios disponibles
            cursor.execute("SELECT espacio FROM Reservaciones WHERE hora_salida IS NULL")
            espacios_ocupados = [fila[0] for fila in cursor.fetchall()]

            # Generar lista de todos los espacios
            todos_los_espacios = [f"A{i+1}" for i in range(total_espacios)]
            libres = list(set(todos_los_espacios) - set(espacios_ocupados))
            libres.sort()

            espacio_asignado = libres[0]

            # Guardar la reservación
            cursor.execute("""
                INSERT INTO Reservaciones (vehiculo_id, hora_entrada, espacio)
                VALUES (?, GETDATE(), ?)
            """, (vehiculo_id, espacio_asignado))
            conexion.commit()

            # Recalcular espacios
            cursor.execute("SELECT COUNT(*) FROM Reservaciones WHERE hora_salida IS NULL")
            ocupados = cursor.fetchone()[0]
            espacios_disponibles = total_espacios - ocupados

            mensaje = f"Registro completado. Se te asignó el espacio: {espacio_asignado} ✅"

    conexion.close()
    return render_template("registrar.html", mensaje=mensaje, disponibles=espacios_disponibles)
