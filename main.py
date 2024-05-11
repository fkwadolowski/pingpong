
from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping pong game")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.listen()

game_is_on =True
while game_is_on:

    time.sleep(0.1)
    ball.move()
    screen.update()
    if ball.ycor()==280 or ball.ycor()==-280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(r_paddle) <50 or ball.xcor() <-320 and ball.distance(l_paddle)<50:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.new_round()
        scoreboard.point_l()
    if ball.xcor() < -380:
        ball.new_round()
        scoreboard.point_r()
screen.exitonclick()