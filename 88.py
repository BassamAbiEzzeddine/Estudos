from random import randint
games=[]
#definimos a quantidade de jogos
quantidadedejogos=int(input('Insira a quantidade de jogos que deja jogar: '))
for jogos in range(0,quantidadedejogos):
    games.append([])
    for i in range(6):
        games[jogos].append(randint(1,60))

for lista in games:
    print(lista)
     