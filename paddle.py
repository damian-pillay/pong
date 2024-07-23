from turtle import Turtle

PADDLE_SPEED = 40

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.up = False
        self.down = False
        self.goto(position)
         
    def move_up(self):
        new_y = self.ycor() + PADDLE_SPEED
        self.goto(self.xcor(), new_y)
    
    def move_down(self):
        new_y = self.ycor() - PADDLE_SPEED
        self.goto(self.xcor(), new_y)

    # def move_up(self):
    #     if self.up == True:
    #         new_y = self.ycor() + PADDLE_SPEED
    #         self.goto(self.xcor(), new_y)
    
    # def move_down(self):
    #     if self.down == True:
    #         new_y = self.ycor() - PADDLE_SPEED
    #         self.goto(self.xcor(), new_y)

    