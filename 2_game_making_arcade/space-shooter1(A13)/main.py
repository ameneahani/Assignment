import random
import arcade
from spaceship import Spaceship
from enemy  import Enemy

class Game(arcade.Window):
    def __init__(self, width = 800, height = 600, title = 'Spaceships War'):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(':resources:/images/backgrounds/stars.png')
        self.spaceship = Spaceship(self.width, self.height)
        self.enemy = Enemy(self.width, self.height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width, self.height,self.background)
        self.spaceship.draw()
        self.enemy.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == 65363:
            self.spaceship.center_x += self.spaceship.speed
        if symbol == 65361:
            self.spaceship.center_x -= self.spaceship.speed

    def on_update(self, delta_time):
        self.enemy.center_y -= 1
        


window = Game()
arcade.run()

