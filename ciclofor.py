contra= input("ingresar la contraseña")
listaa=[]

for i in contra:
    i="*"
    print (i, end="")
    listaa.append(i)
print()
print(listaa)
listaa.pop(2)
print(listaa)