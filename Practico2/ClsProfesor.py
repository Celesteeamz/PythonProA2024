import sqlite3

class Materia:
    def__init__(self, dni, nombre, apellido, curso, estado, email):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.estado = estado
        self.email = email

    def guardar(self):
        con = sqlite3.connect('escolar2.db')
        c = conn.cursor()
        c = execute('INSERT INTO ClsProfesor (dni, nombre, apellido, curso, estado, email) VALUES (?, ?, ?)',
                    (self.dni, self.nombre, self.apellido, self.curso, self.estado, self.email))

        conn.commit()
        conn.close()
    
    @staticmethod
    def obtener_profesores():
        conn = sqlite3.connect('escolar2.db')
        c = conn.cursor()

        c.execute('SELECT * FROM Profesores')

        materias = c.fetchall()
        conn.close()

        return profesores