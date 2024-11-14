import sqlite3
from ClsEstudiante import estudiante
from ClsCalificacion import calificacion
from ClsMateria import materia 
from ClsProfesor import profesor

def conectar_db():
    conn = sqlite3.connect('escolar3.db')
    return conn

def mine():
    conn = conectar_db()
    cursor = conn.cursor()

    menuDos = '''
            -----------------------------
            | 1. Estudiante.            |
            | 2. Profesor.              |
            | 3. Materia.               |
            | 4. Calificacion.          |
            -----------------------------
    '''

    menuTres = '''
            -----------------------------
            | 1. Estudiantes.           |
            | 2. Profesores.            |
            | 3. Materias.              |
            | 4. Calificaciones.        |
            -----------------------------
    '''
    while True:
        print(menuDos)
        opcion = input ("Seleccione la opcion: ")

    if opcionn == 1:
        dni_id = int(input("Ingrese dni del estuiante: "))
        nombre = input("Ingrese solo el nombre del estudiante: ")
        apellido = input("Ingrese el apellido el estudiante: ")
        fecha_nacimiento = int(input("Ingrese la fecha de nacimiento: "))
        curso = int(input("Ingresar curso(1ro,2do,3ro,4to,5to,6to: "))
        email = input("Ingresar email del estudiante o mayor a cargo: ")
        estado = input("'Cursando' o 'No cursando': ")
        continue

    elif opcion == 2:
        dni_id = int(input("Ingrese dni del docente:"))
        nombre = input("Ingrese solo el nombre del profesor: ")
        apellido = input("Ingrese el apellido del docente: ")
        curso = int(input("Ingresar curso(1ro,2do,3ro,4to,5to,6to: "))
        estado = input("'Cursando' o 'No cursando': ")
        email = input("Ingresar email del docente: ")
        estudiante = Estudiante(None, dni_id, nombre, apellido, curso, estado, email))
        estudiante.agregar()
        print("Estudiante agregado.")
        continue

    elif opcion == 3:
        nombre = input("Ingrese nombre de la materia: ")
        curso = int(input("Ingrese curso correspondiente de la materia: "))
        horario = int(input("Ingresar horario de la materia (cuando empieza y termina: "))
        descripcion = input("Ingresar despripción de la materia: ")
        profesor = input("Ingresar nombre de profesor a cargo de la materia: ")

        