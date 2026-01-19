primeirotermo = int(input("Insira o primeiro termo da sua PA: "))
razao = int(input("Insira a razao da sua PA: "))
termos = 10
contas = primeirotermo
while termos != 0:
    print(contas, end=" ")
    contas = contas + razao
    termos = termos - 1
