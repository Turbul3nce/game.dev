import pygame
import sys
import random

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("PongX")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1500, 1100))
        
        # Initialize mixer for sounds
        pygame.mixer.init()
        
        # Load sound effects
        self.bounce_sound = pygame.mixer.Sound("assets/bounce.mp3")  # Ball bounces off paddle or wall
        self.score_sound = pygame.mixer.Sound("assets/score.mp3")    # Player scores a point
        
        # Player positions
        self.player1_pos = [0, 500]  # x, y coordinates for PLAYER1
        self.player2_pos = [1460, 500]  # x, y coordinates for PLAYER2
        
        # Movement flags
        self.player1_movement = [False, False]  # [move_up, move_down]
        self.player2_movement = [False, False]  # [move_up, move_down]
        
        # Ball position and velocity
        self.ball_pos = [750, 550]  # x, y coordinates for the ball
        self.ball_velocity = [0, 0]  # x, y velocity of the ball (initially zero)
        
        # Wall state
        self.wall_active = False  # Whether the wall is active
        self.wall_timer = 0  # Timer for toggling the wall
        
        # Player scores
        self.player1_score = 0
        self.player2_score = 0
        
        # Game state
        self.running = True  # Whether the game is ongoing
        self.start_delay = True  # Whether the game is in the starting delay
        
        # Font for displaying the scoreboard and winner
        self.font = pygame.font.Font(None, 74)
        self.winner_font = pygame.font.Font(None, 100)

    def run(self):
        self.start_game()  # Pause the game at the start

        while self.running:
            self.screen.fill((1, 1, 1))
            
            # Draw the players
            player1 = pygame.draw.rect(self.screen, (255, 255, 255), (*self.player1_pos, 40, 150))  # PLAYER1
            player2 = pygame.draw.rect(self.screen, (255, 255, 255), (*self.player2_pos, 40, 150))  # PLAYER2
            
            # Draw the wall (if active)
            if self.wall_active:
                wall = pygame.draw.rect(self.screen, (10, 255, 220), (715, 0, 55, 1500))
            else:
                wall = None
            
            # Draw the ball
            ball = pygame.draw.circle(self.screen, (255, 255, 255), self.ball_pos, 20)  # THE BALL
            
            # Draw the scoreboard
            player1_score_text = self.font.render(str(self.player1_score), True, (255, 255, 255))
            player2_score_text = self.font.render(str(self.player2_score), True, (255, 255, 255))
            self.screen.blit(player1_score_text, (50, 50))  # Player 1's score
            self.screen.blit(player2_score_text, (1400, 50))  # Player 2's score
            
            # Update Player 1 position
            if self.player1_movement[0] and self.player1_pos[1] > 0:  # Move up
                self.player1_pos[1] -= 5
            if self.player1_movement[1] and self.player1_pos[1] < 950:  # Move down
                self.player1_pos[1] += 5
            
            # Update Player 2 position
            if self.player2_movement[0] and self.player2_pos[1] > 0:  # Move up
                self.player2_pos[1] -= 5
            if self.player2_movement[1] and self.player2_pos[1] < 950:  # Move down
                self.player2_pos[1] += 5
            
            # Update ball position
            self.ball_pos[0] += self.ball_velocity[0]
            self.ball_pos[1] += self.ball_velocity[1]
            
            # Ball collision with top and bottom
            if self.ball_pos[1] <= 0 or self.ball_pos[1] >= 1080:
                self.ball_velocity[1] *= -1  # Reverse y-direction
                self.bounce_sound.play()  # Play bounce sound
            
            # Ball collision with player 1
            if self.player1_pos[0] - 20 <= self.ball_pos[0] <= self.player1_pos[0] + 40 and \
            self.ball_pos[1] in range(self.player1_pos[1] - 20, self.player1_pos[1] + 150 + 20):
                self.ball_velocity[0] = abs(self.ball_velocity[0])  # Ensure positive x-direction
                self.bounce_sound.play()  # Play bounce sound

            # Ball collision with player 2
            if self.player2_pos[0] - 20 <= self.ball_pos[0] <= self.player2_pos[0] + 40 and \
            self.ball_pos[1] in range(self.player2_pos[1] - 20, self.player2_pos[1] + 150 + 20):
                self.ball_velocity[0] = -abs(self.ball_velocity[0])  # Ensure negative x-direction
                self.bounce_sound.play()  # Play bounce sound

            # Ball collision with wall (if active)
            if self.wall_active and wall and ball.colliderect(wall):
                self.ball_velocity[0] = abs(self.ball_velocity[0]) # Reverse x-direction
                self.ball_velocity[1] = abs(self.ball_velocity[0]) # Reverse x-direction
                self.bounce_sound.play()  # Play bounce sound
            
            # Ball out of bounds
            if self.ball_pos[0] <= 0:  # Player 2 scores
                self.player2_score += 1
                self.score_sound.play()  # Play scoring sound
                self.reset_ball()
            if self.ball_pos[0] >= 1500:  # Player 1 scores
                self.player1_score += 1
                self.score_sound.play()  # Play scoring sound
                self.reset_ball()
            
            # Check for game over
            if self.player1_score == 10:
                self.display_winner("Player 1 Wins!")
            if self.player2_score == 10:
                self.display_winner("Player 2 Wins!")
            
            # Randomly toggle the wall
            self.wall_timer += 1
            if self.wall_timer >= random.randint(400, 800):  # Random time interval
                self.wall_active = not self.wall_active
                self.wall_timer = 0
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Player 1 Movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w: 
                        self.player1_movement[0] = True
                    if event.key == pygame.K_s:
                        self.player1_movement[1] = True
                if event.type == pygame.KEYUP: 
                    if event.key == pygame.K_w: 
                        self.player1_movement[0] = False
                    if event.key == pygame.K_s:
                        self.player1_movement[1] = False
                
                # Player 2 Movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_o: 
                        self.player2_movement[0] = True
                    if event.key == pygame.K_l:
                        self.player2_movement[1] = True
                if event.type == pygame.KEYUP: 
                    if event.key == pygame.K_o: 
                        self.player2_movement[0] = False
                    if event.key == pygame.K_l:
                        self.player2_movement[1] = False

            # Update display
            pygame.display.update()
            self.clock.tick(145)

    def reset_ball(self):
        """Reset the ball to the center with random initial velocity."""
        self.ball_pos = [750, 550]
        self.ball_velocity = [random.choice((-4, 4)), random.choice((-4, 4))]

    def start_game(self):
        """Pause the game at the start and release the ball after 3 seconds."""
        self.ball_pos = [800, 800]
        self.ball_velocity = [0, 0]
        pygame.time.wait(600) 
        self.ball_velocity = [4, random.choice((-4, 4))]

    def display_winner(self, message):
        """Display the winner and stop the game."""
        self.running = False
        winner_text = self.winner_font.render(message, True, (255, 255, 255))
        self.screen.fill((0, 0, 0))
        self.screen.blit(winner_text, (500, 500))
        pygame.time.wait(600)
        pygame.display.update()
        pygame.quit()
        sys.exit()

Game().run()

