import pygame

# player class to create the player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        sprite = pygame.image.load('./blastoise.png')
        self.sprite = pygame.transform.scale(sprite, (int(sprite.get_width() * scale), int(sprite.get_height() * scale)))
        self.rect = self.sprite.get_rect()
        self.rect.center = (x,y)

    #assigns movement variables
    def move_character (self, move_left, move_right, jump, move_down):

        #reset movement variables via delta x/y
        dx = 0
        dy = 0

        if move_left:
            dx = -self.speed

        if move_right:
            dx = +self.speed

        if jump:
            dy = -self.speed

        if move_down:
            dy = +self.speed

        self.rect.x += dx
        self.rect.y += dy



    def draw(self, screen):
        screen.blit(self.sprite, self.rect)