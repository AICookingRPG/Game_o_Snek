from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snek:

    def __init__(self):
        self.snek_body_parts = []
        self.make_snek()
        self.head = self.snek_body_parts[0]

    def make_snek(self):
        for position in STARTING_POSITIONS:
            self.add_snek_body_part(position)

    def add_snek_body_part(self, position):
        snek_body = Turtle()
        snek_body.penup()
        snek_body.color("white")
        snek_body.shape("square")
        snek_body.goto(position)
        self.snek_body_parts.append(snek_body)

    def move_snek(self):
        for snek_num in range(len(self.snek_body_parts) - 1, 0, -1):
            new_x = self.snek_body_parts[snek_num - 1].xcor()
            new_y = self.snek_body_parts[snek_num - 1].ycor()
            self.snek_body_parts[snek_num].goto(new_x, new_y)
        self.snek_body_parts[0].forward(MOVE_DISTANCE)

    def extend_snek(self):
        self.add_snek_body_part(self.snek_body_parts[-1].position())

    def snek_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def snek_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def snek_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def snek_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
