lista = []
pares = []
impares = []
while True:
    x = int(input("Insira um numero: "))
    z = " "

    while z not in "nNsS":
        z = str(input("Deseja continuar S/N: "))
    if z in "nN":
        break
    lista.append(x)
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
print(f"Lista com todos os numeros: {sorted(lista)}")
print(f"Lista com os pares: {sorted(pares)}")
print(f"Lista com os numeros impares: {sorted(impares)}")
