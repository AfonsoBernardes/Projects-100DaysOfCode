from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 40, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()

        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=75, y=240)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.goto(x=-75, y=240)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
