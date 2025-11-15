import random
import time
from threading import Thread
import arcade
from spaceship import Spaceship
from enemy  import Enemy
from bullet import Bullet
from heart import Heart

class Game(arcade.Window):
    def __init__(self, width = 800, height = 600, title = 'Spaceships War'):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(':resources:/images/backgrounds/stars.png')
        self.game_over = arcade.load_texture("gameover.png")
        self.spaceship = Spaceship(self.width, self.height)
        self.enemies = []
        self.enemy_speed = 2
        self.hearts = []
        self.score = 0
        for i in range(3):
            new_heart = Heart()
            new_heart.center_x += i*new_heart.width
            self.hearts.append(new_heart)
        self.explosion_sound = arcade.Sound(":resources:/sounds/explosion1.wav")
        self.flag = ""
        self.start_time = time.time()
        self.game_over_time = None
        self.thread = Thread(target= self.make_enemy)
        self.thread.start()

    def on_draw(self):
        arcade.start_render()
        if self.flag == "game_over":
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.game_over)
        else:
            arcade.draw_lrwh_rectangle_textured(0,0,self.width, self.height,self.background)
            arcade.draw_text("score :" +str(self.score), self.width-100, 50, arcade.color.RED, 15, 3)
            self.spaceship.draw()
            for heart in self.hearts:
                heart.draw()
            for enemy in self.enemies:
                enemy.draw()
            for bullet in self.spaceship.bullets:
                bullet.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.spaceship.change_x = 1
        if symbol == arcade.key.LEFT:
            self.spaceship.change_x = -1
        if symbol == arcade.key.SPACE:
            self.spaceship.fire()

    def on_key_release(self, symbol, modifiers):
        self.spaceship.change_x = 0

    def on_update(self, delta_time):
        self.spaceship.move(self.width)

        for enemy in self.enemies:
            enemy.move(self.enemies, self.hearts)
            if len(self.hearts) == 0:
                if self.flag != "game_over":
                    self.flag = "game_over"
                    self.game_over_time = time.time()
            if self.flag == "game_over":
                if  time.time() - self.game_over_time > 3:
                    exit(0)

        for bullet in self.spaceship.bullets:
            bullet.move(self.height, self.spaceship.bullets)
        for enemy in self.enemies:
            if arcade.check_for_collision(self.spaceship, enemy):
                self.flag = "game_over"
                self.game_over_time = time.time()

        for bullet in self.spaceship.bullets:
            for enemy in self.enemies:
                if arcade.check_for_collision(bullet, enemy):
                    self.explosion_sound.play()
                    self.enemies.remove(enemy)
                    self.score += 1
                    self.spaceship.bullets.remove(bullet)
                    break

    def make_enemy(self):
        while True:
            if self.flag == "game_over":
                break
            new_enemy = Enemy(self)
            self.enemies.append(new_enemy)
            self.enemy_speed += 0.1
            time.sleep(3)    

window = Game()
arcade.run()

