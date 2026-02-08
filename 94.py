dados={}
listadedados=[]
mulheres=[]
totaldepessoas=0
mediadeidades=0
idadeacimadamedia=[]
while True:
    dados['nome']=str(input('Insira o nome da pessoa: '))
    dados['sexo']=' '
    while dados['sexo'] not in 'mf':
        dados['sexo']=str(input('Insira o sexo M/F: ')).lower().strip()
    cont=' '
    dados['idade']=int(input('Insira a idade: '))
    listadedados.append(dados.copy())
    totaldepessoas+=1
    while cont not in 'ns':
        cont=str(input('Deseja continuar S/N: ')).lower().strip()
    if cont=='n':
            break
for pessoa in listadedados:
    mediadeidades+=pessoa['idade']
    if pessoa['sexo']=='f':
        mulheres.append(pessoa['nome'])
mediadeidades=mediadeidades/totaldepessoas
for pessoa in listadedados:
    if pessoa['idade']>mediadeidades:
        idadeacimadamedia.append(pessoa['nome'])
print(f'Total de pessoas cadastradas {totaldepessoas}')
print(f'Media de idade {mediadeidades}')
print(f'{mulheres}')
print(f'Pessoas com idade acima da media: {idadeacimadamedia}')



    
    
    
        