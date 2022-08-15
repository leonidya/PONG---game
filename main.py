from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time
# TODO: 1 - create screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


# TODO: 2 - create and move a paddle

r_paddle = Paddle((-350,0))
l_paddle = Paddle((350,0))

screen.listen()
screen.onkey(l_paddle.go_up, key="Up")
screen.onkey(l_paddle.go_down, key="Down")
screen.onkey(r_paddle.go_up, key="w")
screen.onkey(r_paddle.go_down, key="s")


# TODO: create a ball and get a ball moving
ball = Ball()
score= Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
#detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
    if ball.distance(l_paddle) < 50 and ball.xcor() > 320 or ball.distance(r_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()



















screen.exitonclick()