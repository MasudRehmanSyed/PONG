import turtle
from turtle import Turtle

UP = 90
DOWN = 270
HEIGHT = 580 / 2


class Paddle():

    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape('square')
        self.turtle.color('white')
        self.turtle.shapesize(5,1)
        # self.create_paddle()

    # def create_paddle(self):
    #     new_paddle = Turtle('square')
    #     new_paddle.color('white')
    #     new_paddle.pu()
    #     new_paddle.width(20)
    #     new_paddle.shapesize(5, 1)
    #     self.turtle = new_paddle

    def display_paddle(self, position):
        self.turtle.pu()
        self.turtle.goto(position)

    def up(self):
        y = self.turtle.ycor()
        if y < HEIGHT:
            y += 20
            self.turtle.sety(y)

    def down(self):
        y = self.turtle.ycor()
        if y > -HEIGHT:
            y -= 20
            self.turtle.sety(y)
