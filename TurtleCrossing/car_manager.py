from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_SPEED = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.resizemode("user")
        self.shape("square")
        self.shapesize(stretch_wid=1.0, stretch_len=2.0, outline=None)  # Original shape is (20.0, 20.0)
        self.color(random.choice(COLORS))

        self.penup()
        self.goto(x=320, y=random.randint(-250, 250))
        self.setheading(180)

    def move(self):
        self.forward(MOVE_SPEED)
