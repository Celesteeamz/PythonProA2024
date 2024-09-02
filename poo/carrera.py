from Personaje_archivo import Personaje
listaPersonajes = []
personaje = 0

menu =  '''
        #############################
        | 1. Agregar personajes     |
        | 2. Personajes             |   
        ############################# '''

print(menu)

while True:
    opcion = int(input("Ingresa la opcion: "))
    if  opcion == 1 :
        personaje = personaje + 1
        personaje = (input("Ingresar nombre: "))
        personaje = (input("Ingresar altura: "))
        listaPersonajes.append(personaje)

    if opcion == 2
        print(f"Personajes: {listaPersonajes}" )
        break

p1 = Personaje("batman", 100, 80, 90, 70)
print (f"el personaje se llama {p1.nombre}")