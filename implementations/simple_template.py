#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Template ou "esqueleto" básico para um projeto com Pygame
import pygame
from pygame.locals import *

# declaração de constantes
GAME_NAME = "MODELO DE TEMPLATE - MINICURSO DE PYGAME"

# definindo tamanho para a tela
WIDTH = 800
HEIGHT = 600

# definindo velocidade para o loop principal do jogo
FPS = 30

#definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# função principal para rodar o jogo
def main():
    pygame.init()
    pygame.mixer.init()
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(GAME_NAME)

    all_sprites = pygame.sprite.Group()

    running = True

    clock = pygame.time.Clock()

    # laço principal do jogo.
    while running:

        # define a velocidade correta em que o loop deve rodar
        clock.tick(FPS)

        # processar entrada (eventos)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # jogador clicou no botão de fechar
                running = False
            
            elif event.type == pygame.KEYDOWN:
                # usuário apertou alguma tecla

                if event.key == pygame.K_ESCAPE:
                    running = False

        # atualizar informações do jogo
        all_sprites.update()

        # desenhar e renderizar
        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()