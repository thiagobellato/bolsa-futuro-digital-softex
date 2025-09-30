import pygame
import os
import random
import sys
import json 

# --- CONFIGURAÇÃO DE CAMINHO E VARIÁVEIS GLOBAIS ---
try:
    DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
except NameError:
    DIRETORIO_ATUAL = os.path.abspath(os.path.dirname(sys.argv[0]))

IMGS_DIR = os.path.join(DIRETORIO_ATUAL, "imgs")
ARQUIVO_RECORDS = os.path.join(DIRETORIO_ATUAL, "records.json")

TELA_LARGURA = 500
TELA_ALTURA = 800

# Parâmetros de Dificuldade
VELOCIDADE_CANO = 5 
POSICAO_PASSARO_ESPECIAL = 180 

# Carregamento de Imagens
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
        pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, "bird1.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, "bird2.png"))),
        pygame.transform.scale2x(pygame.image.load(os.path.join(IMGS_DIR, "bird3.png"))),
    ]
except pygame.error as e:
    print(f"Erro ao carregar imagens: {e}")
    print("Verifique se a pasta 'imgs' e os arquivos estão corretos.")
    sys.exit()

pygame.font.init()

# --- FONTES ATUALIZADAS ---
try:
    FONTE_MENU_ESTILO = pygame.font.SysFont("comicsansms", 40, bold=True)
    FONTE_MENU_TITULO = pygame.font.SysFont("comicsansms", 70, bold=True)
except:
    FONTE_MENU_ESTILO = pygame.font.SysFont("arial", 40)
    FONTE_MENU_TITULO = pygame.font.SysFont("arial", 70, bold=True)

FONTE_PONTOS = pygame.font.SysFont("arial", 50)
FONTE_INPUT = pygame.font.SysFont("arial", 30)


# --- FUNÇÕES DE RECORDS (LEADERBOARD) ---
# (Mantidas as mesmas)
def carregar_records():
    if not os.path.exists(ARQUIVO_RECORDS):
        return []

    with open(ARQUIVO_RECORDS, 'r') as file:
        try:
            data = json.load(file)
            records = data.get('leaderboard', [])
            records.sort(key=lambda x: x['pontos'], reverse=True)
            return records
        except json.JSONDecodeError:
            salvar_records([])
            return []

def salvar_records(records):
    records.sort(key=lambda x: x['pontos'], reverse=True)
    with open(ARQUIVO_RECORDS, 'w') as file:
        json.dump({"leaderboard": records[:10]}, file, indent=4)

def checar_novo_recorde(pontos):
    records = carregar_records()
    if len(records) < 10 or pontos > records[-1]['pontos']:
        return True
    return False

def adicionar_recorde(nome, pontos):
    records = carregar_records()
    nome_limpo = nome.strip().upper()[:8]
    records.append({"nome": nome_limpo if nome_limpo else "NOME", "pontos": pontos})
    salvar_records(records)


# --- CLASSE PASSARO ---

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
        # Lógica de rotação
        if deslocamento < 0 or self.y < (self.altura - 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        # Lógica de animação
        self.contagem_imagem += 1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0
            
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


# --- CLASSE CANO (Lógica de Modo Corrigida) ---

class Cano:
    DISTANCIA = 200
    
    def __init__(self, x, cano_dificuldade):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        
        # --- ATRIBUTOS DE MODO CORRIGIDOS ---
        self.movimento_vertical = (cano_dificuldade == 'MEDIUM')
        self.intermitente = (cano_dificuldade == 'HARD')
        self.pode_ser_controlado = (cano_dificuldade == 'ESPECIAL_CONTROLE')
        
        self.y_ajuste = 0 # O deslocamento vertical aplicado pelo jogador (só se for controlável)
        
        if cano_dificuldade == 'EASY':
            self.VELOCIDADE_H = VELOCIDADE_CANO
        elif cano_dificuldade == 'MEDIUM':
            self.VELOCIDADE_H = VELOCIDADE_CANO + 2
        else: # HARD e ESPECIAL_CONTROLE
            self.VELOCIDADE_H = VELOCIDADE_CANO + 3
        
        # Visibilidade (apenas no modo HARD)
        self.visivel = True
        self.contador_visibilidade = 0
        
        if self.intermitente:
            self.tempo_visivel = 30 * 1.0 
            self.tempo_invisivel = 30 * 0.5 
        
        self.definir_altura()
        
        # Movimento Vertical (apenas no modo MEDIUM)
        if self.movimento_vertical:
            self.vel_y = random.choice([-2, 2])
            self.limite_superior = self.altura - 150
            self.limite_inferior = self.altura + 150
            if self.limite_superior < 50: self.limite_superior = 50
            if self.limite_inferior > 500: self.limite_inferior = 500


    def definir_altura(self):
        self.altura = random.randrange(100, 400)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA

    def mover(self):
        # Movimento Horizontal (sempre acontece)
        self.x -= self.VELOCIDADE_H
        
        # Movimento Vertical (Modo MEDIUM)
        if self.movimento_vertical:
            self.altura += self.vel_y
            self.pos_topo += self.vel_y
            self.pos_base += self.vel_y
            
            if self.altura < self.limite_superior or self.altura > self.limite_inferior:
                self.vel_y *= -1
                
        # Lógica de Visibilidade (Modo HARD)
        if self.intermitente:
            self.contador_visibilidade += 1
            
            if self.visivel and self.contador_visibilidade >= self.tempo_visivel:
                self.visivel = False
                self.contador_visibilidade = 0
            elif not self.visivel and self.contador_visibilidade >= self.tempo_invisivel:
                self.visivel = True
                self.contador_visibilidade = 0


    def desenhar(self, tela):
        if self.visivel:
            # Desenha com o ajuste vertical (0 se não for especial)
            tela.blit(self.CANO_TOPO, (self.x, self.pos_topo + self.y_ajuste))
            tela.blit(self.CANO_BASE, (self.x, self.pos_base + self.y_ajuste))

    def colidir(self, passaro):
        if not self.visivel:
            return False
            
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        # Colisão deve considerar o ajuste vertical!
        distancia_topo = (self.x - passaro.x, (self.pos_topo + self.y_ajuste) - round(passaro.y))
        distancia_base = (self.x - passaro.x, (self.pos_base + self.y_ajuste) - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        if base_ponto or topo_ponto:
            return True
        return False


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


# --- FUNÇÕES DE INTERFACE (Mantidas) ---

def desenhar_tela(tela, passaros, canos, chao, pontos, modo):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    texto_modo = FONTE_INPUT.render(f"MODO: {modo}", 1, (200, 200, 200))
    tela.blit(texto_modo, (10, 10))

    if modo.startswith('ESPECIAL'):
        texto_instrucao = FONTE_INPUT.render("Controle: Setas Cima/Baixo ou W/S (Mover Cano)", 1, (255, 255, 0))
        tela.blit(texto_instrucao, (TELA_LARGURA // 2 - texto_instrucao.get_width() // 2, 70))


    texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    chao.desenhar(tela)

def exibir_game_over(tela, pontos, nome_jogador, novo_recorde, recorde_salvo):
    s = pygame.Surface((TELA_LARGURA, TELA_ALTURA), pygame.SRCALPHA)
    s.fill((0, 0, 0, 180)) 
    tela.blit(s, (0, 0))

    texto_titulo = FONTE_PONTOS.render("GAME OVER", 1, (255, 50, 50))
    x_titulo = TELA_LARGURA // 2 - texto_titulo.get_width() // 2
    tela.blit(texto_titulo, (x_titulo, 150))

    texto_pontos = FONTE_INPUT.render(f"Pontos: {pontos}", 1, (255, 255, 255))
    tela.blit(texto_pontos, (TELA_LARGURA // 2 - texto_pontos.get_width() // 2, 230))
    
    if novo_recorde:
        if not recorde_salvo:
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
    texto_reset = fonte_instrucao_reset.render("Pressione **R** (Recordes) | **M** (Menu) | Qualquer Outra (Recomeçar)", 1, (200, 200, 200))
    tela.blit(texto_reset, (TELA_LARGURA // 2 - texto_reset.get_width() // 2, TELA_ALTURA - 50))

    pygame.display.update()

def desenhar_leaderboard(tela, records):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))

    texto_titulo = FONTE_MENU_TITULO.render("RECORDES", 1, (255, 255, 0))
    tela.blit(texto_titulo, (TELA_LARGURA // 2 - texto_titulo.get_width() // 2, 50))
    
    fonte_item = FONTE_MENU_ESTILO
    y_pos = 150
    
    for i, record in enumerate(records):
        cor = (255, 255, 255)
        if i == 0:
            cor = (255, 215, 0)

        linha_texto = f"#{i+1:<2} {record['nome']:<8} {record['pontos']:>3}"
        texto_linha = fonte_item.render(linha_texto, 1, cor)
        tela.blit(texto_linha, (TELA_LARGURA // 2 - texto_linha.get_width() // 2, y_pos))
        y_pos += 50
    
    texto_instrucao = FONTE_INPUT.render("Pressione ENTER para Voltar", 1, (150, 150, 150))
    tela.blit(texto_instrucao, (TELA_LARGURA // 2 - texto_instrucao.get_width() // 2, TELA_ALTURA - 50))
    
    pygame.display.update()


# --- FUNÇÃO DE SELEÇÃO DE MENU (ESTILO) ---

def desenhar_menu_selecao(tela, selecao):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    
    texto_titulo = FONTE_MENU_TITULO.render("FLAPPY BIRD", 1, (255, 255, 255))
    tela.blit(texto_titulo, (TELA_LARGURA // 2 - texto_titulo.get_width() // 2, 100))

    texto_instrucao = FONTE_INPUT.render("Selecione o Modo:", 1, (200, 200, 200))
    tela.blit(texto_instrucao, (TELA_LARGURA // 2 - texto_instrucao.get_width() // 2, 250))
    
    opcoes = [
        '[1] EASY (Normal Player)', 
        '[2] MEDIUM (Canos Móveis)',
        '[3] HARD (Cano Intermitente)',
        '[4] MODO ESPECIAL (Controle de Cano)' 
    ]
    
    y_pos = 350
    for i, opcao in enumerate(opcoes):
        cor = (255, 255, 255)
        if i + 1 == selecao:
            cor = (255, 255, 0) 
        
        texto_opcao = FONTE_MENU_ESTILO.render(f"{opcao}", 1, cor)
        tela.blit(texto_opcao, (TELA_LARGURA // 2 - texto_opcao.get_width() // 2, y_pos))
        y_pos += 50
    
    texto_leader = FONTE_INPUT.render("Pressione **R** para Recordes", 1, (150, 150, 150))
    tela.blit(texto_leader, (TELA_LARGURA // 2 - texto_leader.get_width() // 2, TELA_ALTURA - 100))

    pygame.display.update()

def main_menu():
    
    pygame.init()
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pygame.display.set_caption("Flappy Bird com Novo Modo")
    
    menu_aberto = True
    leaderboard_aberto = False
    selecao = 4 # Começa na seleção do novo modo
    
    while menu_aberto:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.KEYDOWN:
                if not leaderboard_aberto:
                    if evento.key == pygame.K_1:
                        selecao = 1
                    elif evento.key == pygame.K_2:
                        selecao = 2
                    elif evento.key == pygame.K_3: 
                        selecao = 3
                    elif evento.key == pygame.K_4: 
                        selecao = 4
                    
                    if evento.key == pygame.K_SPACE or evento.key == pygame.K_RETURN:
                        if selecao == 1:
                            game_loop(tela, modo='DIFICULDADE', dificuldade='EASY')
                        elif selecao == 2:
                            game_loop(tela, modo='DIFICULDADE', dificuldade='MEDIUM')
                        elif selecao == 3:
                            game_loop(tela, modo='DIFICULDADE', dificuldade='HARD')
                        else: # Modo Especial
                            game_loop(tela, modo='ESPECIAL')
                    
                    if evento.key == pygame.K_r: # 'R' para Recordes
                        leaderboard_aberto = True
                else:
                    if evento.key == pygame.K_RETURN:
                        leaderboard_aberto = False
        
        if leaderboard_aberto:
            records = carregar_records()
            desenhar_leaderboard(tela, records)
        else:
            desenhar_menu_selecao(tela, selecao)


# --- LOOP DO JOGO (COM MODO ESPECIAL DE CONTROLE CORRIGIDO) ---
def game_loop(tela, modo, dificuldade=None):
    
    # 1. Configuração do Pássaro e Dificuldade
    posicao_x_passaro = 230
    cano_dificuldade = 'HARD' 
    
    if modo == 'DIFICULDADE':
        
        if dificuldade == 'EASY':
            velocidade_chao = VELOCIDADE_CANO
            cano_dificuldade = 'EASY'
            modo_titulo = 'EASY (Normal Player)'
        elif dificuldade == 'MEDIUM':
            velocidade_chao = VELOCIDADE_CANO + 2
            cano_dificuldade = 'MEDIUM' # Canos se movem verticalmente
            modo_titulo = 'MEDIUM (Canos Móveis)'
        else: # HARD
            velocidade_chao = VELOCIDADE_CANO + 3
            cano_dificuldade = 'HARD' # Canos intermitentes (invisíveis)
            modo_titulo = 'HARD (Cano Intermitente)'
            
    else: # modo == 'ESPECIAL'
        # Pássaro é estático em (X, Y)
        posicao_x_passaro = POSICAO_PASSARO_ESPECIAL
        velocidade_chao = VELOCIDADE_CANO + 3 
        cano_dificuldade = 'ESPECIAL_CONTROLE' 
        modo_titulo = 'ESPECIAL (Controle de Cano)'
    
    passaros = [Passaro(posicao_x_passaro, 350)]
    chao = Chao(730, velocidade_chao)
    canos = [Cano(700, cano_dificuldade)]
    
    pontos = 0
    relogio = pygame.time.Clock()
    rodando = True
    
    game_over = False
    novo_recorde = False
    nome_jogador = ""
    recorde_salvo = False
    
    ajuste_vertical_cano = 0 
    VELOCIDADE_AJUSTE_CANO = 15 

    while rodando:
        relogio.tick(30) 
        
        # --- Lógica de Eventos ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if not game_over:
                # Pássaro só PULA nos modos normais (1, 2 e 3)
                if modo != 'ESPECIAL' and evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE and len(passaros) > 0:
                    passaros[0].pular()

                # Controle de cano no Modo Especial (4)
                if modo == 'ESPECIAL':
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                            ajuste_vertical_cano = -VELOCIDADE_AJUSTE_CANO # Move buraco para CIMA
                        elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                            ajuste_vertical_cano = VELOCIDADE_AJUSTE_CANO # Move buraco para BAIXO
                    
                    if evento.type == pygame.KEYUP:
                        if evento.key in [pygame.K_UP, pygame.K_w, pygame.K_DOWN, pygame.K_s]:
                            ajuste_vertical_cano = 0 

            else: # Lógica de Game Over (M, R, Recomeçar)
                # ... (Lógica de recorde e menu mantida)
                if evento.type == pygame.KEYDOWN:
                    if novo_recorde and not recorde_salvo:
                         if evento.key == pygame.K_RETURN:
                             if nome_jogador.strip():
                                 adicionar_recorde(nome_jogador, pontos)
                             else:
                                 adicionar_recorde("PLAYER", pontos)
                             recorde_salvo = True
                         elif evento.key == pygame.K_BACKSPACE:
                             nome_jogador = nome_jogador[:-1]
                         elif len(nome_jogador) < 8:
                             if evento.unicode.isalnum() or evento.unicode == ' ':
                                 nome_jogador += evento.unicode.upper()
                    
                    elif evento.key == pygame.K_m: 
                        return
                    
                    elif evento.key == pygame.K_r: 
                        main_menu() 
                        return

                    else:
                        game_loop(tela, modo, dificuldade)
                        return
                        
        # --- Lógica de Movimento e Colisão ---
        if not game_over:
            if len(passaros) > 0:
                
                # Movimento do pássaro SÓ nos modos normais
                if modo != 'ESPECIAL':
                    for passaro in passaros:
                        passaro.mover()
                
                chao.mover()
                adicionar_cano = False
                remover_canos = []
                
                for cano in canos:
                    cano.mover() # Move horizontalmente e, se for MEDIUM/HARD, verticalmente/intermitente
                    
                    # Aplica o controle vertical APENAS no Modo Especial
                    if cano.pode_ser_controlado:
                        # Limita o ajuste vertical
                        cano.y_ajuste = max(-200, min(200, cano.y_ajuste + ajuste_vertical_cano))

                    for i, passaro in enumerate(passaros):
                        if cano.colidir(passaro):
                            passaros.pop(i)
                        
                        # Lógica de Contagem de Pontos 
                        if not cano.passou and passaro.x > cano.x + cano.CANO_TOPO.get_width():
                            cano.passou = True
                            adicionar_cano = True

                            
                    if cano.x + cano.CANO_TOPO.get_width() < 0:
                        remover_canos.append(cano)

                if adicionar_cano:
                    pontos += 1
                    # Canos aparecem mais perto no modo Especial para aumentar o ritmo
                    nova_posicao_cano = 600
                    if modo == 'ESPECIAL':
                        nova_posicao_cano = 400 

                    canos.append(Cano(nova_posicao_cano, cano_dificuldade))
                
                for cano in remover_canos:
                    canos.remove(cano)
                
                for i, passaro in enumerate(passaros):
                    # Colisão com o chão/teto (funciona em todos os modos, mesmo que no Especial o pássaro não se mova sozinho)
                    if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                        passaros.pop(i)
                
            if len(passaros) == 0:
                game_over = True
                if checar_novo_recorde(pontos):
                    novo_recorde = True

        
        # --- Desenho da Tela ---
        if not game_over:
            desenhar_tela(tela, passaros, canos, chao, pontos, modo_titulo)
            pygame.display.update()
        else:
            exibir_game_over(tela, pontos, nome_jogador, novo_recorde, recorde_salvo)


if __name__ == "__main__":
    main_menu()