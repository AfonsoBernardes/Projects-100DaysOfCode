from turtle import Turtle
import car_manager
import player

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-290, y=260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1

    def check_finish(self, user):
        if user.ycor() >= player.FINISH_LINE_Y:
            user.goto(player.STARTING_POSITION)
            self.increase_level()
            car_manager.MOVE_SPEED += car_manager.MOVE_INCREMENT

    def game_over(self):
        self.goto(x=0.0, y=0.0)
        self.write("GAME OVER", align="center", font=FONT)
