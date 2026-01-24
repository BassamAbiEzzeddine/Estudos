termo1 = int(input("Insira o primeiro termo: "))
razao = int(input("Insira a razao: "))
decimo = (termo1 + (10 - 1) * razao) + 1
for c in range(termo1, decimo, razao):
    print("{}".format(c), end=" -> ")
print("Acabou")
