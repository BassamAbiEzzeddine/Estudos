def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado = i*resultado
    return resultado


num = int(input('Insira um numero: '))
numfactorial = factorial(num-1)
if (numfactorial+1) % num == 0:
    print('O numero e primo')
else:
    print('O numero nao e primo')
