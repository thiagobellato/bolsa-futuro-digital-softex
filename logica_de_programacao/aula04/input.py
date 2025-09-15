class Cadastro:
    def __init__(self, nome, email, faturamento, taxa_imposto):
        self.nome = nome
        self.email = email
        self.faturamento = faturamento
        self.taxa_imposto = taxa_imposto
        self.imposto = 0
        self.lucro = 0

    def calcular_imposto(self):
        self.imposto = self.faturamento * self.taxa_imposto

    def calcular_lucro(self):
        self.lucro = self.faturamento - self.imposto

    def exibir_resumo(self):
        print(
            f"{self.nome}, verifique seu e-mail: {self.email} para confirmar o seu cadastro"
        )
        print(f"Faturamento: {self.faturamento}")
        print(f"Imposto: {self.imposto}")
        print(f"Lucro: {self.lucro}")


# ===== Uso da classe =====
nome = input("Digite o seu nome: ")
email = input("Digite o seu e-mail: ")
faturamento = float(input("Digite o seu faturamento: "))
taxa_imposto = float(input("Digite a taxa de imposto: "))

cadastro = Cadastro(nome, email, faturamento, taxa_imposto)
cadastro.calcular_imposto()
cadastro.calcular_lucro()
cadastro.exibir_resumo()