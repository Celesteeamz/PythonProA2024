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
        if opcionUno == 1:
            nombreEstudiante = input ("Ingrese nombre del estudiante: ")
            apeliidoEstudiante = input ("Ingrese apellido del estudiante: ") 
            dniEstudiante = int(input ("Ingrese dni del estudiante: "))
            añoEstudiante = int(input ("Ingresar edad del estudiante: "))
            cursoEstudiante = input ("Ingresar curso del estudiante: ")
            emailEstudiante = input ("Ingresar estado del estudiante: ")
            Estudiante.agregar(conn, nombre, apellido, dni, año, curso, email, estado)

        elif opcionDos == 2:
            nombreProfesor = input ("Ingresar nombre del profesor: ")
            apellidoProfesor = input ("Ingresar nombre del profesor: ")
            dniProfesor = int(input("Ingresar dni del profesor: "))
            cursoProfesor = input ("Ingresar curso del profesor")
            estadoProfesor = input ("Ingresar estado del profesor: ")
            emailProfesor = input ("Ingresar email del profesor: ")
            Profesor.agregar(conn, dni, nombre, apellido, curso, estado, email)

        elif opcionTres == 3:
            nombreMateria = input("Ingresar nombre de la materia:")
            cursoMateria = input("Ingresar curso de la materia: ")
            horarioMateria = input("Ingresar horario de la materia: ")
            profesorMateria = input("Ingrese profesor acargo de esta materia: ")
            Materia.agregar(conn, nombre, curso, horario, profesor)
        
        elif opcionCuatro == 4:
            cursoCalificacion = input("Ingresar curso ")
