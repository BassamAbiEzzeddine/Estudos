numero=int(input('Insira um numero para ser somado: '))
soma=0
soma+=numero
contador=0
while numero!=999:
    numero=int(input('Insira outro para ser somado, caso queira que pare digite 999: '))
    soma+=numero
    contador+=1
soma=soma-999
print('A quantidade de numeros digitados foi {}'.format(contador))
print('Sua soma e igual a {}'.format(soma))