import random
from turtle import Turtle
import time

class Frogger(Turtle):

    START_POSITION = -280

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.left(90)
        self.penup()
        self.goto(0, self.START_POSITION)

    def go_up(self):
        self.forward(10)


class Car(Turtle):

    # +/- Range that cars start in and reset to
    X_START = 400
    Y_START = 250
    CAR_SPEED = 15

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.up()
        self.color(random.random(), random.random(), random.random())
        self.goto(random.randint(-self.X_START, self.X_START), random.randint(-self.Y_START, self.Y_START))
        self.right(180)

    def move(self, turtle_position):
        self.forward(self.CAR_SPEED)
        if self.xcor() < -self.X_START:
            self.goto(-self.xcor(), self.ycor())
        if self.distance(turtle_position) < 20:
            print(f"Broke at {self.distance(turtle_position)}")
            return False
        return True

    def increase_speed(self):
        self.CAR_SPEED += 5

class Scoreboard(Turtle):

    score = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 280)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}")