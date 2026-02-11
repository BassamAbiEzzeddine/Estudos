def escreva(a):
    print(f'~'*(len(a)+2))
    print(f'{a:^{len(a)+2}}')
    print('~'*(len(a)+2))
    
    
texto=str(input('Insira o texto:'))
escreva(texto)