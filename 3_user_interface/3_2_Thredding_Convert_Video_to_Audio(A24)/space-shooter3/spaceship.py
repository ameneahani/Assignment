import arcade
from bullet import Bullet
class Spaceship(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__(':resources:/images/space_shooter/playerShip1_blue.png')
        self.width = 50
        self.height = 50
        self.center_x = width/2
        self.center_y = self.height
        self.change_x = 0
        self.change_y = 0
        self.speed = 8
        self.bullets = []
        self.fire_sound = arcade.Sound(":resources:/sounds/laser2.wav")

    def fire(self):
        self.new_bullet = Bullet(self)
        self.bullets.append(self.new_bullet)
        self.fire_sound.play()

    def move(self , game_width):
        self.center_x  += self.change_x * self.speed
        if self.center_x < 0 :
            self.change_x = 0
            self.center_x = 0
        elif game_width < self.center_x:
            self.change_x = 0
            self.center_x = game_width
        
            
