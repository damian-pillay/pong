from turtle import Turtle
from random import choice

BALL_START = [45, 315, 135, 225]

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        
        self.speed = 0.15
        self.direction = 315
        self.setheading(self.direction)

    def move(self):
        self.forward(self.speed)

        if self.ycor() >= 290 or self.ycor() <= -290:
            self.direction *= -1
            self.direction += 360

            self.setheading(self.direction)

    def reset(self):
        if self.direction == 135 or self.direction == 315:
            self.direction -= 90
        else:
            self.direction += 90
        self.setheading(self.direction)
        self.goto(0, 0)
        self.speed = 0.2

        
        



