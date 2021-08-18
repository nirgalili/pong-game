import time
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)
paddle_right = Paddle()

time.sleep(0.5)
screen.update()


screen.exitonclick()