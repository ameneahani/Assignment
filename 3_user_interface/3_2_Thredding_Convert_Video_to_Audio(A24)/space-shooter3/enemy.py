import random
import time
import arcade

class Enemy(arcade.Sprite):
    def __init__(self, game):
        super().__init__(':resources:/images/space_shooter/playerShip1_orange.png')
        self.width = 50
        self.height = 50
        self.center_x = random.randint(0, game.width)
        self.center_y = game.height
        self.change_x = 0
        self.speed = game.enemy_speed
        self.angle = 180

    def move(self, game_enemies, game_hearts):
        self.center_y -= self.speed
        
        if self.center_y < 0 :
            game_enemies.remove(self)
            if len(game_hearts) > 0:
                game_hearts.pop(0)
            
    
 