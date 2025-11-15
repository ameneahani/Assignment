from food import Food

class Pear(Food):
    def __init__(self, game_width, game_height):
        super().__init__(game_width, game_height, "pear.png")

