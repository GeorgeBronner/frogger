from turtle import Screen, Turtle
from logic import Frogger, Car, Scoreboard
import time

NUMBER_OF_CARS = 15

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Frogger Game")
screen.tracer(0)

screen.listen()
tim = Frogger()

cars = []
for i in range(NUMBER_OF_CARS):
    cars.append(Car())

scoreboard = Scoreboard()

screen.onkey(tim.go_up, "Up")

def move_cars():
    for i in cars:
        keep_playing = i.move((tim.xcor(), tim.ycor()))
        if not keep_playing:
            return False
    return keep_playing

def check_score():
    if tim.ycor() >= 300:
        scoreboard.score += 1
        tim.goto(0, tim.START_POSITION)
        for i in cars: i.increase_speed()
        scoreboard.refresh()

game_running = True
while game_running:
    screen.update()
    time.sleep(.1)
    game_running = move_cars()
    check_score()

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
