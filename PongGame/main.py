from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# Create game screen.
screen = Screen()
screen.tracer(False)
screen.bgcolor('black')
screen.setup(width=800, height=600, startx=None, starty=20)
screen.title("PONG GAME")

# Create left and right paddles, and the ball.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

# Make screen listen to keyboard inputs for left and right paddles.
screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")

screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

# Game loop.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    ball.bounce()
    ball.bounce_paddle(r_paddle, l_paddle)
    ball.out_of_bounds()

screen.exitonclick()
