import pygame
from game_evironment.game_window import *
from characters.player import *


#load images 
# bullet 
bullet_img = pygame.image.load('visual_assets/shooting_assets/bullet.png')

#create sprite and update  groups 
bullet_group = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.direction = direction
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self):
        # move bullet 
        self.rect.x += (self.direction * self.speed)

        # check if bullet has gone off screen 
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH - 100:
            self.kill
