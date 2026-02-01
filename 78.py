lista = [
    int(input("Insira o primeiro numero: ")),
    int(input("Insira o segundo numero: ")),
    int(input("Insira o terceiro numero: ")),
    int(input("Insira o quarto numero: ")),
    int(input("Insira o quinto numero: ")),
]
print("-=" * 20)
print(f"Voce digitou os valores {lista}")
print(
    f"O maior numero foi {max(lista)} na posicao {lista.index(max(lista))+1}... \nO menor numero foi {min(lista)}  na posicao {lista.index(min(lista))+1}..."
)
