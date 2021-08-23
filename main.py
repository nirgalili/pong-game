from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

TIME_SLEEP = 0.01
PACE = 3

START_POSITION_RIGHT = (370, 0)
START_POSITION_LEFT = (-370, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My pong game")
scoreboard = Scoreboard()
scoreboard.write_new_score()

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

pace = PACE
time_sleep = TIME_SLEEP
game_is_on = True
while game_is_on:
    time.sleep(time_sleep)
    ball.move(pace)
    screen.update()

    if abs(ball.ycor()) >= 286:
        ball.change_y_heading()

    if ball.xcor() > 350 and ball.distance(paddle_right) < 61:
        ball.change_x_heading()
        time_sleep = 0.9 * time_sleep
        print(time_sleep)

    if ball.xcor() < -350 and ball.distance(paddle_left) < 61:
        ball.change_x_heading()
        time_sleep = 0.9 * time_sleep
        print(time_sleep)

    if ball.xcor() > 380:
        time_sleep = TIME_SLEEP
        scoreboard.change_left_score()
        old_heading = ball.heading()
        ball.home()
        ball.setheading(180 - old_heading)

    if ball.xcor() < -380:
        time_sleep = TIME_SLEEP
        scoreboard.change_right_score()
        old_heading = ball.heading()
        ball.home()
        ball.setheading(180 - old_heading)

screen.exitonclick()