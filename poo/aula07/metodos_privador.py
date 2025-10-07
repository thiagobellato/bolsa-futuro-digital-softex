# class MinhaClasse:
#     def __init__(self, info, elemento):
#         self.atributo_1 = "meu atributo"
#         self.atributo_2 = elemento
#         self.atributo_3 = [1, 2, "a"]
#         self.atributo_4 = info
#         print(self.atributo_4)

#     def metodo_1(self):
#         print("minha acao1")
#         print("minha acao2")
#         print(self.atributo_2)
#         return "Olá Mundo"

#     def metodo_2(self, numero):
#         self.metodo_1()
#         print(self.atributo_3[1] + numero)


# minha_classe = MinhaClasse("informação", 213)
# minha_classe.metodo_2(3)


class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.cpf = cpf

    def __apresentar(self):
        print(f"Minha altura - {self.altura}")
        # Chama o método privado/name-mangled
        self.__coletar_documento() 
        
    # Método "privado" (name-mangled)
    def __coletar_documento(self): 
        print(f"Meu documento - {self.cpf}")
        
joao = Pessoa("1.80","111.222.333-44")

# Chamada que agora deve ser feita para acessar o documento 
# (internamente ele chama o método privado)
joao.__apresentar()

# Se você tentar fazer isso, receberá um erro (AttributeError):
# joao.__coletar_documento()