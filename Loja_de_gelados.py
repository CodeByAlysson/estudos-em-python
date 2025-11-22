print('Bem-Vindos à Loja de Gelados do CodeByAlysson')
car = '-' * 21 + 'Cardápio' + '-' * 21
l1 = '-' * 50  # linha 1 abaixo do cardápio
print(car)
print(l1)

#Menu/Sabores e Tamanhos/Preços (do t_p1 ao t_p3)

m = '-' * 3 + '|' '  Tamanho  ' '|'  '  Cupuaçú (CP)  ' '|'   '  Açaí (AC)  ' '|' + '-' * 3
t_p1 = '-' * 3 + '|' + ' ' * 5 + 'P' + ' ' * 5 + '|' + ' ' * 5 + 'R$ 6,00' + ' ' * 4 + '|' + ' ' * 3 + 'R$ 10,00' + ' ' * 2 + '|' + '-' * 3
t_p2 = '-' * 3 + '|' + ' ' * 5 + 'M' + ' ' * 5 + '|' + ' ' * 5 + 'R$ 12,00' + ' ' * 3 + '|' + ' ' * 3 + 'R$ 14,00' + ' ' * 2 + '|' + '-' * 3
t_p3 = '-' * 3 + '|' + ' ' * 5 + 'G' + ' ' * 5 + '|' + ' ' * 5 + 'R$ 16,00' + ' ' * 3 + '|' + ' ' * 3 + 'R$ 18,00' + ' ' * 2 + '|' + '-' * 3
print(m)
print(t_p1)
print(t_p2)
print(t_p3)

l2 = '-' * 50
print(l2)  #linha 2 fechando o cardápio

#Preços de acordo com o Tamanho e Sabor
preco = {
    'CP': {'P': 6, 'M': 12, 'G': 16},
    'AC': {'P': 10, 'M': 14, 'G': 18}
}

#Acumulador de pedidos com sabores e tamanhos
total = 0.0
while True:
    sabor = input("Escolha o sabor desejado (CP: CUPUAÇÚ / AC: AÇAÍ): ")
    if sabor not in ['CP', 'AC']:
        print("Sabor inválido. Tente novamente!")
        continue

    tamanho = 'P','M','G'

    tamanho = input("Digite o tamanho desejado (P, M ou G): ")
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente!")
        continue

    if sabor == 'CP':
        if tamanho == 'P':
            preco = 6
        elif tamanho == 'M':
            preco = 12
        else:
            preco = 16
    elif sabor == 'AC':
        if tamanho == 'P':
            preco = 10
        elif tamanho == 'M':
            preco = 14
        else:
            preco = 18

    total += preco
    print(f"Você escolheu: {sabor} tamanho {tamanho} - R${preco:.2f}")

    continuar = input("Deseja pedir mais alguma coisa? (S/N): ")
    if continuar != 'S':
        break

# Total a pagar

print(f"\nTotal a pagar: R${total:.2f}")
print("Obrigado pela sua compra!")
print("Volte sempre!")
