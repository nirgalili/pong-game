from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, start_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.start_position = start_position
        self.penup()
        self.goto(start_position)


    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)






