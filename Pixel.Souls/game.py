import pygame
from scripts.entities import PhysicsEntity
from scripts.utils import load_image
import sys

class Game: 
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Pixel Souls")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1740, 1380))
        self.display = pygame.Surface((480, 320))

        self.movement = [False, False]

        self.assets = {
            'hero': load_image('entities/hero.png')
        }

        self.hero = PhysicsEntity(self, 'hero', (50, 50), (8, 15))

    def run(self):
        while True: 

            self.display.fill((244, 164, 96))
            
            self.hero.update((self.movement[1] - self.movement[0], 0))
            self.hero.render(self.display)
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Defining our movement keys:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a: 
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                if event.type == pygame.KEYUP: 
                    if event.key == pygame.K_a: 
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))            
            pygame.display.update()
            self.clock.tick(140)

Game().run()
