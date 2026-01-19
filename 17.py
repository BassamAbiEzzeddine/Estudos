from math import hypot

a = float(input("Insira o valor do cateto oposto: "))
b = float(input("Insira o valor do cateto adjacente: "))
h = hypot(a, b)
print("O valor da hipotenusa e igual a {}".format(h))
