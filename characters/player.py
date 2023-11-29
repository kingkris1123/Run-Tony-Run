import pygame
from icons.bullet import * 

# game variable 
GRAVITY = 1

# player class to create the player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed, ammo):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo 
        self.direction = 1 
        self.flip = False
        self.y_velo = 0
        self.jump = False
        sprite = pygame.image.load('./blastoise.png')
        self.sprite = pygame.transform.scale(sprite, (int(sprite.get_width() * scale), int(sprite.get_height() * scale)))
        self.rect = self.sprite.get_rect()
        self.rect.center = (x,y)
        self.shoot_cooldown = 0 
        self.health = 100
        self.max_health = self.health

    
   
    

   

    
    #assigns movement variables
    def move_character (self, move_left, move_right, jump, move_down):

        #reset movement variables via delta x/y
        dx = 0
        dy = 0

        # move character left/right
        if move_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if move_right:
            dx = +self.speed
            self.flip = False
            self.direction = 1
        
        # have character jump
        if jump and not self.jump:
            self.y_velo = -20
            self.jump = True

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
            self.jump = False

        self.rect.x += dx
        self.rect.y += dy

        def shoot(self):
            if self.shoot_cooldown == 0 and self.ammo > 0:
                self.shoot_cooldown = 20 
            bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction) , self.rect.centery,self.direction)
            bullet_group.add(bullet)
            self.ammo -= 1
        
        def check_alive(self):
            if self.health <= 0:
               self.health = 0
               self.speed = 0
               self.alive = False

        

        def update(self):
		       self.check_alive()
		


			        


    # add player to screen
    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.sprite, self.flip, False), self.rect)