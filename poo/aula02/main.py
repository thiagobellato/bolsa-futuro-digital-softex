class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura, volume = 0, ligado = False):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        self.volume = volume
        self.ligado = ligado

    def __str__(self):
        return (f"Controle Remoto: Cor={self.cor}, Altura={self.altura}cm, "
                f"Profundidade={self.profundidade}cm, Largura={self.largura}cm, "
                f"Volume={self.volume}, Ligado={self.ligado}")
    
    def ligarControle(self):
        self.ligado = True
        print("Controle Ligado")

    def desligarControle(self):
        self.ligado = False
        print("Controle Desligado")

    def aumentarVolume(self):
        if self.ligado: 
            self.volume += 1
            print(f"Aumentando o Volume... O volume agora é: {self.volume}")
        else:
            print("O controle está desligado! Ligue-o para aumentar o volume.")

    def diminuirVolume(self):
        if self.ligado:
            self.volume -= 1
            print(f"Diminuindo o Volume... O volume agora é: {self.volume}")
        else:
            print("O controle está desligado! Ligue-o para diminuir o volume.")


controle1 = ControleRemoto("vermelho", 10, 3, 5)
controle1.ligarControle()
controle1.aumentarVolume()
controle1.aumentarVolume()
controle1.aumentarVolume()
controle1.aumentarVolume()
controle1.aumentarVolume()
controle1.aumentarVolume()
controle1.desligarControle()
print(controle1)