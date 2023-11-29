import pygame

from game_evironment.game_map import *
from shooting_gameplay.bullet import *

# game variable 
GRAVITY = 1

# player action variables (how we move)
move_left = False
move_right = False
move_down = False
jump = False
shoot = False

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
        sprite = pygame.image.load('visual_assets/character_sprites/blastoise.png')
        self.sprite = pygame.transform.scale(sprite, (int(sprite.get_width() * scale), int(sprite.get_height() * scale)))
        self.rect = self.sprite.get_rect()
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
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
            self.y_velo = -17
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

        for tile in map_one_map.tile_list:
            # x value is check for horizontal collision
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0

            # y value is check for any vertical collision
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.y_velo < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.y_velo = 0

                elif self.y_velo >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.y_velo = 0
                    self.jump = False

        self.rect.x += dx
        self.rect.y += dy

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
        bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery.self.direction)
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
