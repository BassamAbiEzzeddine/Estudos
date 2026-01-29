lista = []
while True:
    x = int(input("Insira um numero: "))
    lista.append(x)
    y = " "
    while y not in "nNSs":
        y = str(input("Deseja continuar S/N: ")).strip().lower()
    if y in "nN":
        break
print(f"Foram digitados {len(lista)} numeros")
print(sorted(lista, reverse=True))
if 5 in lista:
    print(f"O valor 5 foi digitrado {lista.count(5)} vezes")
else:
    print("O numero 5 nao foi digitado nenhuma vez")
