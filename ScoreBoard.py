from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.write(arg=f"Score: {self.score}", align="center", font=("Century Gothic", 12, "normal"))

    def change_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("Century Gothic", 12, "normal"))

    def game_over(self):
        self.goto(0, 20)
        self.write(arg="GAME OVER", align="center", font=("Century Gothic", 24, "normal"))
        self.goto(0, -20)
        self.write(arg=f"YOUR SCORE: {self.score}", align="center", font=("Century Gothic", 24, "normal"))

    def game_win(self):
        self.goto(0, 20)
        self.write(arg="YOU WIN!", align="center", font=("Century Gothic", 24, "normal"))
        self.goto(0, -20)
        self.write(arg=f"YOUR SCORE: {self.score}", align="center", font=("Century Gothic", 24, "normal"))