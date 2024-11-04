import sqlite3

class Estudiante:
    def__init__(self, legajo_id, dni_id, nombre, apellido, fecha_nacimiento,  curso, email, estado):
        self.legajo_id = legajo_id
        self.dni = dni_id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.curso = curso
        self.email = email
        self.estado = estado

    def guardar(self):
        con = sqlite3.connect('escolar3.db')
        c = conn.cursor()
        c = execute('INSERT INTO ClsEstudiante (legajo_id, dni_id, nombre, apellido, fecha_nacimiento,  curso, email, estado) VALUES (?, ?, ?)',
                    (self.legajo_id, self.dni_id, self.nombre, self.apellido,  self.fecha_ncimiento, self.curso, self.email, self.estado))

        conn.commit()
        conn.close()
    
    @staticmethod
    def obtener_estudiantes():
        conn = sqlite3.connect('escolar3.db')
        c = conn.cursor()

        c.execute('SELECT * FROM estudiantes')

        estudiantes = c.fetchall()
        conn.close()

        return estudiantes