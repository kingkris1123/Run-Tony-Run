import pygame

WIDTH = 1500
HEIGHT = 1000

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    def update (self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)
        self.camera = pygame.rect(x, y, self.width, self.height)