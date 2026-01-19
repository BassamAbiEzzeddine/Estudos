menor = 1000
maior = 0
for i in range(1, 6):
    peso = float(input("Insira o peso: "))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print("Maior peso = {}\nMenor peso = {}".format(maior, menor))
