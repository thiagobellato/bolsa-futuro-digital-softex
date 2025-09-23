import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "pipe.png"))
)
IMAGEM_CHAO = pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "base.png"))
)
IMAGEM_BACKGROUND = pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "bg.png"))
)
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png"))),
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont("arial", 50)


class Passaro:
    IMGS = IMAGENS_PASSARO
    # rotação do passaro
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
        self.velocidade = 10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # calcular deslocamento
        self.tempo += 1
        self.deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        # restringir deslocamento]
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento - +2

        self.y += deslocamento

        # angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.anguolo < self.ROTACAO_MAXIMA:
                self.angulo -= self.VELOCIDADE_ROTACAO
        else:
            if self.angulo > 90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self):
        # definir qual imagem vai aparecer
        self.contagem_imagem += 1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO * 4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0
        #se o passaro estiver caindo não vai bater a asa
        if self.angulo <= 80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO * 2


class Cano:
    pass


class Chao:
    pass
