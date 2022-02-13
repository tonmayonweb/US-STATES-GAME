import turtle
import pandas

FONT = ("Courier", 24, "normal")

screen = turtle.Screen()
timmy = turtle.Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(width=700, height=500)
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
state_name = state_data.state
state_list = state_name.to_list()  # state lists

gameon = True
count = 0
guessed_state = []
while gameon:
    answer_state = turtle.textinput(title=f"{count}/50 Guess the states", prompt="Whats another states name")
    answer_state_title = answer_state.title()
    guessed_state.append(answer_state_title)
    if answer_state_title == "Exit":
        missing_state = []
        for state in state_list:  # add not guessed states to the list to create a csv file
            if state not in guessed_state:
                missing_state.append(state)
        data = pandas.DataFrame(missing_state)
        data.to_csv("states_to_learn.csv")
        break
    if answer_state_title in state_list:
        count += 1
        state_row = state_data[state_data.state == answer_state_title]
        state_row_dict = state_row.to_dict()
        x_position = (state_row_dict["x"][state_list.index(answer_state_title)])
        y_position = (state_row_dict["y"][state_list.index(answer_state_title)])
        timmy.penup()
        timmy.hideturtle()
        timmy.goto(x=x_position, y=y_position)
        timmy.write(f"{answer_state_title}", False, "center", font=('Courier', 7, 'normal'))
    if count == 50:
        timmy.goto(0, 0)
        timmy.write(f"Congratulation, you guessed all of the 50 states", False, "center", font=('Courier', 7, 'normal'))
        break

# turtle.mainloop()
