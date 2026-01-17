sexo=input('Insira o seu sexo, digite apenas M para masculino e F para feminino: ').lower()

while sexo!='m' and sexo!='f':
    sexo=input('Digite apenas M para masculino e F para feminino: ').lower()
print('Seu sexo e {}'.format(sexo))