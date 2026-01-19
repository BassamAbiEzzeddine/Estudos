from random import randint

maquina = randint(0, 10)
jogador = int(input("Insira um numero de 0 a 10: "))
tentativas = 1
while maquina != jogador:
    if maquina > jogador:
        print("Mais...", end=" ")
    else:
        print("Menos...", end=" ")
    print("O numero escolhido esta incorreto")
    jogador = int(input("Insira outro numero de 0 a 10: "))
    tentativas += 1

if jogador == maquina:
    print(
        "Parabens voce ganhou o numero da maquina era {}\nEm apenas {} tentativas".format(
            maquina, tentativas
        )
    )

print("Jogo encerrado")
