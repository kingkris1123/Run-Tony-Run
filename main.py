# import pygame module
import pygame

# import audio control
from pygame import mixer

#import the game window
from game_evironment.game_window import *

# import the map
from game_evironment.game_map import *

# import character / enemy class
from characters.player import *
from characters.enemy import *

# import bullet class
from shooting_gameplay.bullet import *

# import health bar class 
from shooting_gameplay.health_bar import *

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

# initialize sound mixer
# mixer.init()
# jump_se = mixer.Sound('visual_assets/Grunt_Effect.mp3')
# jump_se.set_volume(.15)

# player instance
player = Player(25, 500, 1.5, 5, 10)

# start
start_game = False

# state of game over (prompts the game over screen)
game_over = False
game_running = True

# score 
score = 0 

#mouse position
game_mouse = pygame.mouse.get_pos() 

# set the game with while loop
while game_running:
    
    if not start_game:
        clock.tick(90)
        screen.blit(background_gif_frames[frame_index], (0, 0))
        frame_index = (frame_index + 1) % len(background_gif_frames)

        start_screen()
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    start_game = True
                if event.key == pygame.K_m:
                    mute_sound()


    else:
        if not game_over:
            clock.tick(FPS)

            # background gif image
            screen.blit(background_gif_frames[frame_index], (0, 0))
            frame_index = (frame_index + 1) % len(background_gif_frames)

            score_board(player)
            sound_keys()

            # update the camera position
            player.update()

            # player movement
            player.move_character(move_left, move_right, jump, move_down)

            # update the camera based on the player
            camera.update(player)

            draw_world()

            # draw character to the camera
            player_surface = player.draw()
            screen.blit(player_surface, (player.rect.x - camera.camera.topleft[0], player.rect.y))

            # put in game over death here
            if int(player.rect.top + 10) > SCREEN_HEIGHT:
                game_over = True

            # update the display for the gameplay
            pygame.display.update()
                
        else:
            clock.tick(90)
            screen.blit(background_gif_frames[frame_index], (0, 0))
            frame_index = (frame_index + 1) % len(background_gif_frames)

            game_over_screen(player.score)

            # update the display after showing game over screen
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                        
                game_keys = pygame.key.get_pressed()

                if not any(game_keys) and game_over:
                    if pygame.key.get_mods():
                        # Reset all key states
                        pygame.key.set_mods(0)

                # Ensure space key restarts the game
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Reset player instance

                    start_game = False

                    player = Player(25, 500, 1.5, 5, 10)

                    # Reset camera positioning
                    camera.reset()

                    # resets temp lists to original values on reset
                    current_map.temp_diamond_list = [*current_map.diamond_list]
                    current_map.temp_portal_list = [*current_map.portal_list]

                    # Reset game_over variable
                    game_over = False

                # Clear the event queue after checking for new key presses
                pygame.event.clear()


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
                Player.player_direction = 'run_right'
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left = True
                Player.player_direction = 'run_left'
            if event.key == pygame.K_SPACE:
                jump = True
                # jump_se.play()
            if event.key == pygame.K_m and not pygame.key.get_mods() & pygame.KMOD_SHIFT:
                mute_sound()
            if event.key == pygame.K_m and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                mute_sound()
                mute_effects()

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
                Player.player_direction = 'idle_right'
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left = False
                Player.player_direction = 'idle_left'
            if event.key == pygame.K_SPACE:
                jump = False

            # to be used in future (duck feature)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down = False

pygame.quit()
