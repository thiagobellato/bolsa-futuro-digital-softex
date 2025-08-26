# 5. Exiba o estoque final e o lucro total:
# o Após a execução da lógica de venda, use um for loop para percorrer o
# dicionário estoque_loja e imprimir o estoque atual de cada produto.
# o Calcule o lucro total com a venda realizada (Venda Total - Imposto Total).
# o Imprima o valor do lucro total.


def calcular_imposto(preco):

    imposto = 0.15
    valor_total_venda = preco * imposto
    print(f"O Valor a ser pago de impostos é: {valor_total_venda}")
    return valor_total_venda


estoque_loja = {
    "monitor": {"quantidade": 15, "preco": 850.50},
    "teclado": {"quantidade": 25, "preco": 120.00},
    "mouse": {"quantidade": 30, "preco": 85.00},
}

for nome_produto, detalhes_produto in estoque_loja.items():
    print(
        f"- Produto:{nome_produto.capitalize()}: Quantidade Disponível:{detalhes_produto['quantidade']} - Preço(R$):{detalhes_produto['preco']:.2f}"
    )

nome_produto = input("Qual produto deseja comprar:").lower()
quantidade_digitada = int(input("Qual a quantidade que você deseja comprar:"))

if nome_produto not in estoque_loja:
    print("Produto Não Encontrado")
elif estoque_loja[nome_produto]["quantidade"] >= quantidade_digitada:
    estoque_loja[nome_produto]["quantidade"] -= quantidade_digitada
    preco_unitario = estoque_loja[nome_produto]["preco"]
    valor_total_venda = quantidade_digitada * preco_unitario
    print(
        f"Venda de {quantidade_digitada} unidades de {nome_produto.capitalize()} realizada com sucesso."
    )
    print(f"Total: R$ {valor_total_venda:.2f}")

else:
    print("Não temos a quantidade desejada em estoque.")

imposto_total = calcular_imposto(valor_total_venda)
print("\n       --- ESTOQUE FINAL ---")
for nome_produto, detalhes_produto in estoque_loja.items():
    print(
        f"- Produto: {nome_produto.capitalize()}: Quantidade Disponível: {detalhes_produto['quantidade']}"
    )

if 'valor_total_venda' in locals():
    lucro_total = valor_total_venda - imposto_total
    print(lucro_total)
