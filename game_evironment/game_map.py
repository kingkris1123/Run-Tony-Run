from pygame import *

# import game window
from game_evironment.game_window import *

# import gif manager
import imageio

from game_maps.map_one import *
from game_maps.map_two import *
from game_maps.map_three import *

background_gif_path = 'visual_assets/backgrounds/Jungle/Jungle.gif'
background_gif = imageio.get_reader(background_gif_path)
background_gif_frames = [
    pygame.transform.flip(pygame.transform.scale(pygame.transform.rotate(pygame.surfarray.make_surface(frame), 90), (SCREEN_WIDTH, SCREEN_HEIGHT)), False, True)
    for frame in background_gif
]

frame_index = 0

# game variables for grid
ROWS = 15
MAXIMUM_COLUMNS = 100
TILES = SCREEN_HEIGHT // ROWS

#load in images
dirt_base = pygame.image.load('visual_assets/environment_tiles/ground5.png')
portal_img = pygame.image.load('visual_assets/environment_tiles/portal_image.png')
diamond_img = pygame.image.load('visual_assets/environment_tiles/diamond.png')

class Map():
    all = []
    map_count = 1

    def __init__(self, map_data=[]):
        self.tile_list = []

        self.portal_list = []
        self.temp_portal_list = []

        self.diamond_list = []
        self.temp_diamond_list = []

        self.width = len(map_data[0])
        self.height = len(map_data)
        self.map_number = Map.map_count
        Map.map_count += 1
        Map.all.append(self)
        
        row_number = 0
        for row in map_data:
            column_number = 0
            for tile in row:
                if tile == 1:
                    image = pygame.transform.scale(dirt_base, (TILES, TILES))
                    image_box = image.get_rect()
                    image_box.x = column_number * TILES
                    image_box.y = row_number * TILES
                    tile = (image, image_box)
                    self.tile_list.append(tile)
                if tile == 2:
                    image = pygame.transform.scale(diamond_img, (TILES * 0.75, TILES * 0.75))
                    image_box = image.get_rect()
                    image_box.x = column_number * TILES
                    image_box.y = row_number * TILES
                    tile = (image, image_box)
                    self.diamond_list.append(tile)
                    self.temp_diamond_list = [*self.diamond_list]
                if tile == 3:
                    image = pygame.transform.scale(portal_img, (TILES, TILES))
                    image_box = image.get_rect()
                    image_box.x = column_number * TILES
                    image_box.y = row_number * TILES
                    tile = (image, image_box)
                    self.portal_list.append(tile)
                    self.temp_portal_list = [*self.portal_list]
                column_number += 1
            row_number += 1
    
    def __repr__(self):
        return f'Map(Number = {self.map_number})'
        
    def draw (self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (155, 0, 0), tile[1], 2)

class Camera():
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    # applies the camera to an entity and displays map based on position
    def apply_camera(self, entity, player):
        initial_shift = max(0, player.rect.x - SCREEN_WIDTH // 2)
        screen_tuple = (self.camera.topleft[0] - initial_shift, self.camera.topleft[1])
        return entity.move(screen_tuple)
    
    # follows the sprite and shifts camera accordingly
    def update (self, player):
        if player.rect.x >= SCREEN_WIDTH // 2:
            x = player.rect.x - int(SCREEN_WIDTH // 2)
            self.camera = pygame.Rect(x, 0, self.width, self.height)
    
    def reset(self):
        self.camera = pygame.Rect(0, 0, self.width, self.height)

# camera instance
camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

map_1 = Map(map_one_data)
map_2 = Map(map_two_data)

# current_map = map_1