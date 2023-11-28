import pygame

# define RGB colors by
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (155, 0 , 0)

# set the window size to open to
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000

# window and title for window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Run Tony Run')

# keep the background refreshing which hides/clears old sprite instances
def draw_background():
    screen.fill(BLACK)

    # makes a line for the floor!
    pygame.draw.line(screen, RED, (0, 750), (990, 750))