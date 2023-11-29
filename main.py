# import pygame module
import pygame

#import the game window
from game_evironment.game_window import *

# import the map
from game_evironment.game_map import *

# import character / enemy class
from characters.player import *
from characters.enemy import *

# import bullet class
from shooting_gameplay.bullet import *

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

# camera instance
camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

# player instance
player = Player(25, 500, 0.1, 5, 10)

# state of game over (prompts the game over screen)
game_over = False
game_running = True

# set the game with while loop
while game_running:
    
    if not game_over:
        clock.tick(FPS)

        # draw_background()
        screen.blit(background_gif_frames[frame_index], (0, 0))
        frame_index = (frame_index + 1) % len(background_gif_frames)

        # adds the player sprite to the window (passes the screen to put the image on the screen)
        # player.draw(screen)
        player.update()

        # player movement
        player.move_character(move_left, move_right, jump, move_down)

        # update the camera based on the player
        # camera.update(player)

        # draws elements based on camera view
        for tile in map_one_map.tile_list:
            screen.blit(tile[0], camera.apply_camera(tile[1]))

        screen.blit(player.sprite, camera.apply_camera(player.rect))

        # put in game over death here
        if int(player.rect.top + 10) > SCREEN_HEIGHT:
            game_over = True

        bullet_group.update()
        bullet_group.draw(screen)

        if player.alive:
            if shoot:
                bullet = Bullet(player.rect.center[0] + (player.rect.size[0] * player.direction), player.rect.center[1], player.direction)
                bullet_group.add(bullet)

        # update the display for the gameplay
        pygame.display.update()
            
    else:
        game_over_screen()

        # update the display after showing game over screen
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player = Player(25, 500, 0.1, 5, 10)  # Reset player
                    game_over = False  # Reset game_over flag


    for event in pygame.event.get():
        # switches game_running to false and allow user to quit game on closing the window
        if event.type == pygame.QUIT:
            game_running = False
        
        # key presses by user (control sprite movement / exit game)
        if event.type == pygame.KEYDOWN:

            # toggle fullscreen gameplay
            if event.key == pygame.K_f and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                pygame.display.toggle_fullscreen()

            # player movement controls
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_SPACE:
                jump = True

            # shoot bullets
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shoot = True

            # to be used in future (duck feature)  
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down = True

            # quit game via escape key    
            if event.key == pygame.K_ESCAPE:
                game_running = False

        #key release (stop character movement)
        if event.type == pygame.KEYUP:

            # player movement control end
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_SPACE:
                jump = False

            # stop shooting bullets
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shoot = False

            # to be used in future (duck feature)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down = False

        
            

        # updates window with all functions (aka displays images / characters)
        # pygame.display.update()
pygame.quit()