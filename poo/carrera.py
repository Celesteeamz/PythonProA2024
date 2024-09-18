from Personaje_class import Personaje

menu =  '''
        #############################
        | 1. Agregar personajes     |
        | 2. Personajes             |   
        ############################# 
'''

cantidadPersonaje = 0
nuevo_personaje = []
personajes = []

while True:
    print(menu)
    opcion = int(input("Ingresa la opcion: "))

    if  opcion == 1 :
        nombre = (input("Ingresar nombre: "))
        altura = int(input("Ingresar altura: "))
        velocidad = int(input("Ingresar velocidad: "))
        resistencia = int(input("Ingresar resistencia: "))
        fuerza = int(input("Ingresar fuerza: "))

        nuevo_personaje = Personaje (nombre, altura, velocidad, resistencia, fuerza)
        personajes.append(nuevo_personaje)

        cantidadPersonaje += 1
        print(f"el personaje {nuevo_personaje.nombre} se ha creado")
        print(f"Cantidad de personajes: {cantidadPersonaje}")

elif opcion == 2:
    if cantidadPersonaje == 0:
            print("No hay personajes")
    else:
        print("Con los siguientes personajes se iniciara la carrera ")
        for personaje in personajes:
            print(f"- {personaje.nombre}")

    continue

elif opcion == 3:
     print("Esta opcion no existe")
     break
