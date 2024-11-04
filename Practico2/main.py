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

    menuTres = '''
            -----------------------------
            | 1. Estudiantes.           |
            | 2. Profesores.            |
            | 3. Materias.              |
            | 4. Calificaciones.        |
            -----------------------------
    '''
    while True:
        print(menu)
        opcion = input ("Seleccione la opcion: ")

    if opcionn == 1:
        print(menuDos)
        
        if opcion == 1:
            nombre = input ("Ingrese nombre del estudiante: ")
            apeliido = input ("Ingrese apellido del estudiante: ") 
            dni = int(input ("Ingrese dni del estudiante: "))
            anho = int(input ("Ingresar edad del estudiante: "))
            curso = input ("Ingresar curso del estudiante: ")
            email = input ("Ingresar estado del estudiante: ")
            #estudiantes.guardar(conn, nombre, apellido, dni, anho, curso, email, estado)
            #print("1.Si   2.No")
            contestar = input("Luis")
            
            #    if opcion == 1:
            #        print(menu)
                
            #    if opcion == 2:
            #        continue

        elif opcion == 2:
            nombre = input ("Ingresar nombre del profesor: ")
            apellido = input ("Ingresar nombre del profesor: ")
            dni = int(input("Ingresar dni del profesor: "))
            curso = input ("Ingresar curso del profesor")
            estado = input ("Ingresar estado del profesor: ")
            email = input ("Ingresar email del profesor: ")
            profesores.agregar(conn, dni, nombre, apellido, curso, estado, email)

        elif opcion == 3:
            nombre = input("Ingresar nombre de la materia:")
            curso = input("Ingresar curso de la materia: ")
            horario = int(input("Ingresar horario de la materia: "))
            profesor = input("Ingrese profesor acargo de esta materia: ")
            materias.agregar(conn, nombre, curso, horario, profesor)

        elif opcion == 4:
            curso = input("Ingresar curso: ")
            materia = input("Ingresar materia: ")
            calificacion = int(input("Ingresar calificacion del estudiante:"))
            estudiante = input ("Ingresar estudiante: ")
            fecha = int(input("Ingresar fecha de la calificacion: "))

            calificaciones.agregar(conn, curso, materia, calificacion, estudiante, fecha)

    elif opcion == 2:
        print(menuTres)

        if opcion == 1:
            estudiantes.mostrar_todos(conn)

        elif opcion == 2:
            profesores.mostrar_todos(conn)

        elif opcion == 3:
            materias.mostrar_todos(conn)

        elif opcion == 4:
            calificaciones.mostrar_todos(conn)

    elif opcion == 3:
        print("chau")
    break
