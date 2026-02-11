from random import randint
from time import sleep


def sortear(a):
    print('Sorteando 5 valores da lista: ',end=' ')
    for i in range(5):
        a.append(randint(1,100))
        print(f'{a[i]}',end=' ',flush=True)
        sleep(0.2)
def somaPar(a):
    som=0
    for num in a:
        if num%2==0:
            som+=num
    print(f'\nSomando os valores pares da lista {a}, temos {som}')
            
            

numeros=[]
sortear(numeros)
somaPar(numeros)
