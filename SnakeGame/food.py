import imp
from mimetypes import init
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_random = random.randint(-200,200)
        y_random = random.randint(-200,200)
        self.goto(x_random,y_random)
