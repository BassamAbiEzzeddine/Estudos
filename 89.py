nomesenotas=[]
poslista=0
while True:
#dar entrada em nomes e notas na lista
    nomesenotas.append([])
#nome pos(0)
    nomesenotas[poslista].append(str(input('Insira o nome do aluno: ')).lower().strip())
#notas pos(1,2)
    for i in range(2):
        nota=1
        nomesenotas[poslista].append(float(input(f'Insira a nota {nota}: ')))
        nota+=1
#media dos alunos se encontra na pos(3)
    nomesenotas[poslista].append((nomesenotas[poslista][1]+nomesenotas[poslista][2])/2)
    poslista+=1
    cont=' '
    while cont not in ('ns'):
        cont=str(input('Deseja continuar S/N: ')).strip().lower()
    if cont in ('n'):
        break
print(f'{'Tabela de notas':^23}')
print(f'{'Nome':<15}{'Media':<9}')
print('-='*12)
for listas in nomesenotas:
    print(f'{listas[0]:<15}{listas[3]:<8}')
#procurar um aluno
while True:
    alunoprocurado=str(input('\nDeseja ver as notas de algum aluno em especifico?\nDigite o nome dele:')).lower().strip()
    for listas in nomesenotas:
        if listas[0]==alunoprocurado:
            print(f'Nome {listas[0]} Nota 1 = {listas[1]} Nota 2 = {listas[2]}')
    while cont not in ('ns'):
        cont=str(input('Deseja continuar S/N: ')).strip().lower
    if cont in ('n'):
        break
    