from turtle import Turtle


class StateName(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def write_name(self, position, state_name):
        self.goto(position)
        self.write(f"{state_name}")
