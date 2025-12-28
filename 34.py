sl=int(input('Insira seu salario : '))
if sl >= 1250:
    print('Seu novo salario e = {}'.format(sl+(sl*(10/100))))
else:
    print('Seu novo salario e = {}'.format(sl+(sl*(15/100))))
    