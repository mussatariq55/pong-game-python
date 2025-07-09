from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 0.1
        self.x_move = 10
        self.y_move = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset()

    def move(self):
        self.goto(self.xcor() + self.x_move,self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed *= 0.9

    def reset(self):
        random_y = random.randint(-280, 280)
        self.speed = 0.1
        self.goto(0, random_y)




