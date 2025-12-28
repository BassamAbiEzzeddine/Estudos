velho=str('')
maior=0
soma=0
menor=0
for i in range(1,5):
    nome=str(input('Insira o nome da pessoa :'))
    idade=float(input('Insira a idade:'))
    sexo=str(input('Insira o sexo, masculino ou feminino:')).strip().upper()
    soma+=idade
    if idade>maior and sexo=='MASCULINO':
        velho=nome
    if idade<20 and sexo=='FEMININO':
        menor+=1
        
        
print('A medida de idade e {}\nO homem mais velho e {}\nExistem {} mulheres abaixo dos 20 anos'.format(soma/4,velho,menor))
    
    