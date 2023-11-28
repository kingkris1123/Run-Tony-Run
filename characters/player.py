import pygame

# game variable 
GRAVITY = 1

# player class to create the player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.y_velo = 0
        sprite = pygame.image.load('./blastoise.png')
        self.sprite = pygame.transform.scale(sprite, (int(sprite.get_width() * scale), int(sprite.get_height() * scale)))
        self.rect = self.sprite.get_rect()
        self.rect.center = (x,y)

    #assigns movement variables
    def move_character (self, move_left, move_right, jump, move_down):

        #reset movement variables via delta x/y
        dx = 0
        dy = 0

        # move character left/right
        if move_left:
            dx = -self.speed
        if move_right:
            dx = +self.speed
        
        # have character jump
        if jump:
            self.y_velo = -11
            self.jump = False

        if move_down:
            dy = +self.speed

        # set velo to be increased (move down) with gravity
        self.y_velo += GRAVITY
        
        # set a limit on velocity speed
        if self.y_velo > 11:
            self.y_velo = 11

        # move the changing y position of the sprite based on the velo movement
        dy += self.y_velo

        # make a floor collision (aka stop falling)
        if self.rect.bottom + dy > 750:
            # difference between bottom of character and floor (900)
            dy = 750 - self.rect.bottom

        self.rect.x += dx
        self.rect.y += dy


    # add player to screen
    def draw(self, screen):
        screen.blit(self.sprite, self.rect)