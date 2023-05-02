from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)  # Set heading north because player can only move up.

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)

    def detect_collision(self, screen):
        """
        Detects if player collides with car. Calls screen.turtles() to list every turtle generated in screen.
        :param screen:
        :return bool:
        """
        for car in screen.turtles()[1:]:  # Player is the first turtle.
            if abs(self.xcor() - car.xcor()) < 20 and abs(self.ycor() - car.ycor()) < 10:
                return True
        return False

