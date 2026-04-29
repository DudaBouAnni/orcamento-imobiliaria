class Imovel:
    def __init__(self, tipo, quartos = 1):
        self.tipo = tipo
        self.quartos = quartos

    def calcular_aluguel(self):
        if self.tipo == "Apartamento":
            return 700.00
        elif self.tipo == "Casa":
            return 900.00
        elif self.tipo == "Estudio":
            return 1200.00
        else:
            return 0