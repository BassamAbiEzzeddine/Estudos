from random import choice
from os import system

while True:

    jogador = (
        input(str("Pedra\nPapel\nTesoura\nInsira qual sera sua jogada: "))
        .lower()
        .strip()
    )

    opcoes = ["pedra", "papel", "tesoura"]
    maquina = choice(opcoes)

    print("A maquina escolheu {}".format(maquina))

    if maquina == jogador:
        print("Foi empate tente novamente")
    elif (
        jogador == "pedra"
        and maquina == "tesoura"
        or jogador == "papel"
        and maquina == "pedra"
        or jogador == "tesoura"
        and maquina == "papel"
    ):
        print(
            "{} ganha de {} voce venceu.".format(
                jogador.capitalize(), maquina.capitalize()
            )
        )
    else:
        print(
            "{} ganha de {} a maquina venceu, tente novamente".format(
                maquina.capitalize(), jogador.capitalize()
            )
        )
