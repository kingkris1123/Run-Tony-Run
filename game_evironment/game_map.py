from pygame import *

# import game window
from game_evironment.game_window import *

# import gif manager
import imageio

from game_maps.map_one import *

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

class Map():
    def __init__(self, map_data):
        self.tile_list = []
        self.width = len(map_data[0])
        self.height = len(map_data)

        #load in images
        dirt_base = pygame.image.load('visual_assets/environment_tiles/ground5.png')
        
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
                column_number += 1
            row_number += 1
        
    def draw (self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

class Camera():
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    def apply_camera(self, entity):
        # gives a new rectangle based on the shift given as an argument
        return entity.move(self.camera.topleft)
    
    # follows the sprite and shifts camera accordingly
    def update (self, target):
        x = -target.rect.x + int(SCREEN_WIDTH / 2)
        # y = -target.rect.y + int(SCREEN_HEIGHT / 2)
        self.camera = pygame.Rect(x, 0, self.width, self.height)

map_one_map = Map(map_one_data)