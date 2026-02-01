x = 0
while True:
    x = int(input("Insira o valor que deseja ver a tabuada: "))
    for i in range(1, 11):
        print(f"{x} x {i} = {x*i}")
    if x < 0:
        break
