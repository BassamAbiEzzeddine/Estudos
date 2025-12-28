nota=float(input('Insira a nota do seu aluno: '))
if nota>=5 and nota<=6.9:
    print('Seu aluno esta de recuperacao')
elif nota<5:
    print('Seu aluno esta repovado')
else:
    print('Seu aluno esta aprovado')