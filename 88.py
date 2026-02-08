from random import randint
games=[]
#definimos a quantidade de jogos
quantidadedejogos=int(input('Insira a quantidade de jogos que deseja jogar: '))
for jogos in range(0,quantidadedejogos):
    games.append([])
    cont=0
    while cont<6:
        num=randint(1,60)
        if num not in games[jogos]:
            games[jogos].append(num)
            cont+=1
for p,lista in enumerate(games):
    print(f'Jogo{p+1}: {lista}')
