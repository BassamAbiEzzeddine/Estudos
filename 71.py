notasde50 = 0
notasde20 = 0
notasde10 = 0
notasde1 = 0
resto = 0

while True:
    saque = float(input("Insira o valor a ser sacado: "))
    if saque >= 50:
        notasde50 = saque // 50
        resto = saque % 50
    if resto >= 20:
        notasde20 = resto // 20
        resto = resto % 20
    if resto >= 10:
        notasde10 = resto // 10
        resto = resto % 10
    if resto >= 1:
        notasde1 = resto // 1
        resto = resto % 1
    if resto < 1:
        break
print(
    f"\n{notasde50} Notas de 50\n\n{notasde20} Notas de 20\n\n{notasde10} Notas de 10\n\n{notasde1} Notas de 1\n\nSobraram {resto} reais na sua conta"
)
