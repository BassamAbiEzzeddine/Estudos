a=int(input('Digite a reta 1: '))
b=int(input('Digite a reta 2: '))
c=int(input('Digite a reta 3: '))

if a<b+c and b<a+c and c<a+b:
    print('O triangulo e possivel')
else:
    print('O triangulo nao sera formado com essas 3 retas')