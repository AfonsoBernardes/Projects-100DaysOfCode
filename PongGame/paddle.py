from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position: tuple):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position: tuple):
        self.color('white')
        self.resizemode("user")
        self.shape("square")

        # Original shape is (20.0, 20.0)
        self.shapesize(stretch_wid=5.0, stretch_len=1.0, outline=None)
        self.penup()
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
