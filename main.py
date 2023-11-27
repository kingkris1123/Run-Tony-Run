import pygame
# import character / enemy class
from characters.player import *
from characters.enemy import *

# initialize the pygame window
pygame.init()

# set the window size to open to
SCREEN_WIDTH = 1750
SCREEN_HEIGHT = (SCREEN_WIDTH * 0.75)

# window and title for window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Run Tony Run')

# sets game framerate
clock = pygame.time.Clock()
FPS = 60

# player action variables
move_left = False
move_right = False
jump = False
move_down = False

# define background
bg = (0,0,0)

# keep the background refreshing which hides/clears old sprite instances
def background():
    screen.fill(bg)

# instance of the player class to be used (test instance)
player = Player(200, 200, 0.125, 5)
enemy = Enemy(1500, 300, 0.125, 5)





# set the game 
game_running = True
while game_running:

    clock.tick(FPS)
    background()

    # adds the player sprite to the window (passes the screen to put the image on the screen)
    player.draw(screen)
    player.move_character(move_left, move_right, jump, move_down)

    # adds the enemy sprite to the window (passes the screen to put the image on the screen)
    enemy.draw(screen)

    for event in pygame.event.get():
        # switches game_running to false and allow user to quit game on closing the window
        if event.type == pygame.QUIT:
            game_running = False
        
        # key presses by user to control sprite
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_w:
                jump = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down = True
            if event.key == pygame.K_ESCAPE:
                game_running = False

        #key release (aka stop character movement)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_w:
                jump = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down = False

    pygame.display.update()


pygame.quit()