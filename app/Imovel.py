class Imovel:
    def __init__(self, tipo, quartos = 1, garagem = False, criancas = False, vagas_estudio = 0):
        self.tipo = tipo
        self.quartos = quartos
        self.garagem = garagem
        self.criancas = criancas
        self.vagas_estudio = vagas_estudio

    def calcular_aluguel(self):

        aluguel = 0

        if self.tipo == "Apartamento":
            aluguel = 700.00

            if self.quartos == 2:
                aluguel += 200

            if self.garagem:
                aluguel += 300

            if not self.criancas:
                aluguel *= 0.95

        elif self.tipo == "Casa":
            aluguel = 900.00

            if self.quartos == 2:
                aluguel += 250

            if self.garagem:
                aluguel += 300

        elif self.tipo == "Estúdio":
            aluguel = 1200.00

            if self.vagas_estudio >= 2:
                aluguel += 250
                extras = self.vagas_estudio - 2
                
                if extras > 0:
                    aluguel += extras * 60

        return aluguel