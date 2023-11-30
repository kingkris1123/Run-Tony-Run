import pygame
from game_evironment.game_window import *
class HealthBar():
    def __init__(self,w,h,max_hp):
        self.x = 10
        self.y = 40
        self.w = w 
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp
    
    def draw (self,surface):
        #calculate health ratio 
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))


   