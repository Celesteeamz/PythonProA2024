import sqlite3
from ClsEstudiante import Estudiante
from ClsCalificacion import Calificacion
from ClsMateria import Materia 
from ClsProfesor import Profesor

def conectar_db():
    conn = sqlite3.connect('escolar.db')
    return conn

def mine():
    conn = conectar_db():
    cursor = conn.cursor()

    menu = '''
        -----------------------------------------------------------------
        | 1. Agregar estudiante, profesor, materia, calificacion.       |
        | 2. Mostrar estudiantes, profesores, materias, calificaciones. |
        | 3. Salir.                                                     |
        -----------------------------------------------------------------
    
    '''
    menuDos = '''
            -----------------------------
            | 1. Estudiante.            |
            | 2. Profesor.              |
            | 3. Materia.               |
            | 4. Calificacion.          |
            -----------------------------
    '''

    while True:
        print(menu)
        opcion = input ("Seleccione la opcion: ")

        if opcionn == 1:
            print(menuDos)
            elif opcionUno == 1:
                nombreEstudiante = input ("Ingrese nombre del estudiante: ")
                apeliidoEstudiante = input ("Ingrese apellido del estudiante: ") 
                dniEstudiante = input ("Ingrese dni del estudiante: ")
                añoEstudiante = input ("Ingresar edad del estudiante: ")
                cursoEstudiante = input ("Ingresar curso del estudiante: ")
                emailEstudiante = input ("Ingresar estado del estudiante: ")
                Estudiante.agregar(conn, nombre, apellido, dni, año, curso, email, estado)

            elif opcionDos == 2:
                nombreProfesor = input ("Ingresar nombre del profesor: ")
                apellidoProfesor

            elif opcionTres == 3:
