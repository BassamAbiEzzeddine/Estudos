from random import randint


c = 0
print("-=-" * 20)
print("VAMOS JOGAR PAR OU IMPAR")
print("-=-" * 20)
while True:
    x = randint(1, 5)
    z = str(input("Escolha entre Par ou Impar: ")).lower().split()[0]
    while z not in "pi":
        z = str(input("Digite apenas par ou impar: ")).lower().split()[0]
    y = int(input("Insira um numero de 1 a 5: "))
    while y not in (1, 2, 3, 4, 5):
        y = int(input("Insira apenas numeros de 1 a 5: "))
    par = (x + y) % 2
    if z == "p" and par == 0:
        print(
            f"\nA maquinas escolheu {x} voce escolheu {y} logo o numero e Par\n\nParabens voce venceu"
        )
        c += 1
    if z == "p" and par != 0:
        print(
            f"\nA maquinas escolheu {x} voce escolheu {y} logo o numero e Impar\n\nVoce perdeu"
        )
        break
    if z == "i" and par != 0:
        print(
            f"\nA maquinas escolheu {x} voce escolheu {y} logo o numero e Impar\n\nParabens voce venceu"
        )
        c += 1
    if z == "i" and par == 0:
        print(
            f"\nA maquinas escolheu {x} voce escolheu {y} logo o numero e Par\n\nVoce perdeu"
        )
        break
    print("-=-" * 20)
print(f"\nVoce perdeu apos {c} Vitorias consecutivas")
