from datetime import date

borning_year = int(input("Insira seu ano de nascimento = "))
yearold = date.today().year - borning_year

if yearold < 18:
    print("Voce ainda vai esperar {} anos para se alistar".format(18 - yearold))
elif yearold > 18:
    print("Voce se alistou a {} anos".format(yearold - 18))
else:
    print("Esta na hora de se alistar no exercito")
