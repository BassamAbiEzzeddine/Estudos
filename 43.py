peso = float(input("Insira seu Peso: "))
altura = float(input("Insira sua Altura"))
imc = peso / (pow(altura, 2))

if peso <= 0 or altura <= 0:
    print("Os valores devem ser diferentes de 0")
elif imc < 18.5:
    print("Abaixo do Peso")
elif imc >= 18.5 and imc <= 25:
    print("Peso ideal")
elif imc >= 25 and imc <= 30:
    print("Sobrepeso")
elif imc >= 30 and imc <= 40:
    print("Obesidade")
elif imc > 40:
    print("Obesidade morbida")
