from datetime import date

anodenascimento = int(input("Insira seu ano de nascimento: "))
idade = date.today().year - anodenascimento

if idade < 9:
    print("Sua categoria e mirim")
elif idade > 9 and idade <= 14:
    print("Sua categoria e infantil")
elif idade > 14 and idade <= 19:
    print("Sua categoria e jovem")
elif idade > 19 and idade < 20:
    print("Sua categoria e senior")
else:
    print("Sua categoria e master")
