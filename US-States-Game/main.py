from turtle import Screen
import pandas as pd
from state_name import StateName

screen = Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Names Game")
screen.bgpic(picname="blank_states_img.gif")

# image = "blank_states_img.gif"
# tutle.shape(image)

# ..-> Below code will print move click coordinates
# def get_mouse_screen_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_screen_coor)

data = pd.read_csv("50_states.csv")
state = data.state
x_cor = data.x
y_cor = data.y
state_dict = {}
for i in range(len(state)):
    state_dict[state[i].lower()] = (x_cor[i], y_cor[i])

check_list = {}
correct = 0
while correct < 51:
    if correct == 0:
        answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?").lower()
    else:
        answer_state = screen.textinput(title=f"{correct}/50 States Correct", prompt="What's another state name?").lower()
    if answer_state == "exit":
        missed_states = []
        for s in state:
            if s.lower() not in check_list:
                missed_states.append(s)
        output_save = pd.DataFrame(missed_states)
        output_save.to_csv("states_to_learn.csv")
        break
    if answer_state in state_dict and answer_state not in check_list:
        correct += 1
        check_list[answer_state] = 1
        state1 = StateName()
        state1.write_name(state_dict[answer_state], answer_state.title())

# below code will keep the screen  open
# turtle.mainloop()
