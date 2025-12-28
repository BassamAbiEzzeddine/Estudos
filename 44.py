valordoproduto = float(input("Insira o valor do produto"))
formadepagamento = int(
    input("1 = avista/cheque\n2 = Credito\nInsira a forma de pagamento:")
)

cred = ""

if formadepagamento == 1:
    print(
        "Valor a ser pago = {}".format(
            valordoproduto - (valordoproduto * (10 / 100)))
    )
elif formadepagamento == 2:
    cred = int(input("Insira em quantas vezes sera o parcelamento: "))
    if cred == 1 or cred == 0:
        print(
            "Valor a ser pago = {}".format(
                valordoproduto - (valordoproduto * (5 / 100))
            )
        )
    elif cred == 2:
        print("Valor a ser pago = {}".format(valordoproduto))
    elif cred >= 3:
        print(
            "Valor a ser pago = {}".format(
                valordoproduto + (valordoproduto * (20 / 100))
            )
        )
