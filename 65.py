inteiro=int(input('Insira um numero: '))
maior=inteiro
menor=inteiro
media=0
contador=0
continuar='s'
while continuar!='n':
    contador+=1
    media+=inteiro
    inteiro=int(input('Insira um numero: '))
    continuar=input('Deseja continuar S/N: ').lower()
    if maior<inteiro:
        maior=inteiro
    elif menor>inteiro:
        menor=inteiro
    if continuar != 'n' and continuar != 's':
        continuar=input('!!!!Digite apenas S ou N!!!!\nDeseja continuar S/N: ').lower()
print('A media de valores = {}'.format(media/contador))
print('Maior valor lido foi {}\nMenor valor lido foi {}'.format(maior,menor))

