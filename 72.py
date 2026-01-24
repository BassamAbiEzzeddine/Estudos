numeros = (
    "um",
    "dois",
    "tres",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quize",
    "dezesseis",
    "dezeseete",
    "dezoito",
    "dezenove",
    "vinte",
)
num = int(input("Insira um numero de 1 a 20: "))
while True:
    num = int(input("Tente novamente, Insira um numero de 1 a 20: "))
    if 0 <= num <= 20:
        break
print(numeros[num - 1])
