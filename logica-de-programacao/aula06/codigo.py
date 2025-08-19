dic_produtos = {
    "airpod": {"preco": 2000.0, "tamanho": "único"},
    "ipad": {"preco": 9000.0, "tamanho": "11 polegadas"},
    "iphone": {"preco": 6000.0, "tamanho": "6,1 polegadas"},
    "macbook": {"preco": 9000.0, "tamanho": "13 polegadas"},
}

# 1. Imprime os produtos existentes
print("Produtos existentes:")
for nome_produto, detalhes_produto in dic_produtos.items():
    print(
        f"- {nome_produto.capitalize()}: R$ {detalhes_produto['preco']:.1f} - {detalhes_produto['tamanho']}"
    )

nome_produto = input("\nDigite o nome do produto: ").lower()
preco_produto = float(input("Digite o preço do produto: "))
tamanho_produto = input("Digite a quantidade de armazenamento do produto: ")

# 3. Adiciona o novo produto com preço e tamanho
# O valor do item no dicionário principal é um novo dicionário com 'preco' e 'tamanho'
dic_produtos[nome_produto] = {"preco": preco_produto, "tamanho": tamanho_produto}

# 4. Aumenta o preço de todos os produtos em 10%
# Agora iteramos sobre os valores (os dicionários internos)
for detalhes_produto in dic_produtos.values():
    detalhes_produto[
        "preco"
    ] *= 1.1  # O atalho *= faz a mesma coisa que 'detalhes['preco'] = detalhes['preco'] * 1.1'

# 5. Imprime o dicionário final com formatação
print("\n---")
print("Preços ajustados (aumento de 10%):")
for nome_produto, detalhes_produto in dic_produtos.items():
    print(
        f"- {nome_produto.capitalize()}: R$ {detalhes_produto['preco']:.1f} - {detalhes_produto['tamanho']}"
    )
