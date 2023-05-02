import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600, startx=None, starty=20)
screen.tracer(False)
screen.title("Road Crossing")

player = Player()

screen.listen()
screen.onkey(fun=player.move, key="Up")

scoreboard = Scoreboard()
car = CarManager()

game_is_on = True
iteration_counter = 0  # Generate car every "iteration_car" times the loop is completed.
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in screen.turtles()[2:]:
        car.move()
    game_is_on = not player.detect_collision(screen)
    iteration_counter += 1
    if iteration_counter == 6:
        CarManager()
        iteration_counter = 0

    scoreboard.check_finish(user=player)
    scoreboard.update_scoreboard()

screen.exitonclick()
