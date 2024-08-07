num=[]
for i in range(10):
    numer=int(input("ingresar 10 numeros: "))
    if numer %2==0 and numer != 0:
        num.append(numer)
print(num)