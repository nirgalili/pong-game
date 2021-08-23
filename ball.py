from turtle import Turtle
import random

rand_heading_in_quarter = random.randint(22, 68)
rand_quarter_heading = random.randint(0, 3) * 90
rand_heading = rand_quarter_heading + rand_heading_in_quarter

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(rand_heading)

    def move(self):
        self.forward(3)

    def change_y_heading(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def change_x_heading(self):
        new_heading = 180 - self.heading()
        self.setheading(new_heading)

