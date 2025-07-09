
# create a moveable pad
# Create another pad
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with the paddle#  Detect when paddle misses
# If ball misses the pong then update the score

# Importing Packages Self + Pre-Built
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

# Making Objects from classes
paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
p1 = ScoreBoard((-100, 220))
p2 = ScoreBoard((100, 220))
ball = Ball()
screen = Screen()

# TODO#1: Create the screen
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


# TODO#2: Moving the paddle
screen.listen()
screen.onkey(key="Up", fun=paddle_1.go_up)
screen.onkey(key="Down", fun=paddle_1.go_down)
screen.onkey(key="w", fun=paddle_2.go_up)
screen.onkey(key="s", fun=paddle_2.go_down)
is_game_on = True


while is_game_on:
    time.sleep(ball.speed)
    screen.update()

    # Detect Collision with the upper & lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with the paddle
    if ball.distance(paddle_1) < 40 or ball.distance(paddle_2) < 40:
        ball.bounce_x()

    # Update Player 1 Score
    if ball.xcor() > 380:
        p1.clear_score()
        p1.increase_score()
        ball.reset()
    elif ball.xcor() < -380:
        p2.clear_score()
        p2.increase_score()
        ball.reset()

    ball.move()

screen.exitonclick()