sexo = (
    str(input("Insira o seu sexo, digite apenas M para masculino e F para feminino: "))
    .lower()
    .strip()[0]
)

while sexo != "m" and sexo != "f":
    sexo = (
        str(input("Digite apenas M para masculino e F para feminino: ")).lower().strip()
    )
print("Seu sexo e {}".format(sexo))
