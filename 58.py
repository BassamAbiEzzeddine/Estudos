from random import randint

maquina = randint(0, 10)
jogador = int(input("Insira um numero de 0 a 10: "))

while maquina != jogador:
    print("O numero escolhido esta incorreto")
    jogador = int(input("Insira outro numero de 0 a 10: "))

if jogador == maquina:
    print("Parabens voce ganhou o numero da maquina era {}".format(maquina))

print("Jogo encerrado")
