from random import randint
jogos={}
for i in range(4):
    x=randint(1,6)
    print(f'Jogador {i+1} tirou {x} ')
    jogos[f'Jogador {i+1}']=x
jogos=dict(sorted(jogos.items(),key=lambda item:item[1],reverse=True))
pos=1
for k,v in jogos.items():
    print(f'{pos} colocado foi o {k} com o valor {v}')
    pos=pos+1