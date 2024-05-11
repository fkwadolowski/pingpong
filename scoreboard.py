from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.Score()

    def Score(self):
        self.write(f"{self.l_score}:{self.r_score}", align="center", font=('Courier', 24, 'normal'))
    def point_l(self):
        self.l_score+=1
        self.clear()
        self.Score()
    def point_r(self):
        self.r_score+=1
        self.clear()
        self.Score()

