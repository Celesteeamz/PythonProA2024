import sqlite3

class ClsCalificacion:
    def__init__(self, nombre, año, materia, calificacion):
        self.nombre = nombre
        self.año = añ
        self.materia = materia
        self.calificacion = calificacion

    def guardar(self):
        con = sqlite3.connect('escuelaaa.db')
        c = conn.cursor()
        c = execute('INSERT INTO ClsCalificacion (nombre, año, materia, calificacion) VALUES (?, ?, ?)',
                    (self.) )