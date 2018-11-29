#!/bin/usr/env python
# -*- coding: utf-8 -*-
import pygame
from sprites import *

GAME_NAME = "Template básico - minicurso de PyGame"

WIDTH = 480
HEIGHT = 600

FPS = 30

#definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(GAME_NAME)

        self.running = True
        self.win = False

        self.all_sprites = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            event_type = event.type

            if event_type == pygame.QUIT:
                self.running = False
            
            if event_type == pygame.KEYDOWN:
                key = event.key

                if key == pygame.K_ESCAPE:
                    self.running = False
        
        self.player.set_speedx(0)

        key_state = pygame.key.get_pressed()

        if key_state[pygame.K_LEFT]:
            self.player.set_speedx(-20)
        elif key_state[pygame.K_RIGHT]:
            self.player.set_speedx(20)
    
    def update(self):
        
        pygame.display.update()
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
        
    
    def loop(self):
        
        while self.running:
            self.clock.tick(FPS)

            self.handle_events()
            self.update()
            self.draw()

    def run(self):
        self.player = Player(GREEN, ((WIDTH / 2), HEIGHT - 100))
        self.all_sprites.add(self.player)

        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.65)

        self.loop()

def main():
    game = Game()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()