lista = []
while True:
    x = int(input("Insira um numero a ser adicionado digite 999 caso queira parar: "))
    if x not in lista:
        lista.append(x)
    else:
        print("O numero digitado ja se encontra na lista")
    if x == 999:
        break
print(f"Sua lista foi {lista}")
print(f"A lita em ordem crescente e {sorted(lista)}")
