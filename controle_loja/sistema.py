import json
from sys import exit
from datetime import datetime

# ---------- CARREGAR DADOS ----------
try:
    with open("controle_loja/dados.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
        usuarios = dados.get("usuarios", [])
        produtos = dados.get("produtos", [])
except (FileNotFoundError, json.JSONDecodeError):
    usuarios = []
    produtos = []

# ---------- CLASSE LOGIN ----------
class Login:
    @staticmethod
    def cadastro():
        nome_cliente = input("Digite seu nome: ").capitalize()
        nascimento_str = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()
        try:
            cpf_cliente = int(input(f"Digite o seu CPF (apenas números): "))
            nascimento_str_obj = datetime.strptime(nascimento_str, "%d/%m/%Y")
        except ValueError:
            print("Entrada inválida! Verifique o formato da data ou do CPF.")
            return

        usuarios.append(
            {
                "nome": nome_cliente,
                "nascimento": nascimento_str,
                "cpf": str(cpf_cliente),
            }
        )
        with open("dados.json", "w", encoding="utf-8") as f:
            json.dump(
                {"usuarios": usuarios, "produtos": produtos},
                f,
                ensure_ascii=False,
                indent=2,
            )
        print(f"Usuário {nome_cliente} cadastrado com sucesso! Faça login para continuar.")

    @staticmethod
    def login():
        try:
            cpf_cliente = int(input(f"Digite o seu CPF: "))
        except ValueError:
            print("CPF inválido! Digite apenas números.")
            return False

        encontrado = None
        for usuario in usuarios:
            if int(usuario["cpf"]) == cpf_cliente:
                encontrado = usuario
                break

        if encontrado:
            # A data precisa ser convertida de volta para objeto datetime
            nascimento = datetime.strptime(encontrado["nascimento"], "%d/%m/%Y")
            hoje = datetime.today()
            idade = (
                hoje.year
                - nascimento.year
                - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
            )
            
            if idade >= 18:
                print(f"Olá {encontrado['nome']}, login confirmado! Acesso liberado!!!")
                return True # Retorna True se o login for bem-sucedido
            else:
                print(f"Acesso negado! {encontrado['nome']} é menor de idade ({idade} anos).")
                return False # Retorna False se for menor de idade
        else:
            print(f"Usuário não encontrado. Cadastre-se primeiro.")
            return False # Retorna False se o usuário não for encontrado

# ---------- CLASSE CRUD ----------
class Crud:
    @staticmethod
    def cadastrar_produto():
        nome_produto = input("Digite o nome do produto: ").lower()
        try:
            preco_produto = float(input("Digite o preço do produto: "))
            produtos.append({"nome": nome_produto, "preco": preco_produto})
            with open("controle_loja/dados.json", "w", encoding="utf-8") as f:
                json.dump(
                    {"usuarios": usuarios, "produtos": produtos},
                    f,
                    ensure_ascii=False,
                    indent=2,
                )
            print(f"Produto {nome_produto} cadastrado com sucesso!")
        except ValueError:
            print("Preço inválido! Use apenas números.")

    @staticmethod
    def listar_produtos():
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("\nLista de Produtos")
            for p in produtos:
                print("-", p["nome"], "R$", p["preco"])

    @staticmethod
    def excluir_produto():
        nome_produto = input("Digite o nome do produto a ser excluído: ").lower()
        tamanho_antes = len(produtos)
        
        # A lista precisa ser modificada no local, e não reatribuída.
        # Caso contrário, a alteração não afeta a lista global 'produtos'.
        novos_produtos = [p for p in produtos if p["nome"] != nome_produto]
        produtos[:] = novos_produtos # Modifica a lista 'produtos' no local

        tamanho_depois = len(produtos)

        with open("controle_loja/dados.json", "w", encoding="utf-8") as f:
            json.dump(
                {"usuarios": usuarios, "produtos": produtos},
                f,
                ensure_ascii=False,
                indent=2,
            )

        if tamanho_depois < tamanho_antes:
            print(f"Produto {nome_produto} excluído com sucesso!")
        else:
            print(f"Produto {nome_produto} não encontrado!")


# ---------- MENU PRINCIPAL ----------
while True:
    print("\nDigite uma das opções abaixo:")
    print("1 - Login")
    print("2 - Cadastrar novo usuário")
    print("3 - Sair")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        if Login.login():  # Verifica o retorno de login()
            # Se o login for bem-sucedido, entra no menu de produtos
            while True:
                print("\nBem-vindo(a) ao sistema de cadastro de produtos!")
                print("Digite uma das opções abaixo:")
                print("1 - Cadastrar Produto")
                print("2 - Listar Produtos")
                print("3 - Excluir Produto")
                print("9 - Sair do Sistema")

                try:
                    opcao_produtos = int(input("Digite a opção desejada: "))
                except ValueError:
                    print("Opção inválida! Digite um número.")
                    continue

                if opcao_produtos == 1:
                    Crud.cadastrar_produto()
                elif opcao_produtos == 2:
                    Crud.listar_produtos()
                elif opcao_produtos == 3:
                    Crud.excluir_produto()
                elif opcao_produtos == 9:
                    print("Saindo do sistema de produtos...")
                    break # Quebra o loop interno, voltando para o menu de login
                else:
                    print("Opção inválida!")
    
    elif opcao == "2":
        Login.cadastro()
    
    elif opcao == "3":
        print("Encerrando o programa.")
        exit()
    
    else:
        print("Opção inválida! Digite 1, 2 ou 3.")