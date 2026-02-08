temp={}
dados=[]
#criar o dicionario e adicionar os dados
while True:
    temp['aluno']=str(input('Insira o nome do aluno: '))
    temp['media']=float(input('Insira a media do aluno: '))
#identificar o resultado final do aluno e retornar se foi aprovado ou reprovado
    if temp['media']>7:
        temp['resultado']='Aprovado'
    else:
        temp['resultado']='Reprovado'
    dados.append(temp.copy())
#continue
    resp=' '
    while resp not in 'sn':
        resp=str(input('Deseja continuar? ')).strip().lower()
    if resp=='n':
        break
#dar print nos dados em forma de tabela
print(f'-='*18)
print(f'{'Nome':<20}{'Media':<6}{'Resultado':<10}')
print(f'-='*18)
for alunos in dados:
    print(f'{alunos["aluno"]:<20}{alunos['media']:<6}{alunos['resultado']:<10}')
print(f'-='*18)