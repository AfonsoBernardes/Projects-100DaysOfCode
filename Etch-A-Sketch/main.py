from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def turn_left():
    turtle.setheading(turtle.heading() + 10)


def turn_right():
    turtle.setheading(turtle.heading() - 10)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.onkeypress(fun=move_forward, key='Up')
screen.onkeypress(fun=move_backward, key='Down')
screen.onkeypress(fun=turn_left, key='Left')
screen.onkeypress(fun=turn_right, key='Right')
screen.onkeypress(fun=clear, key='space')

screen.listen()  # Focus on screen to receive inputs.
screen.exitonclick()  # Exit screen on click only
