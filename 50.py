soma = 0
impares = 0
for i in range(1, 7):
    num = int(input('Insira um numero:'))
    if num % 2 == 0:
        soma = num+soma
print(soma)
