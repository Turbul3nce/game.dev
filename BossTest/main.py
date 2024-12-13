import pygame
import sys
from menu import Menu
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Test Project")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1920, 1280))
        self.running = True

    def run(self):
        # Show the menu
        menu = Menu(self.screen)
        choice = menu.run()
        
        # Handle menu choice
        if choice == "new_game":
            level = Level(self.screen)
            level.run()
        elif choice == "quit_game":
            self.running = False

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    while game.running:
        game.run()

