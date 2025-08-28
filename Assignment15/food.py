import random
import arcade

class Food(arcade.Sprite):
    def __init__(self, game_width, game_height, image_file):
        super().__init__(image_file)
        self.center_x = random.randint(0, game_width)
        self.center_y = random.randint(0, game_height)
        self.width = 25
        self.height = 25
