numero = int(input("Insira o numero para achar seu fatorial: "))
multiplos = numero
fatorial = 1
while multiplos > 0:
    print("{}".format(multiplos), end=" ")
    if multiplos > 1:
        print("x", end=" ")
    else:
        print("=", end=" ")
    fatorial *= multiplos
    multiplos -= 1
print("{}".format(fatorial))
