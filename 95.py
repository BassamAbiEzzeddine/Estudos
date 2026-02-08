jogadores=[]
while True:
    dados={}
    golsporpatida=[]
    totaldegols=0
    dados['nomedojogador']=str(input('Insira o nome do jogador: '))
    dados['partidas']=int(input('Insira a quantidade de partidas que ele jogou: '))
    for i in range(dados['partidas']):
        golsporpatida.append(int(input(f'Quantos gols na partida {i+1}: ')))
    for golsfeitos in (golsporpatida):
        totaldegols+=golsfeitos
    dados['gols']=golsporpatida
    dados['total']=totaldegols
    jogadores.append(dados.copy())
    cont=' '
    while cont not in 'ns':
        cont=str(input('Deseja continuar S/N: ')).lower().strip()
    if cont=='n':
            break   
print('=-'*20)
print(f'{'cod':<5}',end='')
print(f'{'nome':<10}',end='')
print(f'{'gols':<20}',end='')
print(f'{'total':<5}')
print('--'*20)
for pos,jogador in enumerate(jogadores):
    print(f'{pos:<5}',end='')
    print(f"{jogador['nomedojogador']:<10}",end='')
    print(f"{str(jogador['gols']):<20}",end='')
    print(f"{jogador['total']:<5}")
print('--'*20)
verjogador=0    
while verjogador!=999:
        verjogador=int(input('Mostrar dados de qual jogado?  '))
        print('--'*20)
        for pos,jogador in enumerate(jogadores):
            if pos==verjogador:
                print(f'-- Levantamento do jogador {jogador['nomedojogador']}:')
                for i in range(len(jogador['gols'])):
                    print(f'   =>  Na partida {i+1}, fez {jogador["gols"][i]} gols')

