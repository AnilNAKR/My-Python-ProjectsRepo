from turtle import Turtle

starting_position = (0, -280)
ending_position = (0, 280)
move_distance = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        self.forward(move_distance)

    # Detect successful crossing
    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(starting_position)


