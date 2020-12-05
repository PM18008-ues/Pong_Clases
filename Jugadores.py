import turtle

class Jugadores():

    # Barra de jugador
    paddle_a = turtle.Turtle()
    paddle_b = turtle.Turtle()

    def crear_jugadorA(self):
        self.paddle_a.speed(0)
        self.paddle_a.shape("square")
        self.paddle_a.color("white")
        self.paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_a.penup()
        self.paddle_a.goto(-450, 0)

    def paddle_A_up(self):
        y = self.paddle_a.ycor()
        y += 20
        self.paddle_a.sety(y)

    def paddle_A_down(self):
        y = self.paddle_a.ycor()
        y -= 20
        self.paddle_a.sety(y)

    def crear_jugadorB(self):
        self.paddle_b.speed(0)
        self.paddle_b.shape("square")
        self.paddle_b.color("white")
        self.paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_b.penup()
        self.paddle_b.goto(450, 0)

    def paddle_B_up(self):
        y = self.paddle_b.ycor()
        y += 20
        self.paddle_b.sety(y)

    def paddle_B_down(self):
        y = self.paddle_b.ycor()
        y -= 20
        self.paddle_b.sety(y)

