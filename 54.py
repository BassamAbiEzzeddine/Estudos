from datetime import date

nascimento = 0
idade = 0
menor = 0
maior = 0
for pessoas in range(1, 8):
    nascimento = int(input("Insira o ano de nascimento: "))
    idade = date.today().year - nascimento
    if idade < 21:
        menor += 1
    else:
        maior += 1
print(
    "Pessoas com maioridade = {}\nPessoas que n atigiram a mioridade = {}".format(
        maior, menor
    )
)
