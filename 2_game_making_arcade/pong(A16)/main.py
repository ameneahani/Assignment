import random
import arcade


class Racket(arcade.Sprite):
    def __init__(self, center_x, game_height, color):
        super().__init__()
        self.width = 10
        self.height = 60
        self.center_x = center_x
        self.center_y = game_height//2
        self.change_x = 0
        self.change_y = 0
        self.color = color
        self.speed = 4
        self.score = 0

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(self.center_x-self.width/2, self.center_x+self.width/2, self.center_y+self.height/2, self.center_y -self.height/2, self.color)

    def move(self, game_height):
        self.center_y += self.change_y * self.speed
        if self.center_y > game_height - self.height//2 - 15:
            self.center_y = game_height - self.height//2 - 15
        elif self.center_y < self.height//2 + 15:
            self.center_y = self.height//2 + 15

    def move_ai(self,game, ball):
        if ball.center_x > game.width//2:
            if self.center_y < ball.center_y:
                self.change_y = 1
            elif self.center_y > ball.center_y:
                self.change_y = -1
        else:
            self.change_y = 0
        self.center_y += self.change_y * self.speed
        if self.center_y > game.height - self.height//2 - 15:
            self.center_y = game.height - self.height//2 - 15
        elif self.center_y < self.height//2 + 15:
            self.center_y = self.height//2 + 15

class Ball(arcade.Sprite):
    def __init__(self, game_width, game_height):
        super().__init__()
        self.radius = 11
        self.width = self.radius * 2
        self.height = self.radius * 2
        self.center_x = game_width/2
        self.center_y = game_height/2
        self.change_x = random.choice([-1,1])
        self.change_y = random.choice([-1,1])
        self.speed = 5
        self.color = arcade.color.YELLOW

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

    def move(self, game_height):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        if self.center_y < 30 or self.center_y > game_height-30:
            self.change_y *= -1


class Game(arcade.Window):
    def __init__(self, width = 850, height = 500, title = 'Pong Game 2025'):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.player_1 = Racket(30, self.height, arcade.color.RED)
        self.player_2 = Racket(self.width-30 , self.height, arcade.color.BLUE)
        self.ball = Ball(self.width, self.height)
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_1)
        self.player_list.append(self.player_2)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrtb_rectangle_outline(10, self.width-10, self.height-10,10,arcade.color.WHITE, 8)
        arcade.draw_line(self.width/2, 20,self.width/2, self.height-20, arcade.color.WHITE, 7)
        arcade.draw_text(self.player_1.score, 50, 50, arcade.color.WHEAT, 15)
        arcade.draw_text(self.player_2.score, self.width-50, 50, arcade.color.WHEAT, 15)
        self.ball.draw()
        self.player_1.draw()
        self.player_2.draw()
        arcade.finish_render()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.player_1.change_y = 1
        if symbol == arcade.key.DOWN:
            self.player_1.change_y = -1

    def on_key_release(self, symbol, modifiers):
        self.player_1.change_y = 0

    def on_update(self, delta_time):
        self.player_1.move(self.height)
        self.player_2.move_ai(self, self.ball)
        self.ball.move(self.height)

        if self.ball.center_x < 30:
            del self.ball
            self.ball = Ball(self.width, self.height)
            self.player_2.score += 1
        if self.ball.center_x > self.width:
            del self.ball
            self.ball = Ball(self.width, self.height)
            self.player_1.score += 1
            
        if arcade.check_for_collision_with_list(self.ball,self.player_list):
            self.ball.change_x *= -1


game = Game()
arcade.run()