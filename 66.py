soma = 0
contador = 0
numero = int(input("Insira um numero para ser somado: "))
while True:
    if numero == 999:
        break
    soma += numero
    contador += 1
    numero = int(
        input("Insira outro para ser somado, caso queira que pare digite 999: ")
    )
print("A quantidade de numeros digitados foi {}".format(contador))
print("Sua soma e igual a {}".format(soma))
