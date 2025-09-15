nome_cliente = "João"
email_cliente = "jOAo@GmAiL.cOm"

# printa o email original da variável
print(email_cliente)

# manipulação de str
email_cliente = email_cliente.upper()  # maiúsculo
print(email_cliente)

email_cliente = email_cliente.lower()  # minúsculo
print(email_cliente)

print(email_cliente.upper())  # apenas printa sem alterar a variável (maiúsculo)

print(email_cliente.lower())  # apenas printa sem alterar a variável (minúsculo)


# find (posição de um caracter específico)
print(email_cliente.find("@"))  # -1 quando não encontrado

# tamanho
print(len(email_cliente))
print(len(nome_cliente))


# pegar um caracter
print((email_cliente[0]))
print((nome_cliente[0]))

# pegar um caracter do final para o incio
print((email_cliente[-1]))
print((nome_cliente[-1]))

# solicitar informação a partir de um ponto
print((email_cliente[:5]))
print((nome_cliente[:3]))

# solicitar informação a partir de um ponto até um outro ponto
print((email_cliente[1:5]))
print((nome_cliente[1:3]))

# replace (substitui uma informação dentro da string)
novo_email = email_cliente.replace("gmail.com", "hotmail.com")
print(novo_email)

nome_cliente = nome_cliente.replace("João", "Thiago")  # substitui "ão" por "a"
print(nome_cliente)

print(nome_cliente)
