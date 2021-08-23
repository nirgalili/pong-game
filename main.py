from turtle import Turtle, Screen
from paddle import Paddle
import time

START_POSITION_RIGHT = (350, 0)
START_POSITION_LEFT = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My pong game")

screen.tracer(0)
paddle_right = Paddle(start_position=START_POSITION_RIGHT)
paddle_left = Paddle(start_position=START_POSITION_LEFT)
time.sleep(0.2)
screen.update()


screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()