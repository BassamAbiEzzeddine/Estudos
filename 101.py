def voto(anodenascimento):
    from datetime import datetime
    idade=datetime.now().year-anodenascimento
    if 16>idade<18:
        return 'Opicional'
    elif idade<16:
        return 'Negado'
    else:
        return 'Obrigatorio'
    
anodenascimento=int(input('Insira seu ano de nascimento: '))
print(f'Seu voto sera {voto(anodenascimento)}')