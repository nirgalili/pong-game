from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

START_POSITION_RIGHT = (370, 0)
START_POSITION_LEFT = (-370, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My pong game")

screen.tracer(0)
paddle_right = Paddle(START_POSITION_RIGHT)
paddle_left = Paddle(START_POSITION_LEFT)
ball = Ball()
time.sleep(0.2)
screen.update()


screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    ball.move()
    screen.update()

    if abs(ball.ycor()) >= 286:
        ball.change_y_heading()

    if ball.xcor() > 350 and ball.distance(paddle_right) < 61:
        ball.change_x_heading()

    if ball.xcor() < -350 and ball.distance(paddle_left) < 61:
        ball.change_x_heading()

    if ball.xcor() > 380:
        screen.title("Left paddle wins!")
        game_is_on = False

    if ball.xcor() < -380:
        screen.title("Right paddle wins!")
        game_is_on = False

screen.exitonclick()