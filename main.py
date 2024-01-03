import turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

game_is_on = True
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
update_time = 0.07

screen.listen()
screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")
screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")

while game_is_on:
    screen.update()
    time.sleep(update_time)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    if (ball.distance(paddle_right) < 60 and 335 > ball.xcor() > 330) \
            or (ball.distance(paddle_left) < 50 and -335 < ball.xcor() < -330):
        if update_time == 0:
            pass
        else:
            update_time -= 0.007
        ball.bounce_paddle()
    if ball.xcor() > 400 or ball.xcor() < -400:
        update_time = 0.07
        scoreboard.score(ball.xcor())
        scoreboard.write_score()
        if scoreboard.define_winner() == "left":
            scoreboard.game_over()
            game_is_on = False
        if scoreboard.define_winner() == "right":
            scoreboard.game_over()
            game_is_on = False
        ball.change_heading()

 screen.exitonclick()
