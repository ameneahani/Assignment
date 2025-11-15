import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__(':resources:/images/space_shooter/playerShip1_orange.png')
        self.width = 50
        self.height = 50
        self.center_x = random.randint(0, width)
        self.center_y = height 
        self.angle = 180
 