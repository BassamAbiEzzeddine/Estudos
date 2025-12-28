from abc import abstractmethod, ABC


class Converter(ABC):

    def dec_to(self, x):
        sinal = ""
        if x < 0:
            sinal = "-"
            x = -x
        if x == 0:
            return "Numero = 0"
        radix = ""
        while x > 0:
            constant = self.get_constant()
            radix = str(self.get_calculation(x)) + radix
            x //= constant
        return sinal + radix

    @abstractmethod
    def get_constant(self): ...

    @abstractmethod
    def get_calculation(self, x):
        return x % self.get_constant()


class BinConverter(Converter):

    def get_constant(self):
        return 2


class OctalConverter(Converter):

    def get_constant(self):
        return 8


class HexConverter(Converter):

    def __init__(self):
        self.numhex = "0123456789ABCDEF"

    def get_constant(self):
        return 16

    def get_calculation(self, x):
        digito = super().get_calculation(x)
        return self.numhex[digito]


mapper = {1: BinConverter, 2: OctalConverter}

while True:
    nm = int(input("Insira o numero a ser convertido: "))
    mtd = int(
        input(
            "Insira para qual linguagem devo converter \n1 = bin \n2 = octal \n3 = hex\nEscolha:  "
        )
    )
    converter = mapper.get(mtd, HexConverter)()
    print(converter.dec_to(nm))
