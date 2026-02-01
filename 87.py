matriz = [[], [], []]
pares=0
soma3coluna=0  

#abrimos a matriz em linhas e colunas definindo o tamanho da matriz em 3x3
for linha in range(3):
    for coluna in range(3):
        
        
#input de numeros na matriz
        num=int(input(f'Insira um numero para a posicao {linha}:{coluna}: '))
        matriz[linha].append(num)
        
        
#soma dos numeros pares
        if num%2==0:
            pares=+num
            
            
#soma dos numeros da 3 coluna
for matrizes in matriz:
    for pos,num in enumerate(matrizes):
        if pos==2:
            soma3coluna+=num
            
            
#maior numero na segunda linha
maior2linha=max(matriz[1])

 
for matriz in matriz:
    print(matriz)
print(f'A soma dos numeros pares = {pares}')
print(f'A soma da 3 coluna e = {soma3coluna}')
print(f'O maior numero da 3 linha e = {maior2linha}')