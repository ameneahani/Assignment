import arcade

class Spaceship(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__(':resources:/images/space_shooter/playerShip1_blue.png')
        self.width = 50
        self.height = 50
        self.center_x = width/2
        self.center_y = self.height
        self.speed = 5