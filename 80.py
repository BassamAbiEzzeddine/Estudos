lista = [int(input("Insira um numero:"))]
print("Numero adicionado na posisao 1")
while True:
    x = int(input("Insira um numero:"))
    for pos, num in enumerate(lista):
        if num > x:
            lista.insert(pos, x)
            print(f"Numero adicionado na posicao {pos+1}")
            break
    else:
        lista.append(x)
        print("Numero adicionado no fim da lista")

    if len(lista) == 5:
        break
print(lista)
