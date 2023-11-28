import pygame
import imageio
from game_evironment.game_window import *


# import character / enemy class
from characters.player import *
from characters.enemy import *

from game_evironment.map_one import *

# initialize the pygame window
pygame.init()

# sets game framerate
clock = pygame.time.Clock()
FPS = 60

background_gif_path = 'jungle50.gif'
background_gif = imageio.get_reader(background_gif_path)
# background_gif_frames = [pygame.transform.scale(pygame.surfarray.make_surface(frame), (SCREEN_WIDTH, SCREEN_HEIGHT)) for frame in background_gif]
background_gif_frames = [
    pygame.transform.flip(pygame.transform.scale(pygame.transform.rotate(pygame.surfarray.make_surface(frame), 90), (SCREEN_WIDTH, SCREEN_HEIGHT)), False, True)
    for frame in background_gif
]

frame_index = 0

# player action variables (how we move)
move_left = False
move_right = False
jump = False
move_down = False

# instance of the player class to be used (test instance)
player = Player(200, 200, 0.125, 5)

# set the game with while loop
game_running = True
while game_running:

    clock.tick(FPS)
    draw_background()
    draw_grid()
    map_one_map.draw()

    screen.blit(background_gif_frames[frame_index], (0, 0))
    # pygame.draw.line(screen, WHITE, (0, 750), (SCREEN_WIDTH, 750))

    # adds the player sprite to the window (passes the screen to put the image on the screen)
    player.draw(screen)
    player.move_character(move_left, move_right, jump, move_down)

    # adds the enemy sprite to the window (passes the screen to put the image on the screen)
        
    for event in pygame.event.get():
        # switches game_running to false and allow user to quit game on closing the window
        if event.type == pygame.QUIT:
            game_running = False

        # key presses by user to control sprite / exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
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
            if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                jump = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down = False

    pygame.display.update()

    frame_index = (frame_index + 1) % len(background_gif_frames)


pygame.quit()