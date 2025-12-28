dia=int(input('Quantos dias vc ficara com o carro ? '))
km=float(input('Quantos Kms vc rodara com o carro ? '))
d=dia*60
k=km*(15/100)
kd=d+k
print('O valor a ser pago pelo aluguel e R${}'.format(kd))