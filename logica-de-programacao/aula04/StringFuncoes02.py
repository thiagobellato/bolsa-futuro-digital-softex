nomeCliente = "João"
emailCliente = "joao@Gmail.cOm"


novoNome = nomeCliente.replace("João", "João da Silva")
print(novoNome)

novoNome = novoNome.replace("da Silva", "dos Santos")
print(novoNome)

nomeCompleto = "thiagO belLato"

print(nomeCompleto.capitalize())  # 1ª Letra Maiuscula
print(nomeCompleto.title())  # 1ª Letra de Cada Palavra Maiuscula


pi = 3.14159265

print(f"{pi:.2f}")


# Posicao Arroba (Pegar servidor emial)
posicaoArroba = emailCliente.find("@") + 1
servidor = emailCliente[posicaoArroba:]
print(servidor)


posicaoEspaco = nomeCompleto.find(" ")
nome = nomeCompleto[:posicaoEspaco]
sobrenome = nomeCompleto[posicaoEspaco + 1 :]
print(nome)
print(sobrenome)
