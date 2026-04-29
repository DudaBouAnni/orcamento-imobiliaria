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
        tipo = "Apartamento"
    elif opcao == "2":
        tipo = "Casa"
    elif opcao == "3":
        tipo = "Estúdio"
    else:
        print("Opção invalida!")
        return

    while True:
        parcelas = int(input("Em quantas parcelas deseja pagar (máx 5)? "))
        if parcelas <= 1 or parcelas > 5:
            break
        print("Número de parcelas inválido! Digite um numero entre 1 e 5.")

    imovel = Imovel(tipo)
    contrato = Contrato(parcelas)
    orcamento = Orcamento(imovel, contrato)
    orcamento.gerar_orcamento()

if __name__ == "__main__":
    main()