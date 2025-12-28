cont = 0
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma+i
        cont = cont+1
print(
    f'Valores somados= {soma}\nNumeros impares de 1-500 que tambem sao divisiveis por 3 = {cont}')
