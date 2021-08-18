from turtle import Turtle
STARTING_POSITION = [(350, -50), (350, -30), (350, -10), (350, 10), (350, 30), (350, 50)]
MOVE_DIST = 20
UP = 90
DOWN = 270

class Paddle():

    def __init__(self):
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for position in STARTING_POSITION:
            new_seg = Turtle(shape="square")
            new_seg.penup()
            new_seg.color("white")
            new_seg.goto(position)
            self.segments.append(new_seg)





