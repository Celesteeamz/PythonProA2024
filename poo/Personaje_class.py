class Personaje:
    estado = True
    vida = 100

    def__init__(self, nombre, altura, velocidad, recistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self. velocidad = velocidad:
        self.recistencia = recistencia
        self.fuerza = fuerza
        self.estado = Personaje.estado
        self.via = Personaje.vida

    def atacar (self, personaje_nuevo)
        if self.estado:
            danho = self.fuerza - (otro_personaje.resistencia)
            print(f"{self.nombre} ataca a {otro_personaje.nombre} causando {danho} de daño")
            otro_personaje.recibir_danho(danho)
        else:
            print(f"{self.nombre} esta muerto")

    def recibir_danho(self. cantidad):
        if self.estado:
            self.vida = self.vida - cantidad
            print(f"{self.nombre} recibio {cantidad} de daño.")
            if self.vida<=0
                self.vida = 0
                print(f"{self.nombre} ha muerto")
        else:
            print(f"{self.nombre} ya ha muerto")

    def mostrar_info(self):
        print