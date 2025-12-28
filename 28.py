from random import randint

x = randint(0,5)
y = int(input('Insira um numero de 0 a 5: '))
if y==x:
    print('Voce ganhou')
else:
    print('Voce perdeu o numero era = {}'.format(x))