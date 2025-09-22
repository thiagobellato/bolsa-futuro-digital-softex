class Cliente:
    def __init__(self):
        self.nome = None
        self.email = None
        self.plano = None
        self.lista_planos = ["Básico", "Premium", "Família"]
        
    def Cadastro(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["Básico", "Premium", "Família"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano Inválido")

    def Get(self):
        print(f"Nome do cliente: {self.nome}")
        print(f"Email do cliente: {self.email}")
        print(f"Plano do cliente: {self.plano}")

    def MudarPlano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
            print("Plano Alterado")
        else:
            raise Exception("Plano Inválido")


# Criando uma instância (objeto) da classe Cliente
cliente1 = Cliente()
cliente1.Cadastro("Thiago","tfbellato@hotmail.com","Família")
cliente1.Get()
cliente1.MudarPlano("Básico")
print(cliente1.plano)
