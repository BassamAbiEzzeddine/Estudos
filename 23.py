n = input("Digite um numero de ate 4 digitos = ")
lt = list(n)
match len(lt):
    case 0:
        print("Voce nao digitou nada")
    case 1:
        print("Numero digitado contem \n{} Unidades".format(lt[0]))
    case 2:
        print("Numero digitado contem \n{} Dezenas \n{} Unidades".format(lt[0], lt[1]))
    case 3:
        print(
            "Numero digitado contem \n{} Centenas \n{} Dezenas \n{} Unidades".format(
                lt[0], lt[1], lt[2]
            )
        )
    case 4:
        print(
            "Numero digitado contem \n{} Milhar \n{} Centenas \n{} Dezenas \n{} Unidades".format(
                lt[0], lt[1], lt[2], lt[3]
            )
        )
    case _:
        print("Caso nao aceito")
