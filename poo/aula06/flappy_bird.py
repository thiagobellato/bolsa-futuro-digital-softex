import pygame
import os
import random
import sys
import json
import neat

ai_jogando = True
geracao = 0

# --- CONFIGURAÇÃO DE CAMINHO E VARIÁVEIS GLOBAIS ---
try:
    DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
except NameError:
    DIRETORIO_ATUAL = os.path.abspath(os.path.dirname(sys.argv[0]))

IMGS_DIR = os.path.join(DIRETORIO_ATUAL, "imgs")
ARQUIVO_RECORDS = os.path.join(DIRETORIO_ATUAL, "records.json")
ARQUIVO_CONFIG_NEAT = os.path.join(DIRETORIO_ATUAL, "config.txt")

TELA_LARGURA = 500
TELA_ALTURA = 800

# Parâmetros de Dificuldade
VELOCIDADE_CANO = 5
VELOCIDADE_CHAO = VELOCIDADE_CANO + 3 # IA joga em alta velocidade

# Carregamento de Imagens (Mantido)
try:
    IMAGEM_CANO = pygame.transform.scale2x(
        pygame.image.load(os.path.join(IMGS_DIR, "pipe.png"))
    )
    IMAGEM_CHAO = pygame.transform.scale2x(
        pygame.image.load(os.path.join(IMGS_DIR, "base.png"))
    )
    IMAGEM_BACKGROUND = pygame.transform.scale2x(
        pygame.image.load(os.path.join(IMGS_DIR, "bg.png"))
    )
    IMAGENS_PASSARO = [
        pygame.transform.scale2x(
            pygame.image.load(os.path.join(IMGS_DIR, "bird1.png"))
        ),
        pygame.transform.scale2x(
            pygame.image.load(os.path.join(IMGS_DIR, "bird2.png"))
        ),
        pygame.transform.scale2x(
            pygame.image.load(os.path.join(IMGS_DIR, "bird3.png"))
        ),
    ]
except pygame.error as e:
    print(f"Erro ao carregar imagens: {e}")
    print("Verifique se a pasta 'imgs' e os arquivos estão corretos.")
    sys.exit()

pygame.font.init()

# --- FONTES ---
FONTE_PONTOS = pygame.font.SysFont("arial", 50)


# --- FUNÇÕES DE RECORDS (Desabilitadas) ---
def carregar_records():
    return []
def salvar_records(records):
    pass
def checar_novo_recorde(pontos):
    return False
def adicionar_recorde(nome, pontos):
    pass


# --- CLASSE PASSARO (Mantida) ---
class Passaro:
    IMGS = IMAGENS_PASSARO
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[1]

    def pular(self):
        self.velocidade = -12.0
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        GRAVIDADE_PLANO = 0.9
        deslocamento = self.velocidade * self.tempo + GRAVIDADE_PLANO * (self.tempo**2)

        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < -10:
            deslocamento = -10

        self.y += deslocamento
        
        if deslocamento < 0 or self.y < (self.altura - 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        self.contagem_imagem += 1
        # Usando a operação módulo para ciclar as imagens de forma simples
        self.imagem = self.IMGS[self.contagem_imagem // self.TEMPO_ANIMACAO % 3] 

        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


# --- CLASSE CANO (Mantida) ---
class Cano:
    DISTANCIA = 200 # Abertura vertical

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.VELOCIDADE_H = VELOCIDADE_CANO

        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(100, 400)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE_H

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        if base_ponto or topo_ponto:
            return True
        return False


# --- CLASSE CHAO (Mantida) ---
class Chao:
    IMAGEM = IMAGEM_CHAO
    LARGURA = IMAGEM.get_width()

    def __init__(self, y, velocidade):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA
        self.VELOCIDADE = velocidade

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))


# --- FUNÇÃO DE DESENHO DA TELA DA IA ---
def desenhar_tela(tela, passaros, canos, chao, pontos):
    global geracao
    tela.blit(IMAGEM_BACKGROUND, (0, 0))

    for cano in canos:
        cano.desenhar(tela)
    
    for passaro in passaros:
        # Desenhar apenas o primeiro passaro (para desempenho) ou todos
        passaro.desenhar(tela)

    chao.desenhar(tela)

    # Informações da IA
    texto_geracao = FONTE_PONTOS.render(f"Geração: {geracao}", 1, (255, 255, 255))
    tela.blit(texto_geracao, (10, 10))

    texto_pontos = FONTE_PONTOS.render(f"Pontos: {pontos}", 1, (255, 255, 255))
    tela.blit(texto_pontos, (TELA_LARGURA - 10 - texto_pontos.get_width(), 10))
    
    texto_vivos = FONTE_PONTOS.render(f"Vivos: {len(passaros)}", 1, (255, 255, 255))
    tela.blit(texto_vivos, (10, 70))


# --- LOOP DO JOGO (FUNÇÃO FITNESS NEAT OTIMIZADA) ---
def game_loop(genomas, config):
    global geracao
    geracao += 1

    redes = []
    lista_genomas = []
    passaros = []

    # Criação dos pássaros, redes e genomas
    for _, genoma in genomas:
        rede = neat.nn.FeedForwardNetwork.create(genoma, config)
        redes.append(rede)
        # O fitness começa em 0 para cada geração
        genoma.fitness = 0
        lista_genomas.append(genoma)
        passaros.append(Passaro(230, 350))

    pygame.init()
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pygame.display.set_caption(f"Flappy Bird NEAT - Geração {geracao}")

    chao = Chao(730, VELOCIDADE_CHAO)
    canos = [Cano(700)]

    pontos = 0
    relogio = pygame.time.Clock()
    rodando = True

    while rodando and len(passaros) > 0:
        # Aumentar o tick rate do relógio aqui (ex: 60, 120, ou mais) para acelerar o treinamento
        relogio.tick(30) 

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Define qual cano a IA deve olhar (o mais próximo que ainda não passou)
        indice_cano = 0
        # CORREÇÃO: se o primeiro pássaro passou o primeiro cano, olhe para o segundo.
        if len(canos) > 1 and passaros[0].x > canos[0].x + canos[0].CANO_TOPO.get_width():
            indice_cano = 1
        
        # --- DECISÃO DA IA OTIMIZADA ---
        cano_referencia = canos[indice_cano]
        
        # Entradas mais informativas para a rede:
        distancia_vertical_topo = passaros[0].y - cano_referencia.pos_topo
        distancia_vertical_base = passaros[0].y - cano_referencia.pos_base
        distancia_horizontal = cano_referencia.x - passaros[0].x # Distância X do pássaro ao cano
        
        for i, passaro in enumerate(passaros):
            # 1. Aumenta o fitness por sobrevivência
            lista_genomas[i].fitness += 0.1 

            # 2. Entradas para a rede neural: 
            # [Distância_Y_ao_Topo_do_Cano, Distância_Y_à_Base_do_Cano, Distância_X_ao_Cano]
            output = redes[i].activate(
                (
                    passaro.y - cano_referencia.pos_topo,
                    passaro.y - cano_referencia.pos_base,
                    cano_referencia.x - passaro.x # Distância horizontal
                )
            )

            # 3. Executa o pulo se a saída da rede for maior que 0.5
            if output[0] > 0.5:
                passaro.pular()

        # --- MOVIMENTO E COLISÃO ---
        chao.mover()
        adicionar_cano = False
        remover_canos = []

        for passaro in passaros:
            passaro.mover()

        for cano in canos:
            cano.mover() 

            # 1. Colisão com o cano
            for i, passaro in reversed(list(enumerate(passaros))): # Itera reversamente para evitar problemas ao remover
                if cano.colidir(passaro):
                    # Penalidade por colisão
                    lista_genomas[i].fitness -= 1.0 
                    redes.pop(i)
                    lista_genomas.pop(i)
                    passaros.pop(i)

            # 2. Lógica de Pontuação e Geração de Novo Cano
            if not cano.passou and len(passaros) > 0 and passaros[0].x > cano.x + cano.CANO_TOPO.get_width():
                cano.passou = True
                pontos += 1
                adicionar_cano = True
                # Recompensa alta por passar pelo cano (incentivo ao objetivo)
                for genoma in lista_genomas:
                    genoma.fitness += 5.0 

            # 3. Remoção de cano
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)

        if adicionar_cano:
            canos.append(Cano(600))

        for cano in remover_canos:
            canos.remove(cano)

        # 4. Colisão com o chão/teto
        for i, passaro in reversed(list(enumerate(passaros))): # Itera reversamente
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                # Penalidade por cair/bater no teto
                lista_genomas[i].fitness -= 1.0 
                redes.pop(i)
                lista_genomas.pop(i)
                passaros.pop(i)
        
        # --- DESENHO ---
        desenhar_tela(tela, passaros, canos, chao, pontos)
        pygame.display.update()


# --- FUNÇÃO PRINCIPAL NEAT ---
def rodar_neat(caminho_config):
    try:
        config = neat.config.Config(
            neat.DefaultGenome,
            neat.DefaultReproduction,
            neat.DefaultSpeciesSet,
            neat.DefaultStagnation,
            caminho_config,
        )
    except Exception as e:
        print(f"\nERRO: Não foi possível carregar o arquivo de configuração NEAT: {caminho_config}")
        print("Certifique-se de que o arquivo config-feedforward.txt está na pasta correta e tem o formato adequado.")
        sys.exit(1)

    populacao = neat.Population(config)
    
    populacao.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    populacao.add_reporter(stats)

    # Roda a função de fitness (game_loop). Definimos 50 gerações como um bom ponto de partida.
    vencedor = populacao.run(game_loop, 50) 
    print(f"\nEvolução Completa. Melhor genoma encontrado: {vencedor}")


if __name__ == "__main__":
    # Inicia a simulação da IA diretamente
    rodar_neat(ARQUIVO_CONFIG_NEAT)