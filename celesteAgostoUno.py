# calculadora
listaNumeros = []
contador = 0

menu = '''
        #############################
        | 1. Agregar notas          |
        | 2. Calcular               |   
        | 3. Salir                  |
        ############################# '''

print(menu)

while True:
    opcion = int(input("Ingresa la opcion: "))
    if opcion == 1:
        notass = int(input("Ingresar la nota: "))
        if notass > 10:
            print("Error: La nota tiene que ser 10 o menos.")
        else:
            contador = contador + 1
            listaNumeros.append(notass)

    elif opcion == 2:
        if contador == 0:
            print("Error: Ingrese las notas.")
        else:
            resultado = sum(listaNumeros) / contador
            print(f"Resultado es: {resultado}")

    elif opcion < 1 or opcion > 3:
        print("Error")

    elif opcion == 3:
        print("chauuuu")
        break





    