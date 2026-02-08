matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        num=int(input(f'Insira um numero para a posicao {linha}:{coluna}: '))
        matriz[linha].append(num)
        
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^8}]',end=' ')
    print()