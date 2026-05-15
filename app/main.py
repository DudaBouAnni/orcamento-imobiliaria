from app.Contrato import Contrato
from app.Imovel import Imovel
from app.Orcamento import Orcamento


def main():
    print("Bem-vindo ao sistema de orçamento da Imobiliária R.M")
    print("Tipos de imóveis disponíveis:")
    print("1 - Apartamento (R$ 700,00)")
    print("2 - Casa (R$ 900,00)")
    print("3 - Estúdio (R$ 1200,00)")

    opcao = input("Escolha o tipo (1/2/3): ")

    if opcao == "1":
        imovel = Imovel("Apartamento")
    elif opcao == "2":
        imovel = Imovel("Casa")
    elif opcao == "3":
        imovel = Imovel("Estúdio")
    else:
        print("Opção invalida!")
        return

    if imovel.tipo in ["Apartamento","Casa"]:

        while True:

            imovel.quartos = int(
                input("Quantos quartos (1 a 2): ")
            )

            if imovel.quartos > 2 or imovel.quartos < 1:
                print("Quantidade inválida!")

            else:
                imovel.quartos = imovel.quartos
                break

            garagem_input = input(
                "Deseja adicionar garagem? (S/N): "
            )

            if garagem_input.upper() == "S":
                imovel.garagem = True

    if imovel.tipo == "Apartamento":

        criancas_input = input(
            "Possui crianças? (S/N): "
        )

        if criancas_input.upper() == "S":
            imovel.criancas = True

    if imovel.tipo == "Estúdio":

        while True:
            imovel.vagas_estudio = int(
                input("Quantos vagas deseja?: ")
            )

            if imovel.vagas_estudio < 0:
                print("Número inválido!")

            else:
                imovel.vagas_estudio = imovel.vagas_estudio
                break

    while True:
        parcelas = int(
            input("Em quantas parcelas deseja pagar (máx 5)? ")
        )
        if 1 <= parcelas <= 5:
            break
        print("Número de parcelas inválido! Digite um numero entre 1 e 5.")

    contrato = Contrato(parcelas)

    orcamento = Orcamento(imovel, contrato)

    orcamento.gerar_orcamento()

    orcamento.gerar_csv()

if __name__ == "__main__":
    main()