from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

snake = Snake()

screen = Screen()
screen_width = 620
screen_height = 620
screen.setup(width=screen_width, height=screen_height, startx=None, starty=20)
screen.bgcolor('black')
screen.title("SNAKE GAME")
screen.tracer(0)

# Screen width and height divided by two to generate food within those coordinates.
food = Food(screen)

screen.listen()  # Focus on screen to receive inputs.
screen.onkey(fun=snake.move_up, key='Up')
screen.onkey(fun=snake.move_down, key='Down')
screen.onkey(fun=snake.move_left, key='Left')
screen.onkey(fun=snake.move_right, key='Right')

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh(screen)
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if (snake.head.xcor() >= screen_width/2) or (snake.head.ycor() >= screen_height/2) or \
           (snake.head.xcor() <= -screen_width/2) or (snake.head.ycor() <= -screen_height/2):
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with snake body.
    if snake.collision_with_body():
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()  # Exit screen on click only
