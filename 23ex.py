n = input("Digite um numero de ate 4 digitos = ")
lt = list(n)
posicoes = ["Milhar", "Centenas", "Dezenas", "Unidades"]

if len(lt) == 0:
    print("Voce nao digitou nada")
elif len(lt) > 4:
    print("Caso nao aceito")
else:
    print("Numero digitado contem:")
    for i, digito in enumerate(lt):
       print(f"{digito} {posicoes[-len(lt)+i]}")
       