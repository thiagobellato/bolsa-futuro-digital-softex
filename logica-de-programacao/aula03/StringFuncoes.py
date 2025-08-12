nomeCliente = "João"
emailCliente = "joao@Gmail.cOm"

print(emailCliente)

# manipulação de str (maiusculo)
emailCliente = emailCliente.upper()
print(emailCliente)

# manipulação de str (minusculo)
emailCliente = emailCliente.lower()
print(emailCliente)

# find (posição de um caracter específico)
print(emailCliente.find("@"))  # -1 quando não encontrado

# tamanho
print(len(emailCliente))
print(len(nomeCliente))

# pegar um caracter
print((emailCliente[0]))
print((nomeCliente[0]))

# pegar um caracter do final para o incio
print((emailCliente[-1]))
print((nomeCliente[-1]))

# solicitar informação a partir de um ponto
print((emailCliente[:5]))
print((nomeCliente[:3]))

# solicitar informação a partir de um ponto até um outro ponto
print((emailCliente[1:5]))
print((nomeCliente[1:3]))

# replace (substitui uma informação dentro da string)
novoEmail = emailCliente.replace("gmail.com", "hotmail.com")
print(novoEmail)
