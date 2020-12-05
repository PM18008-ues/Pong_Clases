import turtle

class Ventana():
    wn = turtle.Screen()
    pen = turtle.Turtle()

    # Puntaje
    score_a = 0
    score_b = 0

    # Crear la ventana de juego
    def crear_ventana(self):
        self.wn.title("Pong by Melvin Portillo")
        self.wn.bgcolor("black")
        self.wn.setup(width=1000, height=600)
        self.wn.tracer(0)

    #  Marcador
    def crear_marcador(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Player A: {} Player B: {}".format(self.score_a, self.score_b), align="center", font=("Courier", 24, "normal"))

    def actualizar_marcador(self):
        self.pen.clear()
        self.pen.write("Player A: {} Player B: {}".format(self.score_a, self.score_b), align="center", font=("Courier", 24, "normal"))



