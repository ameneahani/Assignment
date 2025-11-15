import time
import arcade
from snake import Snake
from pear import Pear
from apple import Apple
from shit import Shit

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 800, height = 600, title='Snake Game')
        arcade.set_background_color(color = arcade.color.KHAKI)
        self.snake = Snake()
        self.apple = Apple(self.width, self.height)
        self.pear = Pear(self.width, self.height)
        self.shit = Shit(self.width, self. height)
        self.game_over_bg = arcade.load_texture("gameover.png")
        self.game_over_time = None
        self.score = 0
        self.flag = ""

    def on_draw(self):
        arcade.start_render()
        if self.flag == "game_over":
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.game_over_bg)
            if time.time()-self.game_over_time > 3:
                exit(0)
        else:
            arcade.draw_text("score : " + str(self.score), self.width-150, 50, arcade.color.RED, 15, 2)
            self.snake.draw()
            self.apple.draw()
            self.pear.draw()
            self.shit.draw()

    def on_update(self, delta_time):
        
        if (self.snake.center_x + self.snake.speed) < self.apple.center_x and self.snake.change_x!=-1:
            self.snake.change_y = 0
            self.snake.change_x = 1
        elif (self.snake.center_x - self.snake.speed) > self.apple.center_x and self.snake.change_x!=1:
            self.snake.change_y = 0
            self.snake.change_x = -1
        else:
            self.snake.change_x = 0
            if (self.snake.center_y+self.snake.speed) < self.apple.center_y and self.snake.change_y!=-1:
                self.snake.change_y = 1
            elif (self.snake.center_y - self.snake.speed) > self.apple.center_y and self.snake.change_y!=1:
                self.snake.change_y = -1
            else:
                self.snake.change_y = 0

        nish = self.snake.move()
        if nish == 1:
            self.flag = "game_over"
            self.game_over_time = time.time()
        
        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat(self.apple)
            self.score += 1
            self.apple = Apple(self.width, self.height)

        if arcade.check_for_collision(self.snake, self.pear):
            self.snake.eat(self.pear)
            self.score += 2
            self.pear = Pear(self.width, self.height)
        
        if arcade.check_for_collision(self.snake, self.shit):
            self.snake.eat(self.shit)
            self.score -= 1
            if self.score == 0:
                self.flag = "game_over"
                self.game_over_time = time.time()
            self.shit = Shit(self.width, self.height)

        if self.snake.center_x < 0 or self.snake.center_x > self.width or self.snake.center_y < 0 or self.snake.center_y > self.height:
            if self.flag != "game_over":
                self.flag = "game_over"
                self.game_over_time = time.time()


        
        


win = Game()
arcade.run()

