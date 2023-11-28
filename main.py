# import pygame module
import pygame
from game_evironment.game_window import *

# import character / enemy class
from characters.player import *
from characters.enemy import *

# import icons / bullet class
from icons.bullet import * 

# import the map
from game_evironment.map_one import *

# initialize the pygame window
pygame.init()

# scrolling for map
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed =1


# sets game framerate
clock = pygame.time.Clock()
FPS = 60



#create sprite and update  groups 
bullet_group = pygame.sprite.Group()



# player action variables (how we move)
move_left = False
move_right = False
move_down = False
jump = False
shoot = False


# instance of the player class to be used (test instance)
player = Player(200, 200, 0.125, 5)
enemy = Enemy (200, 200, 0.125, 5)



bullet = Bullet(player.rect.centerx + (0.6 * player.rect.size[0] * player.direction) , player.rect.centery,player.direction)

# set the game with while loops
game_running = True
while game_running:

    clock.tick(FPS)

    draw_background()

    draw_grid()

    map_one_map.draw()

    # adds the player sprite to the window (passes the screen to put the image on the screen)
    player.draw(screen)
    player.move_character(move_left, move_right, jump, move_down)

    # adds the enemy sprite to the window (passes the screen to put the image on the screen)
    enemy.draw(screen)
    enemy.move_character(move_left, move_right, jump, move_down)

    # update and draw groups 
    bullet_group.update()
    bullet_group.draw(screen)

 


    for event in pygame.event.get():
        # switches game_running to false and allow user to quit game on closing the window
        if event.type == pygame.QUIT:
            game_running = False
        
        # key presses by user (control sprite movement / exit game)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_SPACE:
                jump = True
            if event.key == pygame.K_LSHIFT:
                shoot = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down = True
            if event.key == pygame.K_ESCAPE:
                game_running = False

        #key release (stop character movement)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_SPACE:
                jump = False
            if event.key == pygame.K_LSHIFT:
                shoot = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down = False

    # updates window with all functions (aka displays images / characters)
    pygame.display.update()


pygame.quit()