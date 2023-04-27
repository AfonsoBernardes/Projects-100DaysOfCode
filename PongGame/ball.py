import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.create_ball()
        self.move_speed = 0.1

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
            self.move_speed *= 0.9  # Increase ball speed every time it touches paddle.

    def out_of_bounds(self, scoreboard):
        if self.xcor() >= 380:
            scoreboard.l_point()
            self.reset_position()
        elif self.xcor() <= -380:
            scoreboard.r_point()
            self.reset_position()

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1  # Reset ball speed to initial speed.

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)
