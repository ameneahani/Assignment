import arcade

class Heart(arcade.Sprite):
    def __init__(self):
        super().__init__("heart.png")
        self.width = 20
        self.height = 20
        self.center_x = 40
        self.center_y = 40

