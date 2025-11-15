import arcade
class Bullet(arcade.Sprite):
    def __init__(self, spaceship):
        super().__init__(":resources:/images/space_shooter/laserRed01.png")
        self.center_x = spaceship.center_x
        self.center_y = spaceship.center_y
        self.change_x = 0
        self.change_y = 0
        self.speed = 5

    def move(self, game_height, bullets):
        self.center_y += self.speed
        if game_height < self.center_y :
            bullets.remove(self)


