from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.goto(randint(-200, 200), randint(-200, 200))

    def create_food(self):
        self.goto(randint(-200, 200), randint(-200, 200))
