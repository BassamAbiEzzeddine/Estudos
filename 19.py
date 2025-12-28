from random import choice

a1 = input("insira o nome do aluno 1: ")
a2 = input("insira o nome do aluno 2: ")
a3 = input("insira o nome do aluno 3: ")
a4 = input("insira o nome do aluno 4: ")
r = choice([a1, a2, a3, a4])
print("O aluno escolhido foi {}".format(r))
