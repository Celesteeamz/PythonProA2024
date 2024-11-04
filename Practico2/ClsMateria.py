import sqlite3

class Materia:
    def__init__(self, nombre, curso, materia, horario, profesor):
        self.nombre = nombre
        self.curso = curso
        self.horario = horario
        self.profesor = profesor

    def guardar(self):
        con = sqlite3.connect('escolar2.db')
        c = conn.cursor()
        c = execute('INSERT INTO ClsMateria (nombre, curso, horario, profesor) VALUES (?, ?, ?)',
                    (self.nombre, self.curso, self.horario, self.profesor))

        conn.commit()
        conn.close()
    
    @staticmethod
    def obtener_materias():
        conn = sqlite3.connect('escolar2.db')
        c = conn.cursor()

        c.execute('SELECT * FROM Materias')

        materias = c.fetchall()
        conn.close()

        return materias