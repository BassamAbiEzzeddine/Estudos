numero = int(input('Insira o numero que vc quer a tabuada: '))
multiplicador = 0
for i in range(1, 11):
    multiplicador = multiplicador+1
    print('{}x{}={}'.format(numero, multiplicador, numero*multiplicador))
