from app.Contrato import Contrato
import csv

class Orcamento:

    def __init__(self, imovel, contrato):
        self.imovel = imovel
        self.contrato = contrato

    def gerar_orcamento(self):
        aluguel = self.imovel.calcular_aluguel()
        valor_contrato = Contrato.VALOR_CONTRATO
        parcela_contrato = self.contrato.valor_parcela()

        print("\n Orçamento gerado com sucesso!")
        print(f"Tipo de imóvel: {self.imovel.tipo}")
        print(f"Valor do aluguel: R$ {aluguel:.2f}")
        print(f"Valor do contrato: R$ {valor_contrato:.2f}")
        print(f"Parcelas do contrato: {self.contrato.parcelas}x de R$ {parcela_contrato:.2f}")

    def gerar_csv(self):
        aluguel = self.imovel.calcular_aluguel()

        with open("parcelas.csv", "w", newline="") as arquivo:
            escritor = csv.writer(arquivo)

            escritor.writerow(["Parcela", "Valor"])

            for mes in range(1, 13):
                escritor.writerow([mes, aluguel])

        print("CSV gerado!")