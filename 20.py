from random import sample

a1 = input("insira o nome do aluno 1: ")
a2 = input("insira o nome do aluno 2: ")
a3 = input("insira o nome do aluno 3: ")
a4 = input("insira o nome do aluno 4: ")
r = sample([a1, a2, a3, a4], k=4)
print("A ordem da apresentacao e {}".format(r))
