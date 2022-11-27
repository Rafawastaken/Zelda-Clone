import pygame
import sys

# Helpers
from settings import *
from debug import * 

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')

            debug('Hello')

            pygame.display.update()
            self.clock.tick(FPS)

            

if __name__ == '__main__':
    game = Game()
    game.run()