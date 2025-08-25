# O objetivo é combinar diferentes tópicos como variáveis, listas, dicionários, loops
# (for), condicionais (if/else) e funções (def) para resolver um problema.
# Exercício: Sistema de Controle de Estoque e Vendas
# Você é o responsável pelo sistema de controle de estoque de uma pequena loja de
# eletrônicos. Sua tarefa é criar um programa em Python que ajude a gerenciar o
# estoque, registrar vendas e calcular impostos.
# Instruções:
# 1. Crie um dicionário para o estoque:
# o Crie um dicionário chamado estoque_loja para armazenar os produtos e
# suas respectivas quantidades em estoque.
# o Adicione os seguintes produtos e quantidades iniciais:
# ▪ "monitor": 15
# ▪ "teclado": 25
# ▪ "mouse": 30
# 2. Crie um dicionário de preços:
# o Crie outro dicionário chamado precos_produtos com os mesmos
# produtos e seus preços de venda:
# ▪ "monitor": 850.50
# ▪ "teclado": 120.00
# ▪ "mouse": 85.00
# 3. Implemente a lógica de venda:
# o Use um input() para perguntar ao usuário qual produto ele deseja
# comprar.
# o Converta a entrada do usuário para letras minúsculas (.lower()) para
# garantir que a busca funcione corretamente.
# o Use uma estrutura de if/else para verificar se o produto existe no
# estoque_loja e se há quantidade disponível.

# ▪ Se o produto estiver em estoque:
# ▪ Pergunte ao usuário a quantidade desejada.
# ▪ Verifique se a quantidade solicitada é menor ou igual à
# quantidade em estoque.
# ▪ Se for, atualize o estoque subtraindo a quantidade
# vendida.
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
        f"- {nome_produto.lower()}: R$ {detalhes_produto['quantidade']:.1f} - {detalhes_produto['preço']}"
    )
    
nome_produto = input("Qual produto deseja comprar:").lower()
if nome_produto and "quantidade" in detalhes_produto > 0 in estoque_loja:
    print("Temos")
else:
    print("Não Temos")



