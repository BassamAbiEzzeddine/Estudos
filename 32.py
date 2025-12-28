x= int(input('Insira em que ano estamos: '))

if x%4 == 0 and x%100!=0 or x%400 == 0:
    print('Esse ano e bissexto')
else:
    print('Esse ano nao e bissexto')