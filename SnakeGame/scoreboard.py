from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # Open file containing the highest score recorded.
        with open('high_score_tracker.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, y=285)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score_tracker.txt', mode='w') as score_file:
                score_file.write(f"{self.high_score}")

        self.write(arg=f"SCORE: {self.score}    HIGHEST SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
