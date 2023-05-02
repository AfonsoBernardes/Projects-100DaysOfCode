import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600, startx=None, starty=20)
screen.tracer(False)
screen.title("ROAD CROSSING")

player = Player()

screen.listen()
screen.onkey(fun=player.move, key="Up")

scoreboard = Scoreboard()
CarManager()

game_is_on = True
iteration_counter = 0  # Generate car every "iteration_car" times the loop is completed.
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in screen.turtles()[2:]:
        car.move()

    scoreboard.check_finish(user=player)
    scoreboard.update_scoreboard()

    if player.detect_collision(screen):
        scoreboard.game_over()
        screen.update()
        game_is_on = False

    iteration_counter += 1
    if iteration_counter == 6:
        CarManager()
        iteration_counter = 0

screen.exitonclick()
