from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.right_score = 0
        self.left_score = 0

    def write_new_score(self):
        argument = f"Left {self.left_score} | Right {self.right_score} "
        self.write(argument, False, "center", FONT)

    def change_left_score(self):
        self.clear()
        self.left_score += 1
        self.write_new_score()

    def change_right_score(self):
        self.clear()
        self.right_score += 1
        self.write_new_score()