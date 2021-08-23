from turtle import Turtle, Screen
import time

START_POSITION_RIGHT = (350, 0)


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My pong game")

screen.tracer(0)
# time.sleep(0.2)
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(5, 1)

paddle.penup()
paddle.goto(START_POSITION_RIGHT)
screen.update()


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()