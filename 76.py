produtos = (
    "Lapis",
    "1.75",
    "Borracha",
    "2.00",
    "Caderno",
    "15.90",
    "Estojo",
    "25.00",
    "Transferidor",
    "4.20",
    "Compasso",
    "9.99",
    "Mochila",
    "120.32",
    "Canetas",
    "22.30",
    "Livros",
    "34.90",
)
print("-" * 31)
print("LISTAGEM DE PRECOS".center(31))
print("-" * 31)
cont = len(produtos) / 2
produto = 0
valor = 1
while cont != 0:
    print(produtos[produto], end="")
    print("." * (23 - len(produtos[produto])), end="")
    print("R$", end="")
    print(" " * (6 - len(produtos[valor])), end="")
    print(produtos[valor])
    cont -= 1
    produto += 2
    valor += 2
