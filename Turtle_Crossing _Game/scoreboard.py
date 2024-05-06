from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.level_update()

    def increase_level(self):
        self.level += 1
        self.level_update()

    def level_update(self):
        self.clear()
        self.write(f"Game Level: {self.level}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 16, "normal"))
