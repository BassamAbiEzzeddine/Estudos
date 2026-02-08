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
print('=-'*20)
print(dados)
print('=-'*20)
print(f'O campo nome tem o valor {dados["nomedojogador"]}')
print(f'O campo gols tem o valor {dados["gols"]}')
print(f'O total de gols foi {dados["total"]}')
print('=-'*20)
print(f'O jogador {dados["nomedojogador"]} jogol {dados["partidas"]} partidas no total')
for i in range(len(dados['gols'])):
    print(f'   =>  Na partida {i+1}, fez {dados["gols"][i]} gols')
print(f'Foram feitos um total de {dados["total"]} gols')

    

