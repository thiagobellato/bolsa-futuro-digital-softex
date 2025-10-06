import pygame
import os
import random
import sys
import json 

# --- CONFIGURAÇÃO E VARIÁVEIS GLOBAIS ---
try:
    DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
except NameError:
    DIRETORIO_ATUAL = os.path.abspath(os.path.dirname(sys.argv[0]))

IMGS_DIR = os.path.join(DIRETORIO_ATUAL, "imgs")
ARQUIVO_RECORDS = os.path.join(DIRETORIO_ATUAL, "records.json")

TELA_LARGURA = 500
TELA_ALTURA = 800

# Parâmetros de Jogo
VELOCIDADE_CANO = 5             # Velocidade horizontal base
POSICAO_PASSARO_FIXA = 180      # Posição X do pássaro no Modo Especial
VELOCIDADE_AJUSTE_CANO = 15     # Velocidade de movimento do cano (Controle por Teclado)

# Carregamento de Imagens e Fontes
try:
    IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, "pipe.png")))
    IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, "base.png")))
    IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, "bg.png")))
    IMAGENS_PASSARO = [
        pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, "bird1.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, "bird2.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, "bird3.png"))),
    ]
except pygame.error as e:
    print(f"Erro ao carregar imagens: {e}")
    sys.exit()

pygame.font.init()
FONTE_TITULO = pygame.font.SysFont("arial", 70, bold=True)
FONTE_MENU = pygame.font.SysFont("arial", 40, bold=True)
FONTE_PONTOS = pygame.font.SysFont("arial", 50)
FONTE_INPUT = pygame.font.SysFont("arial", 30)

# --- FUNÇÕES DE RECORDS (Leaderboard) ---

def carregar_records():
    """Carrega o Top 10 de records do arquivo JSON."""
    if not os.path.exists(ARQUIVO_RECORDS):
        return []
    with open(ARQUIVO_RECORDS, 'r') as file:
        try:
            data = json.load(file)
            records = data.get('leaderboard', [])
            records.sort(key=lambda x: x['pontos'], reverse=True)
            return records
        except json.JSONDecodeError:
            return []

def salvar_records(records):
    """Salva o Top 10 de records no arquivo JSON."""
    records.sort(key=lambda x: x['pontos'], reverse=True)
    with open(ARQUIVO_RECORDS, 'w') as file:
        json.dump({"leaderboard": records[:10]}, file, indent=4)

def checar_novo_recorde(pontos):
    """Verifica se a pontuação atual é um novo recorde (Top 10)."""
    records = carregar_records()
    return len(records) < 10 or pontos > records[-1]['pontos']

def adicionar_recorde(nome, pontos):
    """Adiciona um novo recorde e salva a lista."""
    records = carregar_records()
    nome_limpo = nome.strip().upper()[:8]
    records.append({"nome": nome_limpo if nome_limpo else "PLAYER", "pontos": pontos})
    salvar_records(records)


# --- CLASSE PASSARO ---

class Passaro:
    """
    Representa o pássaro, com lógica de movimento condicional.
    """
    IMGS = IMAGENS_PASSARO
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y, pode_pular):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.pode_pular = pode_pular
        
    def pular(self):
        """Inicia o pulo se o modo permitir."""
        if self.pode_pular:
            self.velocidade = -12.0  
            self.tempo = 0
            self.altura = self.y

    def mover(self):
        """Atualiza a posição (apenas se 'pode_pular') e a animação."""
        if self.pode_pular:
            self.tempo += 1
            GRAVIDADE_PLANO = 0.9 
            deslocamento = self.velocidade * self.tempo + GRAVIDADE_PLANO * (self.tempo**2) 

            # Limita o deslocamento
            if deslocamento > 16:
                deslocamento = 16
            elif deslocamento < -10: 
                deslocamento = -10
            
            self.y += deslocamento
            
            # Lógica de rotação
            if deslocamento < 0 or self.y < (self.altura - 50):
                if self.angulo < self.ROTACAO_MAXIMA:
                    self.angulo = self.ROTACAO_MAXIMA
            else:
                if self.angulo > -90:
                    self.angulo -= self.VELOCIDADE_ROTACAO

        # Lógica de animação
        self.contagem_imagem += 1
        self.imagem = self.IMGS[self.contagem_imagem // self.TEMPO_ANIMACAO % 3]
            
    def desenhar(self, tela):
        """Desenha o pássaro na tela."""
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        """Retorna a máscara de colisão do pássaro."""
        return pygame.mask.from_surface(self.imagem)


# --- CLASSE CANO ---

class Cano:
    """
    Representa os canos com lógica de dificuldade.
    """
    DISTANCIA = 200 # Abertura vertical padrão
    
    def __init__(self, x, dificuldade, velocidade_chao):
        self.x = x
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        
        # Configurações dinâmicas
        self.VELOCIDADE_H = velocidade_chao
        self.intermitente = (dificuldade == 'HARD')      
        self.movimento_vertical = (dificuldade == 'MEDIUM') 
        self.controlavel = (dificuldade == 'ESPECIAL')      
        self.y_ajuste = 0                                # Deslocamento total do cano

        # Variáveis para intermitente (HARD)
        self.visivel = True
        self.contador_visibilidade = 0
        if self.intermitente:
            self.tempo_visivel = 30 * 1.0 
            self.tempo_invisivel = 30 * 0.5 

        # Variáveis para movimento vertical (MEDIUM)
        if self.movimento_vertical:
            self.vel_y = random.choice([-2, 2])
        
        self.definir_altura()
        # Armazena a posição Y inicial para referência do ajuste
        self.altura_inicial_topo = self.pos_topo
        self.altura_inicial_base = self.pos_base


    def definir_altura(self):
        """Define uma nova altura aleatória para o buraco do cano."""
        altura_centro = random.randrange(100, 400)
        self.pos_topo = altura_centro - self.CANO_TOPO.get_height()
        self.pos_base = altura_centro + self.DISTANCIA

    def mover(self):
        """Move o cano horizontalmente e verticalmente (se for o Modo Medium)."""
        self.x -= self.VELOCIDADE_H
        
        if self.movimento_vertical:
            # Lógica de movimento vertical (Modo MEDIUM)
            # O y_ajuste do cano é usado para a física do cano móvel
            self.y_ajuste += self.vel_y
            
            # Limita o movimento vertical para o cano móvel (corrigido)
            LIMITE_MOVIMENTO = 100 
            if self.y_ajuste > LIMITE_MOVIMENTO or self.y_ajuste < -LIMITE_MOVIMENTO:
                 self.vel_y *= -1
                 
        if self.intermitente:
            # Lógica de visibilidade (Modo HARD)
            self.contador_visibilidade += 1
            if self.visivel and self.contador_visibilidade >= self.tempo_visivel:
                self.visivel = False
                self.contador_visibilidade = 0
            elif not self.visivel and self.contador_visibilidade >= self.tempo_invisivel:
                self.visivel = True
                self.contador_visibilidade = 0

    def desenhar(self, tela):
        """Desenha o cano se estiver visível."""
        if self.visivel:
            # A posição final é a inicial + o ajuste (movimento ou controle do jogador)
            tela.blit(self.CANO_TOPO, (self.x, self.pos_topo + self.y_ajuste))
            tela.blit(self.CANO_BASE, (self.x, self.pos_base + self.y_ajuste))

    def colidir(self, passaro):
        """Verifica a colisão com o pássaro."""
        if not self.visivel:
            return False
            
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        # Colisão usa a posição inicial + o ajuste vertical total (y_ajuste)
        distancia_topo = (self.x - passaro.x, (self.pos_topo + self.y_ajuste) - round(passaro.y))
        distancia_base = (self.x - passaro.x, (self.pos_base + self.y_ajuste) - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        return base_ponto or topo_ponto


# --- CLASSE CHAO ---

class Chao:
    """Representa o chão que se move em loop."""
    IMAGEM = IMAGEM_CHAO
    LARGURA = IMAGEM.get_width()

    def __init__(self, y, velocidade):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA
        self.VELOCIDADE = velocidade

    def mover(self):
        """Move as duas imagens do chão."""
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        """Desenha o chão."""
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))


# --- INTERFACE E MENU ---

def desenhar_tela(tela, passaro, canos, chao, pontos, modo_titulo):
    """Desenha todos os elementos do jogo na tela."""
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    
    passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    chao.desenhar(tela)
    
    # Informações
    texto_modo = FONTE_INPUT.render(f"MODO: {modo_titulo}", 1, (200, 200, 200))
    tela.blit(texto_modo, (10, 10))
    
    # Instruções dinâmicas
    if modo_titulo.startswith('ESPECIAL'):
        instrucao = "Controle: Setas/W/S ou Mouse (Mover Cano)"
    else:
        instrucao = "Controle: ESPAÇO (Pular)"
    
    texto_instrucao = FONTE_INPUT.render(instrucao, 1, (255, 255, 0))
    tela.blit(texto_instrucao, (TELA_LARGURA // 2 - texto_instrucao.get_width() // 2, 70))

    texto_pontos = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto_pontos, (TELA_LARGURA - 10 - texto_pontos.get_width(), 10))

def exibir_game_over(tela, pontos, nome_jogador, novo_recorde, recorde_salvo):
    """Exibe a tela de Game Over e o input de recorde."""
    s = pygame.Surface((TELA_LARGURA, TELA_ALTURA), pygame.SRCALPHA)
    s.fill((0, 0, 0, 180)) 
    tela.blit(s, (0, 0))

    texto_titulo = FONTE_PONTOS.render("GAME OVER", 1, (255, 50, 50))
    tela.blit(texto_titulo, (TELA_LARGURA // 2 - texto_titulo.get_width() // 2, 150))

    texto_pontos = FONTE_INPUT.render(f"Pontos: {pontos}", 1, (255, 255, 255))
    tela.blit(texto_pontos, (TELA_LARGURA // 2 - texto_pontos.get_width() // 2, 230))
    
    if novo_recorde:
        if not recorde_salvo:
            # Lógica de input do nome
            texto_instrucao = FONTE_INPUT.render("NOVO RECORDE! Digite seu nome:", 1, (255, 255, 0))
            tela.blit(texto_instrucao, (TELA_LARGURA // 2 - texto_instrucao.get_width() // 2, 320))
            
            input_box = pygame.Rect(TELA_LARGURA // 2 - 100, 370, 200, 40)
            pygame.draw.rect(tela, (255, 255, 255), input_box, 2)
            
            texto_nome = FONTE_INPUT.render(nome_jogador, 1, (255, 255, 255))
            tela.blit(texto_nome, (input_box.x + 5, input_box.y + 5))
            
            texto_salvar = FONTE_INPUT.render("Pressione ENTER para Salvar", 1, (50, 255, 50))
            tela.blit(texto_salvar, (TELA_LARGURA // 2 - texto_salvar.get_width() // 2, 430))
        else:
            texto_salvo = FONTE_INPUT.render("Recorde Salvo! Parabéns!", 1, (50, 255, 50))
            tela.blit(texto_salvo, (TELA_LARGURA // 2 - texto_salvo.get_width() // 2, 370))
    else:
        texto_nao_recorde = FONTE_INPUT.render("Sua pontuação não entrou no Top 10.", 1, (200, 200, 200))
        tela.blit(texto_nao_recorde, (TELA_LARGURA // 2 - texto_nao_recorde.get_width() // 2, 370))

    fonte_instrucao_reset = pygame.font.SysFont("arial", 25)
    texto_reset = fonte_instrucao_reset.render("Pressione **R** (Recordes) | ESC (Menu) | Qualquer Outra (Recomeçar)", 1, (200, 200, 200))
    tela.blit(texto_reset, (TELA_LARGURA // 2 - texto_reset.get_width() // 2, TELA_ALTURA - 50))


def desenhar_leaderboard(tela, records):
    """Exibe a tela de Recordes (Leaderboard)."""
    tela.blit(IMAGEM_BACKGROUND, (0, 0))

    texto_titulo = FONTE_TITULO.render("RECORDES", 1, (255, 255, 0))
    tela.blit(texto_titulo, (TELA_LARGURA // 2 - texto_titulo.get_width() // 2, 50))
    
    y_pos = 150
    for i, record in enumerate(records):
        cor = (255, 255, 255) if i > 0 else (255, 215, 0)
        linha_texto = f"#{i+1:<2} {record['nome']:<8} {record['pontos']:>3}"
        texto_linha = FONTE_PONTOS.render(linha_texto, 1, cor)
        tela.blit(texto_linha, (TELA_LARGURA // 2 - texto_linha.get_width() // 2, y_pos))
        y_pos += 50
    
    texto_instrucao = FONTE_INPUT.render("Pressione ENTER para Voltar | ESC para o Menu Principal", 1, (150, 150, 150))
    tela.blit(texto_instrucao, (TELA_LARGURA // 2 - texto_instrucao.get_width() // 2, TELA_ALTURA - 50))
    pygame.display.update()

def main_menu(tela):
    """Gerencia o menu principal e a seleção de modos."""
    
    menu_aberto = True
    leaderboard_aberto = False
    selecao = 1 
    
    opcoes = [
        'EASY (Pulo Simples, Cano Fixo, Vel. Lenta)', 
        'MEDIUM (Pulo Simples, Cano Móvel, Vel. Média)',
        'HARD (Pulo Simples, Cano Intermitente, Vel. Rápida)',
        'ESPECIAL (Controle de Cano, Pássaro Fixo, Vel. Rápida)' 
    ]
    modos = ['EASY', 'MEDIUM', 'HARD', 'ESPECIAL']
    
    while menu_aberto:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE: # Sai do jogo/recordes
                    if leaderboard_aberto:
                        leaderboard_aberto = False
                    else:
                        pygame.quit()
                        sys.exit()
                    
                if not leaderboard_aberto:
                    # Seleção de modo
                    if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                        selecao = max(1, selecao - 1)
                    elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                        selecao = min(len(modos), selecao + 1)
                    
                    if evento.key in [pygame.K_SPACE, pygame.K_RETURN, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                        if evento.key == pygame.K_1: selecao = 1
                        elif evento.key == pygame.K_2: selecao = 2
                        elif evento.key == pygame.K_3: selecao = 3
                        elif evento.key == pygame.K_4: selecao = 4

                        modo_selecionado = modos[selecao - 1]
                        # Inicia o jogo, se retornar True, volta ao menu
                        if game_loop(tela, modo_selecionado):
                            return
                        
                    if evento.key == pygame.K_r: # 'R' para Recordes
                        leaderboard_aberto = True
                else:
                    if evento.key == pygame.K_RETURN:
                        leaderboard_aberto = False

        if leaderboard_aberto:
            records = carregar_records()
            desenhar_leaderboard(tela, records)
        else:
            # Desenha a tela de Menu
            tela.blit(IMAGEM_BACKGROUND, (0, 0))
            texto_titulo = FONTE_TITULO.render("FLAPPY BIRD", 1, (255, 255, 255))
            tela.blit(texto_titulo, (TELA_LARGURA // 2 - texto_titulo.get_width() // 2, 100))
            texto_instrucao = FONTE_INPUT.render("Selecione o Modo:", 1, (200, 200, 200))
            tela.blit(texto_instrucao, (TELA_LARGURA // 2 - texto_instrucao.get_width() // 2, 250))
            
            y_pos = 350
            for i, opcao in enumerate(opcoes):
                cor = (255, 255, 255) if i + 1 != selecao else (255, 255, 0)
                texto_opcao = FONTE_MENU.render(f"[{i+1}] {opcao}", 1, cor)
                tela.blit(texto_opcao, (TELA_LARGURA // 2 - texto_opcao.get_width() // 2, y_pos))
                y_pos += 50
            
            texto_leader = FONTE_INPUT.render("Pressione **R** (Recordes) | ESC (Sair)", 1, (150, 150, 150))
            tela.blit(texto_leader, (TELA_LARGURA // 2 - texto_leader.get_width() // 2, TELA_ALTURA - 100))
            pygame.display.update()


# --- LOOP PRINCIPAL DO JOGO ---

def game_loop(tela, modo):
    """O loop principal de jogo, adaptado para todos os modos."""
    
    # 1. Configurações baseadas no modo
    if modo == 'EASY':
        velocidade_chao = VELOCIDADE_CANO
        pode_pular = True
        posicao_passaro_x = 230
    elif modo == 'MEDIUM':
        velocidade_chao = VELOCIDADE_CANO + 2
        pode_pular = True
        posicao_passaro_x = 230
    elif modo == 'HARD':
        velocidade_chao = VELOCIDADE_CANO + 3
        pode_pular = True
        posicao_passaro_x = 230
    else: # Modo ESPECIAL
        velocidade_chao = VELOCIDADE_CANO + 3
        pode_pular = False
        posicao_passaro_x = POSICAO_PASSARO_FIXA
        
    MODO_TITULO = modo
    
    # Inicializa os objetos
    passaro = Passaro(posicao_passaro_x, 350, pode_pular)
    chao = Chao(730, velocidade_chao)
    canos = [Cano(700, modo, velocidade_chao)]
    
    pontos = 0
    relogio = pygame.time.Clock()
    game_over = False
    novo_recorde = False
    recorde_salvo = False
    nome_jogador = ""
    leaderboard_aberto = False

    # Controle do jogador no modo especial
    ajuste_vertical_cano = 0 
    mouse_control = False
    nova_posicao_cano_x = 600 if modo != 'ESPECIAL' else 400

    while True:
        relogio.tick(30)
        
        # --- Lógica de Eventos ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # ESC: VOLTA AO MENU PRINCIPAL (durante o jogo, game over ou recordes)
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return True # Sinaliza para voltar ao menu

            if game_over:
                # Gerencia a navegação na tela de Game Over
                if leaderboard_aberto:
                    if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                        leaderboard_aberto = False
                    continue

                if evento.type == pygame.KEYDOWN:
                    if novo_recorde and not recorde_salvo:
                        # Input do nome
                        if evento.key == pygame.K_RETURN:
                            adicionar_recorde(nome_jogador, pontos)
                            recorde_salvo = True
                        elif evento.key == pygame.K_BACKSPACE:
                            nome_jogador = nome_jogador[:-1]
                        elif len(nome_jogador) < 8 and (evento.unicode.isalnum() or evento.unicode == ' '):
                            nome_jogador += evento.unicode.upper()
                            
                    elif evento.key == pygame.K_r: # Vai para Recordes
                        leaderboard_aberto = True
                        
                    elif recorde_salvo or not novo_recorde: # Recomeçar
                        game_loop(tela, modo)
                        return
                    
            else:
                # 2. Controle do Pássaro (Modos Easy/Medium/Hard)
                if pode_pular and evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                    passaro.pular()

                # 3. Controle do Cano (Modo Especial)
                if not pode_pular:
                    # Mouse
                    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # Botão esquerdo
                        mouse_control = True
                    if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                        mouse_control = False

                    # Teclado
                    if evento.type == pygame.KEYUP:
                        if evento.key in [pygame.K_UP, pygame.K_w, pygame.K_DOWN, pygame.K_s]:
                            ajuste_vertical_cano = 0
                    elif evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                            ajuste_vertical_cano = -VELOCIDADE_AJUSTE_CANO
                        elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                            ajuste_vertical_cano = VELOCIDADE_AJUSTE_CANO
        
        # --- Lógica de Movimento e Colisão ---
        if not game_over and not leaderboard_aberto:
            
            passaro.mover() 
            chao.mover()
            
            adicionar_cano = False
            remover_canos = []
            
            for cano in canos:
                cano.mover() 
                
                # Controle de Posição do Cano (Modo Especial)
                if cano.controlavel:
                    if mouse_control:
                        # Se o mouse estiver pressionado, ajusta o cano para seguir a posição Y do mouse
                        mouse_y = pygame.mouse.get_pos()[1]
                        # Calcula o y_ajuste necessário para que o centro do buraco (altura_centro) siga o mouse
                        centro_buraco_mouse = mouse_y 
                        centro_buraco_cano = cano.pos_base - (cano.DISTANCIA / 2)
                        
                        # Ajusta o y_ajuste do cano na direção do mouse
                        diferenca = centro_buraco_mouse - centro_buraco_cano
                        
                        # Suaviza o movimento e evita o jittering
                        if abs(diferenca) > 5:
                            cano.y_ajuste += diferenca / 5 
                        else:
                            cano.y_ajuste += diferenca # Move o restante
                        
                    else:
                        # Se mouse não estiver pressionado, aplica o ajuste do teclado
                        cano.y_ajuste += ajuste_vertical_cano
                        
                    # Limite de ajuste vertical
                    LIMITE_AJUSTE_JOGADOR = 200
                    cano.y_ajuste = max(-LIMITE_AJUSTE_JOGADOR, min(LIMITE_AJUSTE_JOGADOR, cano.y_ajuste))


                if cano.colidir(passaro):
                    game_over = True
                    break

                # Pontuação e Geração de Novo Cano
                if not cano.passou and passaro.x > cano.x + cano.CANO_TOPO.get_width():
                    cano.passou = True
                    adicionar_cano = True
                        
                # Remove cano que saiu da tela
                if cano.x + cano.CANO_TOPO.get_width() < 0:
                    remover_canos.append(cano)

            if game_over:
                if checar_novo_recorde(pontos):
                    novo_recorde = True
            
            if adicionar_cano:
                pontos += 1
                canos.append(Cano(nova_posicao_cano_x, modo, velocidade_chao))

            for cano in remover_canos:
                canos.remove(cano)
            
            # Colisão com o chão/teto
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                game_over = True
                if checar_novo_recorde(pontos):
                    novo_recorde = True

        
        # --- Desenho da Tela ---
        if not game_over:
            desenhar_tela(tela, passaro, canos, chao, pontos, MODO_TITULO)
        else:
            if leaderboard_aberto:
                records = carregar_records()
                desenhar_leaderboard(tela, records)
            else:
                exibir_game_over(tela, pontos, nome_jogador, novo_recorde, recorde_salvo)
                
        pygame.display.update()
        
    return False # Retorna False por padrão se o loop for interrompido de outra forma (sair do Pygame)


# --- INÍCIO DO PROGRAMA ---

if __name__ == "__main__":
    # Inicializa Pygame e chama o Menu Principal
    pygame.init()
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pygame.display.set_caption("Flappy Bird: Múltiplos Modos")
    main_menu(tela)