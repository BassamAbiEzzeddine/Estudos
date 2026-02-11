def contador(inicio,fim,passo):
    if passo<0:
        passo=passo*-1
    if passo==0:
        passo=1
    if inicio>fim:
        print('=='*20)
        print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
        for num in range(inicio,fim+(passo*-1),passo*-1):
            print(num,end=' ')
        print('fim')
        print('=='*20)
    else:
        print('=='*20)
        print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
        for num in range(inicio,fim+passo,passo):
            print(num,end=' ')
        print('fim')
        print('=='*20)

contador(1,10,1)
contador(10,0,2)
print(f'Agora e sua vez, tente voce mesmo: ')
contador(int(input('Insira o valor inicial: ')),int(input('Insira o valor final: ')),int(input('Insira o passo: ')))