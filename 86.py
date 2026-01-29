matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        num=int(input(f'Insira um numero para a posicao {coluna}:{linha}: '))
        matriz[linha].append(num)
        
for matriz in matriz:
    print(matriz)