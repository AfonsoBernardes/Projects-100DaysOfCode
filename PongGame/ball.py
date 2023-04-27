import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.create_ball()

    def create_ball(self):
        self.color('white')
        self.resizemode("user")
        self.shape("circle")
        self.shapesize(stretch_wid=1.0, stretch_len=1.0, outline=None)  # Original shape is (20.0, 20.0)
        self.penup()

    def bounce(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.y_move *= -1  # Only change y direction.

    def bounce_paddle(self, r_paddle, l_paddle):
        """
        Detect collision with paddles
        """
        if (self.distance(r_paddle) <= 50 and self.xcor() >= 340) or \
                (self.distance(l_paddle) <= 50 and self.xcor() <= -340):
            self.x_move *= -1  # Only change y direction.

    def out_of_bounds(self):
        if self.xcor() >= 380 or self.xcor() <= -380:
            self.reset_position()

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)
