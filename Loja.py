# Mensagem Inicial:
print("Bem-Vindos à loja do CodeByAlysson")

# Valor e quantidade do produto:
valor_do_produto = int(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

# Cálculo do valor total sem desconto
valor_sem_desconto = valor_do_produto * quantidade

# Cálculo do desconto
if valor_sem_desconto < 2500:
    desconto = 0  # 0% de desconto
elif 2500 <= valor_sem_desconto < 6000:
    desconto = 0.04  # 4% de desconto
elif 6000 <= valor_sem_desconto < 10000:
    desconto = 0.07  # 7% de desconto
else:  # valor_sem_desconto >= 10000
    desconto = 0.11  # 11% de desconto

# Cálculo do valor total com desconto
valor_com_desconto = valor_sem_desconto * (1 - desconto)

# Resultados:
print(f"Valor total sem desconto: R$ {valor_sem_desconto:.2f}")
print(f"Valor total com desconto: R$ {valor_com_desconto:.2f}")
print()
print("Obrigado e volte sempre! :)")
