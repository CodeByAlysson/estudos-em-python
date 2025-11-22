print('***Bem-Vindos à Livraria do CodeByAlysson***')
l1 = '-' * 45  # linha 1 abaixo da mensagem inicial
m = '-' * 15 + ' MENU PRNCIPAL ' + '-' * 15
print(l1)
print(m)

# Lista vazia para armazenar livros e variável de controle de ID
lista_livro = []
id_global = 0

# Função Cadastrar Livro
def cadastrar_livro(id):
    l1 = '-' * 45  # linha 1 acima de CADASTRAR LIVRO
    m = '-' * 15 + ' CADASTRAR LIVRO ' + '-' * 13
    print(l1)
    print(m)
    print(f"\nCadastro de Livro - ID: {id}")
    nome = input("Informe o nome do livro: ")
    autor = input("Informe o autor do livro: ")
    editora = input("Informe a editora do livro: ")

    livro = {
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }

    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!\n")

# Função para consultar livros
def consultar_livro():
    l2 = '-' * 45  # linha 1 acima de CONSULTAR LIVRO
    m = '-' * 15 + ' CONSULTAR LIVRO ' + '-' * 13
    print(l2)
    print(m)
    while True:
        print("\nConsulta de Livros")
        print("1. Consultar Todos os Livros")
        print("2. Consultar Livros por Id")
        print("3. Consultar Livros por Autor")
        print("4. Retornar ao Menu!")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Lista de Todos os Livros ---")
            for livro in lista_livro:
                print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
        elif opcao == "2":
            try:
                id_consulta = int(input("Digite o ID do livro: "))
                encontrado = False
                for livro in lista_livro:
                    if livro['id'] == id_consulta:
                        print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                        encontrado = True
                if not encontrado:
                    print("Livro não encontrado.")
            except ValueError:
                print("ID inválido. Digite um número inteiro.")
        elif opcao == "3":
            autor_consulta = input("Digite o nome do autor: ")
            encontrados = [livro for livro in lista_livro if livro['autor'] == autor_consulta]
            if encontrados:
                for livro in encontrados:
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
            else:
                print("Nenhum livro encontrado para este autor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para remover livro
def remover_livro():
    l3 = '-' * 45  # linha 1 acima de CADASTRAR LIVRO
    m = '-' * 15 + ' REMOVER LIVRO ' + '-' * 15
    print(l3)
    print(m)
    while True:
        try:
            id_remover = int(input("Digite o ID do livro a ser removido: "))
            for livro in lista_livro:
                if livro['id'] == id_remover:
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!")
                    return
            print("Id inválido. Tente novamente.")
        except ValueError:
            print("ID inválido. Digite um número inteiro.")

# Menu Principal (fora de função)
while True:
    print("\n**Menu Principal**\n")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif escolha == "2":
        consultar_livro()
    elif escolha == "3":
        remover_livro()
    elif escolha == "4":
        print("Programa encerrado. Volte sempre!")
        break
    else:
        print("Opção inválida. Tente novamente!")
