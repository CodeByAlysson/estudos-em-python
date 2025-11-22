print("**Bem-Vindo(a) à Copiadora do CodeByAlysson**\n")
print('Os serviços oferecidos por nossa copiadora são: \n')
print('DIG - DIGITAÇÃO')
print('ICO - IMPRESSÃO COLORIDA')
print('IPB - IMPRESSÃO PRETO E BRANCO')
print('FOT - FOTOCOPIA \n')

# Escolha do serviços e preços
def escolha_servico():
    while True:
        servico = input("Escolha o serviço desejado (DIG / ICO / IPB / FOT): ")
        if servico == "DIG":
            return 1.10
        elif servico == "ICO":
            return 1.00
        elif servico == "IPB":
            return 0.40
        elif servico == "FOT":
            return 0.20
        else:
            print("Opção inválida! Escolha novamente o serviço desejado.")

# Quantidade de páginas
def num_pagina():
    while True:
        try:
            paginas = int(input("Digite o número de páginas: "))
            if paginas >= 20000:
                print("Quantidade de páginas excedidas! Máximo permitido: 19999.")
            elif paginas < 0:
                print("Número inválido. Digite um valor positivo.")
            else:
                if paginas < 20:
                    return paginas
                elif paginas < 200:
                    return paginas * 0.85 #desconto de 15%
                elif paginas < 2000:
                    return paginas * 0.80 #desconto de 20%
                else:
                    return paginas * 0.75 #desconto de 25%
        except ValueError:
            print("Por favor, digite um número válido.")

# Adicionando serviço extra e preço
def servico_extra():
    while True:
        adicional = input("Deseja algum serviço adicional?\n 1 - Não desejo serviço extra!\n 2 - Encadernação Simples [R$15]\n 3 - Encadernação Capa Dura [R$40] \n ")
        if adicional == "1":
            return 0.0
        elif adicional == "2":
            return 15.0
        elif adicional == "3":
            return 40.0
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")

# Uso do try/except + resumo da venda e valor total a pagar
try:
    valor_servico = escolha_servico()
    paginas_descontadas = num_pagina()
    valor_adicional = servico_extra()

    total = (valor_servico * paginas_descontadas) + valor_adicional

    print(f"\nResumo do carrinho: \n")
    print(f"Valor por página (com base no serviço): R${valor_servico:.2f}")
    print(f"Número de páginas (com desconto se aplicável): {paginas_descontadas:.2f}")
    print(f"Valor adicional: R${valor_adicional:.2f}")
    print(f"Total a pagar: R${total:.2f}\n")
    print('***A copiadora CodeByAlysson agradece por sua compra. Volte sempre!***')
except Exception as e:
    print("Ocorreu um erro inesperado:", e)
