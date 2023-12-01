import pygame

from pygame import mixer

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

mixer.init()
mixer.music.load('visual_assets/jungle_music.mp3')
mixer.music.play(-2)
mixer.music.set_volume(.2)

def mute_sound():
    if mixer.music.get_volume() > 0:
        mixer.music.set_volume(0)
    else:
        mixer.music.set_volume(.25)

def score_board(player):
    score_font = pygame.font.SysFont('Courier', 40)
    score_text = score_font.render(f"Score: {player.score}", True, WHITE)
    screen.blit(score_text, (35, 35))

def sound_keys():
    sound_font = pygame.font.SysFont('Courier', 18)
    music_text = sound_font.render(f"Mute Music: Press [m]", True, WHITE)
    effect_text = sound_font.render(f"Mute All: Press [shift + m]", True, WHITE)
    screen.blit(music_text, (SCREEN_WIDTH - music_text.get_width() - 25, 25))
    screen.blit(effect_text, (SCREEN_WIDTH - effect_text.get_width() - 25, 50))

def start_screen():
    # screen.fill(BLACK)
    
    text = pygame.font.SysFont('Courier', 98, True)
    title = text.render('RUN TONY RUN', True, WHITE)
    
    button_text = pygame.font.SysFont('Courier', 36, False)
    button = button_text.render('Hold [shift] and Press [space]', True, WHITE)

    # check mouseover and clicked conditions

    # sets the title to the middle of the screen (divide by two for width and height of screen)
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/3))
   
    screen.blit(button, (SCREEN_WIDTH/2 - button.get_width()/2, SCREEN_HEIGHT/1.75 + button.get_height()/3))

# game over sreen, draws over game
def game_over_screen(score=0):
    # screen.fill(BLACK)
    
    text = pygame.font.SysFont('Courier', 98, True)
    title = text.render('Better Luck Next Time', True, WHITE)

    score_text = pygame.font.SysFont('Courier', 60, True)
    title_score = score_text.render(f'Score: {score}', True, WHITE)
    
    button_text = pygame.font.SysFont('Courier', 40)
    button = button_text.render('Hit [space] to Play Again?', True, WHITE)

    # sets the game over title to the middle of the screen (divide by two for width and height of screen)
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2.75 - title.get_height()/3))
    screen.blit(title_score, (SCREEN_WIDTH/2 - title_score.get_width()/2, SCREEN_HEIGHT/2.25 + title_score.get_height()/3))
    screen.blit(button, (SCREEN_WIDTH/2 - button.get_width()/2, SCREEN_HEIGHT/1.75 + button.get_height()/3))

def continue_screen(score=0):
    # screen.fill(BLACK)
    
    text = pygame.font.SysFont('Courier', 75, True)
    title = text.render('Do you want to Continue?', True, WHITE)

    score_text = pygame.font.SysFont('Courier', 60, True)
    title_score = score_text.render(f'Current Score: {score}', True, WHITE)
    
    button_text = pygame.font.SysFont('Courier', 40)
    button = button_text.render('Hit [space] to Continue', True, WHITE)

    # sets the game over title to the middle of the screen (divide by two for width and height of screen)
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2.75 - title.get_height()/3))
    screen.blit(title_score, (SCREEN_WIDTH/2 - title_score.get_width()/2, SCREEN_HEIGHT/2.25 + title_score.get_height()/3))
    screen.blit(button, (SCREEN_WIDTH/2 - button.get_width()/2, SCREEN_HEIGHT/1.75 + button.get_height()/3))

def win_screen(score=0):
    # screen.fill(BLACK)
    
    text = pygame.font.SysFont('Courier', 60, True)
    title = text.render("You've done it!", True, WHITE)

    score_text = pygame.font.SysFont('Courier', 48, True)
    title_score = score_text.render(f'Total Score: {score}', True, WHITE)
    
    button_text = pygame.font.SysFont('Courier', 36)
    button = button_text.render('Hit [space] to Restart', True, WHITE)

    # sets the game over title to the middle of the screen (divide by two for width and height of screen)
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/3 - title.get_height()/3))
    screen.blit(title_score, (SCREEN_WIDTH/2 - title_score.get_width()/2, SCREEN_HEIGHT/2.5 + title_score.get_height()/3))
    screen.blit(button, (SCREEN_WIDTH/2 - button.get_width()/2, SCREEN_HEIGHT/2 + button.get_height()/3))