gasto = 0
maisque1000 = 0
barato = " "
valorbarato = 0
contadordeprodutos = 0
while True:
    continuar = " "
    nomedoproduto = str(input("\nInsira o nome do produto: "))
    preco = int(input("\nInsira o Preco do produto: "))
    contadordeprodutos += 1
    gasto += preco
    if preco > 1000:
        maisque1000 += 1
    if contadordeprodutos == 1:
        barato = nomedoproduto
        valorbarato = preco
    if preco < valorbarato:
        valorbarato = preco
        barato = nomedoproduto
    while continuar not in "sSnN":
        continuar = str(input("\nDeseja continuar? S/N: ")).strip().lower()[0]
    if continuar == "n":
        break
print(
    f"Voce gastou no total {gasto} Reais\n\nNo total {maisque1000} produtos custaram mais de 1000 Reais\n\nO produto mais barato foi o/a {barato} saindo pelo valor de {valorbarato} Reais"
)
