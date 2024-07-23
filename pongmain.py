from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score import Score

LEFT = (-350, 0)
RIGHT = (350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

player_1 = Paddle(RIGHT)
player_2 = Paddle(LEFT)
ball = Ball()
score = Score()

def reset_players():
    player_1.goto(RIGHT)
    player_2.goto(LEFT)

screen.update()
sleep(2)

screen.listen()
screen.onkey(player_1.move_up, "Up")
screen.onkey(player_1.move_down, "Down")
screen.onkey(player_2.move_up, "w")
screen.onkey(player_2.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    if ball.xcor() >= 330 and (ball.ycor() <= player_1.ycor() + 70 and ball.ycor() >= player_1.ycor() - 70):
        if ball.direction == 135 or ball.direction == 315:
            ball.direction -= 90
        else:
            ball.direction += 90

        ball.setheading(ball.direction)
        ball.speed += 0.02

    elif ball.xcor() <= -330 and (ball.ycor() <= player_2.ycor() + 70 and ball.ycor() >= player_2.ycor() - 70):
        if ball.direction == 135 or ball.direction == 315:
            ball.direction -= 90
        else:
            ball.direction += 90

        ball.setheading(ball.direction)
        ball.speed += 0.02
    
    if ball.xcor() >= 400:
        ball.reset()
        reset_players()
        score.r_point()

    if ball.xcor() <= -400:
        ball.reset()
        reset_players()
        score.l_point()
        
        
        
screen.exitonclick()