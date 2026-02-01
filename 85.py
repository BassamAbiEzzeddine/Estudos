imparpar = [[], []]
while True:
    num = int(input("Insira um numero: "))
    if num % 2 == 0:
        imparpar[1].append(num)
    else:
        imparpar[0].append(num)

    continuar = " "
    while continuar not in "nNsS":
        continuar = str(input("Deseja continuar S/N: "))
    if continuar in "nN":
        break

print(f"Numeros pares = {sorted(imparpar[1])}")
print(f"Numeros impares = {sorted(imparpar[0])}")
