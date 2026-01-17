numero=int(input('Insira o numero para achar seu fatorial: '))
multiplos=numero-1
conta=0
while multiplos!=0:
    conta=numero*multiplos
    numero=conta
    multiplos=multiplos-1
print('O resultado e {}'.format(numero))