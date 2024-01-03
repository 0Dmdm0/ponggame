from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def score(self, ball_xcor):
        if ball_xcor > 0:
            self.l_score += 1
        else:
            self.r_score += 1

    def write_score(self):
        self.clear()
        self.goto(-50, 250)
        self.write(self.l_score, align="center", font=("Courier", 30, "normal"))
        self.goto(0, 250)
        self.write(":", align="center", font=("Courier", 30, "normal"))
        self.goto(50, 250)
        self.write(self.r_score, align="center", font=("Courier", 30, "normal"))

    def define_winner(self):
        if self.r_score >= 10:
            return "right"
        if self.l_score >= 10:
            return "left"

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 80, "normal"))
