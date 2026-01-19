vl = float(input("Qual o valor da sua casa: "))
sl = float(input("Qual seu salario: "))
an = float(input("Em quantos anos sera paga: "))

if (vl / (an * 12)) > sl * (
    30 / 100
):  # se o valor da casa for maior que 30% do valor do salario o imprestimo sera negado
    print("Imprestimo negado")
else:
    print("Imprestimo autorizado o valor mensal e = {:.2f}".format(vl / (an * 12)))
