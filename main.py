from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

#currently the block
player = PlatformerController2d(y=10, scale_y=1, max_jumps=2)

#currently the platform on which you can stand
ground = Entity(model='quad', scale_x=100, y=-5, collider='box', color=color.white)

# get run on each page to determine location of block and where to move in
def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt

# specific function to increase the vertical height of the character 'jump'
# the invoke setattr returns the player to the original y position (-1) after a .25 second jump
def input(key):
    if key == 'space':
        player.y =+ 1
        invoke (setattr, player, 'y', player.y-1, delay=.25)

app.run()