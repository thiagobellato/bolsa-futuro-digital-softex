from sys import exit

def calcular_imposto(preco):

    valor_imposto = 0.15
    imposto_total = preco * valor_imposto
    print(f"- O Valor a ser pago de impostos é: R${imposto_total:.2F}")
    return imposto_total

estoque_loja = {
    "monitor": {"quantidade": 15, "preco": 850.50},
    "teclado": {"quantidade": 25, "preco": 120.00},
    "mouse": {"quantidade": 30, "preco": 85.00},
}

print("\n       --- ESTOQUE INICIAL ---")
for nome_produto, detalhes_produto in estoque_loja.items():
    print(f"- Produto: {nome_produto.capitalize()} - Quantidade Disponível({detalhes_produto['quantidade']}) - Preço(R$){detalhes_produto['preco']:.2f}")


nome_produto = input("Qual produto deseja comprar:").lower()
if nome_produto not in estoque_loja:
    print("Produto não encontrado")
    exit()

quantidade_digitada = int(input("Qual a quantidade que você deseja comprar:"))
if estoque_loja[nome_produto]["quantidade"] >= quantidade_digitada:
    estoque_loja[nome_produto]["quantidade"] -= quantidade_digitada
    preco_unitario = estoque_loja[nome_produto]["preco"]
    valor_total_venda = quantidade_digitada * preco_unitario
    print("\n       --- RESUMO DA VENDA ---")
    print(f"- Venda de {quantidade_digitada} unidades de {nome_produto.capitalize()} realizada com sucesso.")
    print(f"- Total: R${valor_total_venda:.2f}")
else:
    print("Não há estoque suficiente")
    exit()

print("\n       --- IMPOSTOS ---")
imposto_total = calcular_imposto(valor_total_venda)

print("\n       --- ESTOQUE FINAL ---")
for nome_produto, detalhes_produto in estoque_loja.items():
    print(f"- Produto: {nome_produto.capitalize()} - Quantidade Disponível({detalhes_produto['quantidade']})")

print("\n       --- LUCRO ---")
if 'valor_total_venda' in locals():
    lucro_total = valor_total_venda - imposto_total
    print(f"- O lucro foi de R${lucro_total:.2f}")