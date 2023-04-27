from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh(screen)

    def refresh(self, screen):
        screen_half_width = screen.window_width() // 2
        screen_half_height = screen.window_height() // 2

        random_x = random.randint(-screen_half_width + 50, screen_half_width - 50)
        random_y = random.randint(-screen_half_height + 50, screen_half_height - 50)
        self.goto(x=random_x, y=random_y)
