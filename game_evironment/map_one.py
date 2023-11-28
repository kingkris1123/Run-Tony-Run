import pygame
from game_evironment.game_window import *

# game variables for grid
ROWS = 15
MAXIMUM_COLUMNS = 25
TILES = SCREEN_HEIGHT // ROWS

class World():
    def __init__(self, map_data):
        self.tile_list = []

        #load in images
        dirt_base = pygame.image.load('./environment_tiles/ground5.png')
        
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

# draw the map grid
def draw_grid():
    # vertical lines
    for column in range(MAXIMUM_COLUMNS + 1):
        pygame.draw.line(screen, WHITE, (column * TILES, 0), (column * TILES, SCREEN_HEIGHT))
    # horizontal lines
    for row in range(ROWS + 1):
        pygame.draw.line(screen, WHITE, (0, row * TILES), (SCREEN_WIDTH, row * TILES))

# list for populating world tiles
map_one_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
]

map_one_map = World(map_one_data)