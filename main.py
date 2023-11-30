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

# import health bar class 
# from shooting_gameplay.health_bar import *

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

# # camera instance
# camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

# player instance
player = Player(25, 500, 1.5, 5, 10)

# health_bar = HealthBar(250,200,300,40,100)


# start
start_game = True

# state of game over (prompts the game over screen)
game_over = False
game_running = True

# set the game with while loop
while game_running:
    
    if start_game:
        pass

    if not game_over:
        clock.tick(FPS)

        # background gif image
        screen.blit(background_gif_frames[frame_index], (0, 0))
        frame_index = (frame_index + 1) % len(background_gif_frames)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {player.score}", True, WHITE)
        screen.blit(score_text, (25, 25))

        # update the camera position
        player.update()

        # player movement
        player.move_character(move_left, move_right, jump, move_down)

        # update the camera based on the player
        camera.update(player)

        # draws elements based on camera view
        # draws tiles based on camera
        for tile in current_map.tile_list:
            screen.blit(tile[0], (tile[1][0] - camera.camera.topleft[0], tile[1][1]))

        # draws diamonds based on camera
        for diamond in current_map.temp_diamond_list:
            screen.blit(diamond[0], (diamond[1][0] - camera.camera.topleft[0], diamond[1][1]))

        #draws portal based on camera
        for portal in current_map.temp_portal_list:
            screen.blit(portal[0], (portal[1][0] - camera.camera.topleft[0], portal[1][1]))

        # draw character to the camera
        player_surface = player.draw()
        screen.blit(player_surface, (player.rect.x - camera.camera.topleft[0], player.rect.y))

        # put in game over death here
        if int(player.rect.top + 10) > SCREEN_HEIGHT:
            game_over = True

       # detect a collision with the "tunnel object" then increment the variable to the next integer
        # if player.rect.colliderect("rectangle"):
        #     current_map += 1

        # update the display for the gameplay
        pygame.display.update()
            
    else:
        game_over_screen(player.score)

        # update the display after showing game over screen
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                    
            game_keys = pygame.key.get_pressed()

            if any(game_keys) and game_over:
                if pygame.key.get_mods():
                    # Reset all key states
                    pygame.key.set_mods(0)

            # Ensure space key restarts the game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Reset player instance
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
                # if Player.player_direction == 'run_right' or Player.player_direction == 'idle_right':
                #     Player.player_direction = "jump_right"
                # else:
                #     Player.player_direction = "jump_left"
                
            # shoot bullets
            # if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            #     shoot = True

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

            # stop shooting bullets
            # if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            #     shoot = False

            # to be used in future (duck feature)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down = False
            
        #draw health bar 
        # health_bar.draw(screen)
        # updates window with all functions (aka displays images / characters)
        # pygame.display.update()

pygame.quit()
