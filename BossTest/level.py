import pygame
import random

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.health = 3
        self.block_stamina = 2
        self.color = (0, 0, 255)
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

    def attack(self, boss):
        if self.rect.colliderect(boss.rect):
            boss.health -= 1

    def block(self, attack_rect):
        if self.rect.colliderect(attack_rect):
            if self.block_stamina > 0:
                self.block_stamina -= 1
                return True
            else:
                self.health -= 1
                return False
        return False


class Boss:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 100, 100)
        self.health = 10
        self.color = (255, 0, 0)
        self.speed = 3

    def move(self):
        self.rect.x += random.choice([-1, 1]) * self.speed
        self.rect.y += random.choice([-1, 1]) * self.speed


class Level:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(100, 300)
        self.boss = Boss(600, 300)
        self.running = True

    def run(self):
        clock = pygame.time.Clock()
        attack_rect = pygame.Rect(0, 0, 0, 0)

        while self.running:
            self.screen.fill((30, 30, 30))
            keys = pygame.key.get_pressed()

            # Draw the player and boss
            pygame.draw.rect(self.screen, self.player.color, self.player.rect)
            pygame.draw.rect(self.screen, self.boss.color, self.boss.rect)

            # Display health
            self.draw_health()

            # Player movement
            self.player.move(keys)

            # Player attack
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        self.player.attack(self.boss)
                    if event.button == 3:  # Right click
                        attack_rect = self.boss.rect.copy()
                        if self.player.block(attack_rect):
                            print("Blocked!")
                        else:
                            print("Took damage!")

            # Boss movement
            self.boss.move()

            # Check if game is over
            if self.boss.health <= 0:
                print("Boss defeated!")
                self.running = False
            if self.player.health <= 0:
                print("You died!")
                self.running = False

            pygame.display.flip()
            clock.tick(60)

    def draw_health(self):
        font = pygame.font.Font(None, 36)
        player_health_text = font.render(f"Player Health: {self.player.health}", True, (255, 255, 255))
        boss_health_text = font.render(f"Boss Health: {self.boss.health}", True, (255, 255, 255))
        self.screen.blit(player_health_text, (20, 20))
        self.screen.blit(boss_health_text, (20, 60))

