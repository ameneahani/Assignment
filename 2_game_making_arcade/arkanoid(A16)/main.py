import random
import time
import arcade

class Ball(arcade.Sprite):
    def __init__(self, paddle):
        super().__init__()
        self.radius = 5
        self.width = 2*self.radius
        self.height = 2*self.radius
        self.center_x = paddle.center_x
        self.center_y = paddle.center_y + paddle.height/2 + self.radius
        self.change_x = random.choice([-1,1])
        self.change_y = 1
        self.color = arcade.color.AERO_BLUE
        self.speed = 4

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

    def move(self, game):
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
            
        if  self.center_x >= game.width or self.center_x <= 0:
            self.change_x *= -1
        if self.center_y >= game.height:
            self.change_y *= -1
        

class Paddle(arcade.Sprite):
    def __init__(self, game_width, game_height):
        super().__init__("arkanoid\paddle.png")
        self.width = 50
        self.height = 10
        self.center_x = game_width//2
        self.center_y = game_height//15
        self.change_x = 0
        self.speed = 4

    def move(self, game):
        if self.center_x <self.width//2:
            self.center_x = self.width//2
        if self.center_x >= game.width-self.width//2:
            self.center_x = game.width-self.width//2
        self.center_x += self.change_x * self.speed


class Brick(arcade.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.width = 31
        self.height = 15
        self.color = color
        self.center_x = x
        self.center_y = y

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(self.center_x-self.width//2, self.center_x+self.width//2, self.center_y+self.height//2, self.center_y-self.height//2, self.color)
        arcade.draw_lrtb_rectangle_outline(self.center_x-self.width//2, self.center_x+self.width//2, self.center_y+self.height//2, self.center_y-self.height//2, arcade.color.DARK_BLUE)

class Life_count(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("arkanoid\paddle.png")
        self.center_x = x
        self.center_y = y
        self.width = 20
        self.height = 5


class Game(arcade.Window):
    def __init__(self, width = 500, height = 600, title = 'Arkanoid 2025'):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.score = 0
        self.brick_list = []
        for j in range(4):
            color = [arcade.color.GRAY, arcade.color.RED, arcade.color.ORANGE, arcade.color.YELLOW]
            for i in range(16):
                self.brick = Brick(color[j], 17+i*31, self.height*3/4-j*15)
                self.brick_list.append(self.brick)
        self.paddle = Paddle(self.width, self.height)
        self.ball = Ball(self.paddle)
        self.lifes = []
        for i in range(3):
            self.life = Life_count(30+i*22,10)
            self.lifes.append(self.life)
        self.flag = ""
        self.gameover_bg = arcade.load_texture("arkanoid\gameover.png")
        self.gameover_time = 0

    def on_draw(self):
        arcade.start_render()
        if self.flag == "game_over":
            arcade.draw_scaled_texture_rectangle(self.width//2, self.height//2, self.gameover_bg)
            if time.time() - self.gameover_time > 3:
                exit(0)
        else:
            arcade.draw_text(self.score, 30, self.height-30, arcade.color.ASH_GREY)
            for brick in self.brick_list:
                brick.draw()
            if self.lifes:
                for life in self.lifes:
                    life.draw()
            self.paddle.draw()
            self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.paddle.center_x = x

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.paddle.change_x = 1
        if symbol == arcade.key.LEFT:
            self.paddle.change_x = -1

    def on_key_release(self, symbol, modifiers):
        self.paddle.change_x = 0

    def on_update(self, delta_time):
        self.ball.move(self)
        self.paddle.move(self)

        for brick in self.brick_list:
            if arcade.check_for_collision(self.ball,brick):
                if self.brick_list:
                    self.brick_list.remove(brick)
                    self.score += 10
                    self.ball.change_y *= -1
        if arcade.check_for_collision(self.ball, self.paddle):
            self.ball.change_y *= -1
        if self.ball.center_y < 0:
            del self.ball
            self.ball = Ball(self.paddle)
            self.score -= 10
            if self.lifes:
                self.lifes.pop(0)
                if not self.lifes:
                    self.flag = "game_over"
                    self.gameover_time = time.time()
                    
        


game = Game()
arcade.run()
