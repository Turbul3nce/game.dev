import pygame
import sys

# Make our game its own object (Object-oriented Programming)
class Game: 
    def __init__(self):
        # Setup pygame
        pygame.init()
        pygame.display.set_caption("Pixel Souls")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1920, 1280))

        # Load images and define screens/colors
        self.img = pygame.image.load('data/images/sky/cloud_1.png')
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [20, 20]  # Tuple instead of list
        self.movement = [False, False, False, False]

        self.collision_area = pygame.Rect(50, 50, 300, 50)
    
    def run(self):
        # Run the program. Allow user to exit
        while True: 
            
            # Warm desert orange color for the background
            self.screen.fill((244, 164, 96))
            
            # Vertical movement
            self.img_pos[1] += self.movement[1] - self.movement[0]
            
            # Horizontal movement
            self.img_pos[0] += self.movement[3] - self.movement[2]  
            
            # Blit background image and secondary image
            self.screen.blit(self.img, self.img_pos)

            # Setup collision
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 210), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 100, 210), self.collision_area)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Defining our movement keys:
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_w: 
                        self.movement[0] = True
                    if event.key == pygame.K_s:
                        self.movement[1] = True
                    if event.key == pygame.K_a: 
                        self.movement[2] = True
                    if event.key == pygame.K_d:
                        self.movement[3] = True

                if event.type == pygame.KEYUP: 
                    if event.key == pygame.K_w: 
                        self.movement[0] = False
                    if event.key == pygame.K_s: 
                        self.movement[1] = False
                    if event.key == pygame.K_a: 
                        self.movement[2] = False
                    if event.key == pygame.K_d:
                        self.movement[3] = False

            # Update the display and control frame rate
            pygame.display.update()
            self.clock.tick(60)  # Set FPS to 60

# Instantiate and run the game
Game().run()
