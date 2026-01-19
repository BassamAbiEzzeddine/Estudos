first_number = int(input("Insira o primeiro numero = "))
second_number = int(input("Insira o segundo numero ="))

if first_number > second_number:
    print("O numero {} e maior que {}".format(first_number, second_number))
elif second_number > first_number:
    print("O numero {} e maior que {}".format(second_number, first_number))
else:
    print("Os numeros sao iguais {}={}".format(first_number, second_number))
