palavras = (
    "aprender",
    "amigo",
    "jogar",
    "curso",
    "guanabara",
    "estudos",
    "pratica",
    "trabalhar",
    "mercado",
    "futuro",
)
cont = 10
pos = 0
vogais = "aeiou"
while cont > 0:
    memoria = ()
    palavra = palavras[pos]
    splitado = list(palavra)
    for letra in splitado:
        if letra in vogais:
            if (
                letra == "a"
                or letra == "e"
                or letra == "i"
                or letra == "o"
                or letra == "u"
            ):
                memoria = memoria + (letra,)

    print(f"A palavra {palavras[pos]} contem as seguintes vogais {memoria}")
    pos += 1
    cont -= 1
