maiorque18 = 0
homens = 0
mulheresmenosde20 = 0
while True:
    sexo = " "
    cont = " "
    idade = int(input("Insira a idade: "))
    while sexo not in "mfMF":
        sexo = str(input("Insira o sexo M/F: ")).lower().strip()[0]
    if idade > 18:
        maiorque18 += 1
    if sexo == "m":
        homens += 1
    if sexo == "f" and idade < 20:
        mulheresmenosde20 += 1
    while cont not in "snSN":
        cont = str(input("Deseja continuar S/N: ")).lower().strip()[0]
    if cont == "n":
        break
print(
    f"Existem {maiorque18} com mais de 18 anos\nExistem {homens} homens cadastrados\nExistem {mulheresmenosde20} mulheres com menos de 20 anos "
)
