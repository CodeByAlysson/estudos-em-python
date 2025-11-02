# Neste exercício vou te explicar como usar o loop while em Python.

while True:
    nome = input("Digite o nome correto para acessar o sistema: ")

    if nome == "CodeByAlysson":
        print("Acesso permitido. Bem-vindo, CodeByAlysson ! ✅")
        break
    else:
        print("Nome incorreto. Tente novamente ou caia fora ! ❌.")