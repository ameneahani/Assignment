import arcade
from apple import Apple
class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = 100
        self.center_y = 100
        self.width = 20
        self.height = 20
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.head = arcade.load_texture("head.png")
        self.head_angle = 0
        self.body = []

    def draw(self):
        if self.body:
            for i in range(len(self.body)-1, -1, -1):
                if i%2 ==0:
                    snake_body_color = arcade.color.GREEN
                else :
                    snake_body_color = arcade.color.DARK_GREEN
                arcade.draw_rectangle_filled(self.body[i]['x'], self.body[i]['y'], self.width, self.height, snake_body_color)
        if self.change_x == 1:
            self.head_angle = 0
        elif self.change_x == -1:
            self.head_angle = 180
        elif self.change_y == 1:
            self.head_angle = 90
        else:
            self.head_angle = -90
        arcade.draw_texture_rectangle(self.center_x, self.center_y, 35, 35 ,self.head, self.head_angle+90)

    def move(self):
        prev_x = self.center_x
        prev_y = self.center_y
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        
        if self.body:
            for i in range(len(self.body)-1, 0 , -1):
                self.body[i]['x'] = self.body[i-1]['x']
                self.body[i]['y'] = self.body[i-1]['y']

            self.body[0]['x'] = prev_x
            self.body[0]['y'] = prev_y

            for segment in self.body:  
                if segment['x'] == self.center_x and segment['y'] == self.center_y:
                    return 1  # برخورد با بدن
            return 0 
        

    def eat(self, food):
        if type(food) == Apple:
            self.body.append({'x':self.center_x,'y':self.center_y})
        del food
    
 

        


