valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))
conta = 0


while conta != 5:
    conta = int(
        input(
            "Escolha oque sera feito a seguir \n1 = soma\n2 = multiplicacão\n3 = maior\n4 = novos numeros\n5 = sair do programa\n"
        )
    )

    if conta == 1:
        print("\nO resultado da soma e = {}\n".format(valor1 + valor2))
    elif conta == 2:
        print("\nO resultado da multiplicacao e = {}\n".format(valor1 * valor2))
    elif conta == 3:
        if valor1 > valor2:
            print("\no numero {} e maior que {}\n".format(valor1, valor2))
        if valor2 > valor1:
            print("".format(valor2, valor1))
    elif conta == 4:
        print("\nInsira novos numeros!!!\n")
        valor1 = int(input("Insira o primeiro valor: "))
        valor2 = int(input("Insira o segundo valor: "))

print("!!Programa encerrado!!")
