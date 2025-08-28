import arcade

class Box(arcade.Window):
    def __init__(self, width = 600, height = 600, title = 'Complex Loops_Box'):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        for i in range(0, 10):
            for j in range(0,10):
                if (i+j)%2 !=0:
                    color = arcade.color.BLUE
                else:
                    color = arcade.color.RED
                arcade.draw_rectangle_filled(self.width//3+j*20, self.height//3+i*20, 10, 10, color, 135)

window = Box()
arcade.run()

