from Personaje_class import Personaje

menu =  '''
        #############################
        | 1. Agregar personajes     |
        | 2. Personajes             |
        | 3. Iniciar la carrera     |   
        ############################# 
 '''

cantidadPersonaje = 0
nuevo_personaje = []
personajes = []
danhoo = []

while True:
        print(menu)
        opcion = int(input("Ingresa la opcion: "))

        if  opcion == 1:
                nombre = (input("Ingresar nombre: "))
                altura = int(input("Ingresar altura 40/200: "))
                velocidad = int(input("Ingresar velocidad 50/100: "))
                resistencia = int(input("Ingresar resistencia 0/20: "))
                fuerza = int(input("Ingresar fuerza 0/10: "))
                #cantidadPersonaje.append(nombre)

                nuevo_personaje = Personaje (nombre, altura, velocidad, resistencia, fuerza)
                personajes.append(nuevo_personaje)
                cantidadPersonaje = cantidadPersonaje + 1
                print(f"el personaje {nuevo_personaje.nombre} se ha creado")
                print(f"Cantidad de personajes: {cantidadPersonaje}")

        elif opcion == 2:
                if cantidadPersonaje == 0:
                        print("No hay personajes")

                else:
                        print("Con los siguientes personajes se iniciara la carrera ") 
                        for personaje in personajes: 
                             print(f"- {personaje_nuevo}")
                print("salga de la carrera e ingrese otro numero de fuerza mayor a 0: ")
