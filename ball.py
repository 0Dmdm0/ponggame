from turtle import Turtle


class Ball(Turtle):

    def __init__(self,):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(50)

    def move(self):
        self.forward(10)

    def bounce_wall(self):
        self.setheading(360 - self.heading())

    def bounce_paddle(self):
        if self.xcor() < 360 or self.xcor() > -360:
            if self.heading() <= 180:
                self.setheading(180 - self.heading())
            else:
                self.setheading(360 - self.heading() + 180)

    def change_heading(self):
        if self.xcor() > 0:
            self.setheading(130)
        else:
            self.setheading(50)
        self.goto(0, 0)
