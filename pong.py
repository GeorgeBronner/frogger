from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_running = True
while game_running:
    screen.update()
    time.sleep(.1)
    ball.move()

# detect food collision
#     if snake.head.distance(food) < 17:
#         food.refresh()
#         scoreboard.add_to_score()
#         snake.extend()
#
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_running = False
#         scoreboard.game_over()
#
#     for i in snake.tim[1:]:
#         if snake.head.distance(i) < 10:
#             game_running = False

screen.exitonclick()
