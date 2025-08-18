import json
from sys import exit
from datetime import datetime

# ---------- CARREGAR DADOS ----------
try:
    with open("dados.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
        usuarios = dados.get("usuarios", [])
        produtos = dados.get("produtos", [])
except (FileNotFoundError, json.JSONDecodeError):
    usuarios = []
    produtos = []

# ---------- MENU DE LOGIN / CADASTRO ----------
while True:
    print("\nDigite uma das opções abaixo:")
    print("1 - Login")
    print("2 - Cadastrar novo usuário")
    opcao = input("Opção: ").strip()

    if opcao == "1":  # LOGIN
        nome_cliente = input("Digite seu nome: ").capitalize()

        # Verifica se o usuário está cadastrado
        encontrado = False
        for usuario in usuarios:
            if usuario["nome"] == nome_cliente:
                encontrado = True
                nascimento = datetime.strptime(usuario["nascimento"], "%d/%m/%Y")
                hoje = datetime.today()
                idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
                break

        if encontrado:
            if idade >= 18:
                print(f"Olá {nome_cliente}, login confirmado! Acesso liberado!!!")
                break  # sai do menu de login e entra no sistema de produtos
            else:
                print(f"Acesso negado! {nome_cliente} é menor de idade ({idade} anos).")
        else:
            print(f"Usuário {nome_cliente} não encontrado. Cadastre-se primeiro.")

    elif opcao == "2":  # CADASTRO
        nome_cliente = input("Digite seu nome: ").capitalize()
        nascimento_str = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()
        try:
            nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y")
        except ValueError:
            print("Formato de data inválido! Use DD/MM/AAAA.")
            continue

        # Adiciona usuário à lista (permitindo qualquer idade)
        usuarios.append({"nome": nome_cliente, "nascimento": nascimento_str})

        # Salva no JSON
        with open("dados.json", "w", encoding="utf-8") as f:
            json.dump({"usuarios": usuarios, "produtos": produtos}, f, ensure_ascii=False, indent=2)

        print(f"Usuário {nome_cliente} cadastrado com sucesso! Faça login para continuar.")

    else:
        print("Opção inválida! Digite 1 ou 2.")

# ---------- LOOP DO MENU DE PRODUTOS ----------
while True:
    print("\nBem-vindo(a) ao sistema de cadastro de produtos!")
    print("Digite uma das opções abaixo:")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Excluir Produto")
    print("9 - Sair do Sistema")

    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida! Digite um número.")
        continue

    if opcao == 1:
        nome_produto = input("Digite o nome do produto: ").lower()
        try:
            preco_produto = float(input("Digite o preço do produto: "))
        except ValueError:
            print("Preço inválido! Use apenas números.")
            continue

        produtos.append({"nome": nome_produto, "preco": preco_produto})

        # salvar produtos no JSON
        with open("dados.json", "w", encoding="utf-8") as f:
            json.dump({"usuarios": usuarios, "produtos": produtos}, f, ensure_ascii=False, indent=2)

        print(f"Produto {nome_produto} cadastrado com sucesso!")

    elif opcao == 2:
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("\nLista de Produtos")
            for p in produtos:
                print("-", p["nome"].capitalize(), "R$", p["preco"])

    elif opcao == 3:
        nome_produto = input("Digite o nome do produto a ser excluído: ").lower()
        tamanho_antes = len(produtos)
        produtos = [p for p in produtos if p["nome"] != nome_produto]
        tamanho_depois = len(produtos)

        # salvar produtos no JSON
        with open("dados.json", "w", encoding="utf-8") as f:
            json.dump({"usuarios": usuarios, "produtos": produtos}, f, ensure_ascii=False, indent=2)

        if tamanho_depois < tamanho_antes:
            print(f"Produto {nome_produto} excluído com sucesso!")
        else:
            print(f"Produto {nome_produto} não encontrado!")

    elif opcao == 9:
        print("Saindo do sistema...")
        exit()

    else:
        print("Opção inválida!")

    input("\nPressione ENTER para voltar ao menu...")
