#calculadora
listaNumeros = []
def suma(a,b):
    return a + b

def division(a,b):
    if b == 0:
        print ("Error")
    else:
            return a / b

menu =  '''
        #############################
        | 1. Agregar mas notas      |
        | 4. Calcular               |
        ############################# '''

print(menu)

while True:
    opcion = int(input("Ingresa la opcion: "))

    if  opcion == 1 :
        notass =input("Ingresar la nota: ")
        listaNumeros.append(resultado)
    
    elif opcion > 2 :
        print("error")

    elif opcion == 2 :
        resultado = sum /notass
        print(f"Resultado es:", resultado )
        break

    elif opcion > 10:
            print("Error")


    