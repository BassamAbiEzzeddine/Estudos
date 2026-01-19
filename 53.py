frase = str(input("Insira uma frase: ")).strip().upper()
inverso = ""
for i in range(len(frase) - 1, -1, -1):
    inverso = inverso + frase[i]
if inverso == frase:
    print("A frase e um palindromo")
else:
    print("A frase n e um palindromo")
