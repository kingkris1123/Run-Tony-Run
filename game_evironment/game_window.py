import pygame

clock = pygame.time.Clock()
FPS = 60

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
# def draw_background():
#     screen.fill(BLACK)

    # makes a line for the floor!
    # pygame.draw.line(screen, RED, (0, 750), (990, 750))

# def start_game_screen():
#     screen.fill(BLACK)

#     header_text = pygame.font.SysFont('Times New Roman', 48)
#     # button_text = pygame.font.SysFont('Times New Roman', 24)

#     game_start = header_text.render('Run Tony Run', True, WHITE)
#     # start_button = button_text.render('Start Game', True, WHITE)

#     # screen.blit(start_button, (SCREEN_WIDTH/2 - start_button.get_width()/2, SCREEN_HEIGHT/2 + start_button.get_height()/2))
#     screen.blit(game_start, (SCREEN_WIDTH/2 - game_start.get_width()/2, SCREEN_HEIGHT/2 - game_start.get_height()/3))

def game_over_screen():
    screen.fill(BLACK)
    
    text = pygame.font.SysFont('Times New Roman', 60)
    title = text.render('YOU LOSE', True, WHITE)
    
    button_text = pygame.font.SysFont('Times New Roman', 36)
    button = button_text.render('Hit [space] to Play Again?', True, WHITE)

    # sets the game over title to the middle of the screen (divide by two for width and height of screen)
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/3 - title.get_height()/3))
    screen.blit(button, (SCREEN_WIDTH/2 - button.get_width()/2, SCREEN_HEIGHT/2 + button.get_height()/3))
    
    # waiting = True
    # while waiting:
    #     clock.tick(FPS)
    #     keys_down = pygame.key.get_pressed()

    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #         if not event.type == pygame.KEYDOWN:
    #             waiting = False