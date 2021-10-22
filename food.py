from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()

    def create_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.color("green")
        self.speed("fastest")
        cor_x = random.randint(-280, 280)
        cor_y = random.randint(-280, 280)
        self.goto(cor_x, cor_y)

    def position_change(self):
        cor_x = random.randint(-280, 280)
        cor_y = random.randint(-280, 280)
        self.goto(cor_x, cor_y)
