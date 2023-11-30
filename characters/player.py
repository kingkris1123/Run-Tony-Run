import pygame

from game_evironment.game_map import *
from game_evironment.game_window import *
from shooting_gameplay.bullet import *

# game variable 
GRAVITY = 1

# player action variables (how we move)
move_left = False
move_right = False
move_down = False
jump = False
shoot = False

idle_frame_width = 21
idle_spritesheet = pygame.image.load('visual_assets/character_sprites/hero_idle.png').convert_alpha()

run_frame_width = 23
run_spritesheet = pygame.image.load('visual_assets/character_sprites/hero_running.png').convert_alpha()

jump_frame_width = 17
jump_spritesheet = pygame.image.load('visual_assets/character_sprites/hero_jump.png').convert_alpha()

idle_width, idle_height = idle_spritesheet.get_size()
idle_num_frames = int(idle_width / idle_frame_width)
idle_right_frames = []
for i in range(idle_num_frames):
    frame = idle_spritesheet.subsurface(pygame.Rect(i * idle_frame_width, 0, idle_frame_width, idle_height))
    idle_right_frames.append(frame)

run_width, run_height = run_spritesheet.get_size()
run_num_frames = int(run_width / run_frame_width)
run_right_frames = []
for i in range(run_num_frames):
    frame = run_spritesheet.subsurface(pygame.Rect(i * run_frame_width, 0, run_frame_width, run_height))
    run_right_frames.append(frame)

jump_width, jump_height = jump_spritesheet.get_size()
jump_num_frames = int(jump_width / jump_frame_width)
jump_right_frames = []
for i in range(jump_num_frames):
    frame = jump_spritesheet.subsurface(pygame.Rect(i * jump_frame_width, 0, jump_frame_width, jump_height))
    jump_right_frames.append(frame)


def invert_surface(surface, flip_horizontal = False, flip_vertical = False):
    return pygame.transform.flip(surface, flip_horizontal, flip_vertical)

idle_left_frames = [invert_surface(surface, flip_horizontal = True) for surface in idle_right_frames]
run_left_frames = [invert_surface(surface, flip_horizontal = True) for surface in run_right_frames]
jump_left_frames = [invert_surface(surface, flip_horizontal = True) for surface in jump_right_frames]

animations = {
    'run_right': run_right_frames,
    'run_left': run_left_frames,

    'idle_right': idle_right_frames,
    'idle_left': idle_left_frames,

    'jump_right': jump_right_frames,
    'jump_left': jump_left_frames
}

move_on = 0
current_map = None

if move_on < len(Map.all):
    current_map = Map.all[move_on]

elif move_on > len(Map.all):
    move_on = 0
    current_map = Map.all[move_on]

# player class to create the player sprite
class Player(pygame.sprite.Sprite):
    player_direction = 'idle_right'
    player_frame_count = 0
    number_change = 0

    def __init__(self, x, y, scale, speed, ammo):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.direction = 1
        self.flip = False
        self.y_velo = 0
        self.jump = False
        self.__set_sprite()
        self.rect = self.sprite.get_rect()
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.rect.center = (x, y)
        self.shoot_cooldown = 0
        self.health = 100
        self.max_health = self.health
        self.score = 0

    def __set_sprite(self):
        sprite = animations[Player.player_direction][Player.number_change]
        self.sprite = pygame.transform.scale(sprite, (int(sprite.get_width() * self.scale), int(sprite.get_height() * self.scale)))

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

        for tile in current_map.tile_list:

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

################################ DIAMOND ##############################

        for diamond in current_map.temp_diamond_list:
            if diamond[1].colliderect(self.rect.x + dx, self.rect.y + dy, self.width, self.height):
                
                current_map.temp_diamond_list.remove(diamond)
                self.score += 5

                # portal_collision_occurred = True  # Set flag to True after collision

################################ PORTAL ###############################
        # portal_collision_occurred = False  # Flag to track collision occurrence
        # continue_screen_active = None
        
        for portal in current_map.temp_portal_list:
            if portal[1].colliderect(self.rect.x + dx, self.rect.y + dy, self.width, self.height):
                print('you win')
                
                current_map.temp_portal_list.remove(portal)

                # portal_collision_occurred = True  # Set flag to True after collision

                game_over_screen(self.score)
                # continue_screen_active = True

                pygame.display.update()

        self.rect.x += dx
        self.rect.y += dy

    # add player to screen
    def draw(self):
        Player.player_frame_count += 1
        if Player.player_frame_count >= 8:
            Player.player_frame_count = 0
            Player.number_change = (Player.number_change + 1) % len(animations[Player.player_direction])
            if Player.number_change  >= 8:
                Player.number_change = 0
        
        self.__set_sprite()

        return self.sprite