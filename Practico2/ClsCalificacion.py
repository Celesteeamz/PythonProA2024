import sqlite3

class ClsCalificacion:
    def__init__(self, materia, calificacion, estudiante, curso, fecha):
        self.materia = materia
        self.calificacion = calificacion
        self.estudiante = estudiante
        self.curso = curso
        self.fecha = fecha

    def guardar(self):
        con = sqlite3.connect('escolar2.db')
        c = conn.cursor()
        c = execute('INSERT INTO ClsCalificacion (curso, materia, calificacion, estudiante, fecha) VALUES (?, ?, ?)',
                    (self.curso, self.materia, self.calificacion, self.estudiante, self.fecha))

        conn.commit()
        conn.close()
    
    @staticmethod
    def obtener_calificaciones():
        conn = sqlite3.connect('escolar2.db')
        c = conn.cursor()

        c.execute('SELECT * FROM Calificaciones')

        calificaciones = c.fetchall()
        conn.close()

        return calificaciones