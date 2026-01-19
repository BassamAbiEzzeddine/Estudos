valor1 = int(input("Insira o primeiro valor: "))
print("=-" * 10)
valor2 = int(input("Insira o segundo valor: "))
conta = 0


while conta != 5:
    print("=-" * 10)
    conta = int(
        input(
            "Escolha oque sera feito a seguir \n    1 = soma\n    2 = multiplicacão\n    3 = maior\n    4 = novos numeros\n    5 = sair do programa\n>>>>>Qual a sua opcoa: "
        )
    )
    print("=-" * 10)

    if conta == 1:
        print("\nO resultado da soma e = {}\n".format(valor1 + valor2))
    elif conta == 2:
        print("\nO resultado da multiplicacao e = {}\n".format(valor1 * valor2))
    elif conta == 3:
        if valor1 > valor2:
            print("\nO numero {} e maior que {}\n".format(valor1, valor2))
        if valor2 > valor1:
            print("\nO numero {} e maior que {}\n".format(valor2, valor1))
    elif conta == 4:
        print("\nInsira novos numeros!!!\n")
        valor1 = int(input("Insira o primeiro valor: "))
        valor2 = int(input("Insira o segundo valor: "))
    elif conta not in "12345":
        print("Opcao invalida digite novamente")
print("=-" * 10)

print("!!Programa encerrado!!")
