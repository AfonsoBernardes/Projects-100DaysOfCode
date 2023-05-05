import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. STATES GAME")
screen.setup(width=715, height=500)

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.color("Black")
pen.hideturtle()
pen.penup()

# Load CSV file as DataFrame.
with open("50_states.csv") as file:
    df_states = pd.read_csv(file)

current_score = 0
total_score = len(df_states)
while current_score < total_score:
    answer_state = screen.textinput(title=f'{current_score}/{total_score} States Correct', prompt="Enter a state's "
                                                                                                  "name.").title()

    if answer_state == 'Exit':
        df_states.to_csv('missed_states.csv')
        break
        
    if answer_state in df_states["state"].values:
        # Write state onto the map. Need the process of lifting pen and move to right location.
        state_index = df_states[df_states.state == answer_state].index.values[0]  # Comes as a number ready to use.
        pen.penup()
        pen.goto(x=df_states['x'][state_index], y=df_states['y'][state_index])
        pen.pendown()
        pen.write(arg=answer_state, align='center', font=('Arial', 10, 'normal'))

        # Delete entry from DataFrame.
        df_states = df_states.drop(state_index)

        # Increase current score.
        current_score += 1

screen.exitonclick()
