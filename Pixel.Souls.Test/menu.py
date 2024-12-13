import pygame
import sys

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.options = ["New Game", "Load Game", "Quit Game"]
        self.selected = 0

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))

            # Render menu options
            for i, option in enumerate(self.options):
                color = (255, 255, 255) if i == self.selected else (100, 100, 100)
                text = self.font.render(option, True, color)
                self.screen.blit(text, (300, 200 + i * 100))

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    if event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    if event.key == pygame.K_RETURN:
                        if self.selected == 0:
                            return "new_game"
                        elif self.selected == 1:
                            return "load_game"
                        elif self.selected == 2:
                            return "quit_game"

            pygame.display.flip()

