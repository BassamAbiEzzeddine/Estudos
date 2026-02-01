lista = []
dados = []
cont = 0
maior = []
menor = []
numerico = []
while True:
    # Entrada de dados, Nome e Peso
    dados.append(input("Insira um nome: "))
    dados.append(int(input("Insira o peso: ")))
    lista.append(dados[:])

    # Contador de pessoas
    cont += 1

    # Continue
    continuar = " "
    while continuar not in "nNsS":
        continuar = str(input("Deseja continuar S/N: "))
    if continuar in "nN":
        break

    dados.clear()

# Definir maior e menor peso
for listas in lista:
    numerico.append(listas[1])
maior.append(max(numerico))
menor.append(min(numerico))

# Encontrar quem tem o maior e menor peso
for listas in lista:
    if listas[1] == menor[0]:
        menor.append(listas[0])
    if listas[1] == maior[0]:
        maior.append(listas[0])

print(f"Foram cadastradas {cont} pessoas")
print(f"As pessoas mais pesadas foram {maior[1:]} com o peso de {maior[0]}")
print(f"As pessoas menos pesadas foram {menor[1:]} com o peso de {menor[0]}")
