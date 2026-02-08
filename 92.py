from datetime import date
dados={}
dados['nome']=str(input('Insira seu nome: '))
nascimento=(int(input('Insira seu nome de nascimento: ')))
dados['idade']=(date.today().year)-nascimento
dados['ctps']=int(input('Insira o numero da sua carteira de tabalho, caso nao tenha digite 0:'))
if dados['ctps']!=0:
    dados['contratacao']=int(input('Insira seu ano de contratacao:'))
    dados['salario']=float(input('Insira o seu salario: '))
if dados['ctps']!=0:
    print(f'Nome inserido = {dados['nome']}')
    print(f'Idade = {dados["idade"]}')
    print(f'Numero da ctps = {dados['ctps']}')
    print(f'Seu primeiro salario foi {dados["salario"]}')
    print(f'Voce ira se aposentar com {(dados['contratacao']-nascimento)+35} anos de idade')
    print(dados)
else:
    print(f'Nome inserido = {dados['nome']}')
    print(f'Idade = {dados["idade"]}')
    print(f'Numero da ctps = {dados['ctps']}')
    print(dados)