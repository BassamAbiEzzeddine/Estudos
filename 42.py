a = int(input("Digite a reta 1: "))
b = int(input("Digite a reta 2: "))
c = int(input("Digite a reta 3: "))

if a < b + c and b < a + c and c < a + b:
    if (a == b) and (b == c):
        print("Seu triangulo e possivel e ele e equilatero")
    if ((a == b) and (b != c)) or ((a == c) and (c != b)) or ((b == c) and (c != a)):
        print("Seu triangulo e possivel e ele e isoseles")
    if (a != b) and (b != c) and (a != c):
        print("Seu triangulo e possivel e ele e escaleno")
else:
    print("O triangulo nao sera formado com essas 3 retas")
