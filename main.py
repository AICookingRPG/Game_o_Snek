from turtle import Screen
import time
from SnekBrain import Snek
from Food import Food
from ScoreBoard import Scoreboard
from Border import Border

screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("black")
screen.title("Snek Game")
screen.tracer(0)

snek = Snek()
food = Food()
scoreboard = Scoreboard()
border = Border()

screen.listen()
screen.onkey(snek.snek_up, "Up")
screen.onkey(snek.snek_down, "Down")
screen.onkey(snek.snek_left, "Left")
screen.onkey(snek.snek_right, "Right")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snek.move_snek()

    if snek.head.distance(food) < 10:
        scoreboard.change_score()
        if scoreboard.score == 838:
            game_is_on = False
            scoreboard.game_win()
        snek.extend_snek()
        food.refresh()
        for body_part in snek.snek_body_parts:
            while food.distance(body_part) < 10:
                food.refresh()

    if snek.head.xcor() > 295 or snek.head.xcor() < -295 or snek.head.ycor() > 295 or snek.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()

    for body_part in snek.snek_body_parts[1:]:
        if snek.head.distance(body_part) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()


# TODO 1 - Make sure that food can't spawn on snek
# TODO 2 - Make turtle width 18