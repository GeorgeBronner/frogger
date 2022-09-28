from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.up()
        self.y_speed = 10
        self.x_speed = 10

    def move(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_speed *= -1
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)
