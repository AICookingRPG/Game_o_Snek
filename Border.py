from turtle import Turtle


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(300, 300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(-300, -300)
        self.goto(300, -300)
        self.goto(300, 300)
        self.penup()
