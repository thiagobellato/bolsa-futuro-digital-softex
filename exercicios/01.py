
# ▪ Calcule o valor total da venda (quantidade * preço).
# ▪ Imprima uma mensagem de sucesso, como "Venda de X
# unidades de Y realizada com sucesso. Total: R$ Z".
# ▪ Se não houver quantidade suficiente:
# ▪ Imprima uma mensagem informando que não há estoque
# suficiente.
# ▪ Se o produto não existir:
# ▪ Imprima uma mensagem de erro, como "Produto não
# encontrado.".
# 4. Crie uma função para calcular impostos:
# o Use o conceito de def para criar uma função chamada
# calcular_imposto(preco).
# o Esta função deve receber o preço de um produto como parâmetro.
# o A função deve retornar o valor do imposto, que é de 15% sobre o preço.
# o No final da sua lógica de venda, adicione uma linha para calcular e exibir
# o valor do imposto sobre a venda total.
# 5. Exiba o estoque final e o lucro total:
# o Após a execução da lógica de venda, use um for loop para percorrer o
# dicionário estoque_loja e imprimir o estoque atual de cada produto.
# o Calcule o lucro total com a venda realizada (Venda Total - Imposto Total).
# o Imprima o valor do lucro total.

estoque_loja = {
    "monitor": {"quantidade": 15, "preço": 850.50},
    "teclado": {"quantidade": 25, "preço": 120.00},
    "mouse": {"quantidade": 30, "preço": 85.00},
}

for nome_produto, detalhes_produto in estoque_loja.items():
    print(
        f"- {nome_produto.capitalize()}: {detalhes_produto['quantidade']} - {detalhes_produto['preço']}"
    )

nome_produto = input("Qual produto deseja comprar:").lower()
quantidade_digitada = int(input("Qual a quantidade que você deseja comprar:"))

if nome_produto not in estoque_loja:
    print("Produto Não Encontrado")
elif estoque_loja[nome_produto]['quantidade'] >= quantidade_digitada:
    estoque_loja[nome_produto]['quantidade'] -= quantidade_digitada
    for nome_produto, detalhes_produto in estoque_loja.items():
        print(
            f"- {nome_produto.capitalize()}: {detalhes_produto['quantidade']} - {detalhes_produto['preço']}"
        )
    print(f"Venda realizada de R$ {quantidade_digitada*detalhes_produto['preço']}")
else:
    print("Não temos a quantidade desejada em estoque.")
    
    
# def calcular_imposto()

