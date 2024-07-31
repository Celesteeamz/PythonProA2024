vocalesFrase=input("ingresar una frase: ")
contador=0
vocales="aeiouAEIOU"
for i in vocalesFrase:
    if i in "aeiouAEIOU":
        contador = contador +1
print(f"La cantidad de vocales ingresadas son {contador}")