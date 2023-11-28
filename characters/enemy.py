import pygame

# player class to create the player sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
       
        self.speed = speed
        self.direction = 1 
        self.flip = False
        sprite = pygame.image.load('./blastoise.png')
        self.sprite = pygame.transform.scale(sprite, (int(sprite.get_width() * scale), int(sprite.get_height() * scale)))
        self.rect = self.sprite.get_rect()
        self.rect.center = (x,y)

    # assigns movement variables
    def move_character (self, move_left, move_right, jump, move_down):

        #reset movement variables via delta x/y
        dx = 0
        dy = 0

        if move_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1


        if move_right:
            dx = +self.speed
            self.flip = False
            self.direction = 1


        if jump:
            dy = -self.speed

        if move_down:
            dy = +self.speed

        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.sprite, self.flip, False), self.rect)