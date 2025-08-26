# 4. Crie uma função para calcular impostos:
# o Use o conceito de def para criar uma função chamada
# calcular_imposto(preco).
# o Esta função deve receber o preco de um produto como parâmetro.
# o A função deve retornar o valor do imposto, que é de 15% sobre o preco.
# o No final da sua lógica de venda, adicione uma linha para calcular e exibir
# o valor do imposto sobre a venda total.
# 5. Exiba o estoque final e o lucro total:
# o Após a execução da lógica de venda, use um for loop para percorrer o
# dicionário estoque_loja e imprimir o estoque atual de cada produto.
# o Calcule o lucro total com a venda realizada (Venda Total - Imposto Total).
# o Imprima o valor do lucro total.


def calcular_imposto(preco):

    imposto = 0.15
    valor_total_venda = preco * imposto
    print(valor_total_venda)


estoque_loja = {
    "monitor": {"quantidade": 15, "preco": 850.50},
    "teclado": {"quantidade": 25, "preco": 120.00},
    "mouse": {"quantidade": 30, "preco": 85.00},
}

for nome_produto, detalhes_produto in estoque_loja.items():
    print(
        f"- {nome_produto.capitalize()}: {detalhes_produto['quantidade']} - {detalhes_produto['preco']}"
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

for preco in estoque_loja:
    imposto = calcular_imposto(preco)
    print(calcular_imposto)
