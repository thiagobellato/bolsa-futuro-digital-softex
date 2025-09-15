nome_cliente = "João"
email_cliente = "joao@Gmail.cOm"

novo_nome = nome_cliente.replace("João", "João da Silva")
print(novo_nome)

novo_nome = novo_nome.replace("da Silva", "dos Santos")
print(novo_nome)

nome_completo = "thiagO belLato"

print(nome_completo.capitalize())  # 1ª Letra Maiuscula
print(nome_completo.title())  # 1ª Letra de Cada Palavra Maiuscula

# Posicao Arroba (Pegar servidor emial)
posicao_arroba = email_cliente.find("@") + 1
servidor = email_cliente[posicao_arroba:]
print(servidor.lower())

posicao_espaco = nome_completo.find(" ")
nome = nome_completo[:posicao_espaco]
sobrenome = nome_completo[posicao_espaco + 1 :]
print(nome.capitalize())
print(sobrenome.capitalize())