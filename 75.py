tru = (
    int(input("Insira o primeiro numero: ")),
    int(input("Insira o segundo numero: ")),
    int(input("Insira o terceiro numero: ")),
    int(input("Insira o quarto numero: ")),
)


cont9 = tru.count(9)
par = ()
pares = 0

print(f"O numero 9 apareceu {cont9} vezes")
if 3 in tru:
    print(f"O numero 3 foi digitado na {tru.index(3)+1} posicao")
else:
    print("O numero 3 nao foi diitado")
pares == len(par)
if pares == 1:
    print(f"O numero par digitado foi {par[0]}")
elif pares > 1:
    print(f"Os numero pares digitados foram {par}")
else:
    print("Nenhum numero par foi digitado")
