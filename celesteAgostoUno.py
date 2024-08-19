#calculadora
listaNumeros = []
contador=0

menu =  '''
        #############################
        | 1. Agregar mas notas      |
        | 2. Calcular               |   
        | 3. Salir                  |
        ############################# '''

print(menu)

while True:
    opcion = int(input("Ingresa la opcion: "))
    if  opcion == 1 :
        notass =(int(input("Ingresar la nota: ")
        listaNumeros.append(notass)
        continue

    if opcion == 2 :
        resultado = (notass+0)/contador
        print(f"Resultado es:", resultado )

    elif opcion > 3 :
        print("error")

    elif notass > 11:
        print("Error")

    elif opcion == 3 :
        print("chauuuu" )
    break





    