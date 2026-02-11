from time import sleep

def maior(a):
    if a==[]:
        print('-='*20)
        print('Analisando os valores passados...')
        for num in a:
            print(f'{num}',end=' ',flush=True)
            sleep(0.2)
        print(f'Foram importados {0} valores ao todo')
        print(f'O maior valor foi 0')
    else:
        print('-='*20)
        print('Analisando os valores passados...')
        for num in a:
            print(f'{num}',end=' ',flush=True)
            sleep(0.2)
        print(f'Foram importados {len(a)} valores ao todo')
        print(f'O maior valor foi {max(a)}')
    
    
    
maior([2,9,4,5,7,1])
maior([4,7,0])
maior([6])
maior([])