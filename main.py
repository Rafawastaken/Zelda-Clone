import pygame
import sys

# Helpers
from level import Level
from settings import *
from debug import * 

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Zelda')

        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()

        # Level initializer
        self.level = Level()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')

            # Run level
            self.level.run()

            pygame.display.update()
            self.clock.tick(FPS)

            

if __name__ == '__main__':
    game = Game()
    game.run()