lista = []
abre = ""
fecha = ""
while True:
    x = str(input("Insira a sua expressao para verificarmos os parenteses: "))
    for letra in x:
        lista.append(letra)
    abre = lista.count("(")
    fecha = lista.count(")")
    if abre == fecha:
        print("Tudo ok na sua formular")
        break
    else:
        print("Tem algo errado ai meu patrao")
        break
