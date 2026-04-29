class Contrato:
    VALOR_CONTRATO = 2000.00

    def __init__(self, parcelas):
        self.parcelas = min(parcelas, 5)

    def valor_parcela(self):
        if self.parcelas == 0:
            return 0.00
        return self.VALOR_CONTRATO / self.parcelas
