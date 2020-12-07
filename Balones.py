import turtle

class Balones():
    ball= turtle.Turtle()

    def crear_balon(self):
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.penup()
        self.ball.goto(0, 0)

        # ball moves 0.15 pixels
        self.ball.dx = 0.15
        self.ball.dy = 0.15

    # Move the ball
    def mover_balon(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)


