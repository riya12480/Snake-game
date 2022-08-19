import turtle
from turtle import Turtle
import random

food_shape = ["circle", "square"]
food_color = ["blue", "red", "yellow", "orange"]
turtle.colormode(255)

class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__()
        self.shape(random.choice(food_shape))
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(food_color))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.shape(random.choice(food_shape))
        self.color(random.choice(food_color))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
