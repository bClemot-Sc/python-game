### Little game with insects ###
## Author : Bastien Clémot


## ----- Libraries
import pygame
import sys


## ----- Window initialization

# Start game
pygame.init()
# Set colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
# Window size
WINDOW_SIZE = (400,400)
# Create window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("The Insect Game")


## ----- Game initialization
# Grid size
GRID_SIZE = 20
CELL_SIZE = WINDOW_SIZE[0] // GRID_SIZE
# Player start
player_x,player_y = 0,0


## ----- Game script
# Lauch game
running = True
while running:

    # Inputs
    for event in pygame.event.get():

        # Stop game
        if event.type == pygame.QUIT:
            running = False
        
        # Move player
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_y > 0:
                player_y -= 1
            elif event.key == pygame.K_DOWN and player_y < GRID_SIZE - 1:
                player_y += 1
            elif event.key == pygame.K_LEFT and player_x > 0:
                player_x -= 1
            elif event.key == pygame.K_RIGHT and player_x < GRID_SIZE - 1:
                player_x += 1

    # Delete screen
    screen.fill(BLACK)

    # Draw grid
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x*CELL_SIZE,y*CELL_SIZE,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,WHITE,rect,1)

    # Player sprite
    player_rect = pygame.Rect(
        player_x*CELL_SIZE,player_y*CELL_SIZE,CELL_SIZE,CELL_SIZE
    )
    pygame.draw.rect(screen,GREEN,player_rect)

    # Update window
    pygame.display.flip()


## ----- Quit Game
pygame.quit()
sys.exit()


    

