from turtle import Turtle, Screen
from paddle import Paddle
import time

WIDTH = 800
HEIGHT = 600
position_1 = (380, 0)
position_2 = (-380, 0)
delay = 0.1

screen = Screen()
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg='black')
screen.tracer(0)


def clean():
    screen.update()
    time.sleep(delay)


# TODO: Create 2 paddles and place them on screen


paddle_1 = Paddle()
# paddle_1.create_paddle()
paddle_1.display_paddle(position_1)

paddle_2 = Paddle()
# paddle_2.create_paddle()
paddle_2.display_paddle(position_2)

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")

screen.onkey(paddle_2.up, "a")
screen.onkey(paddle_2.down, "z")


game_on = True

while game_on:
    clean()
    screen.onkey(paddle_1.up, "Up")
    screen.onkey(paddle_1.down, "Down")

    screen.onkey(paddle_2.up, "a")
    screen.onkey(paddle_2.down, "z")

screen.exitonclick()
