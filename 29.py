km= int(input('Insira sua velocidade = '))
kv= (km-80)*7
if km<=80:
    print('Voce esta dentro do limite de velocidade')
else:
    print('Voce foi multado no valor de {}'.format(kv))