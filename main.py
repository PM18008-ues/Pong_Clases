import turtle
import Ventana
import Jugadores
import Balones

# importamos las librerias para reproducir sonido segun
# el sistema operativo
try:
    import winsound
    sistema = "windows"
except:
    import os
    sistema = "linux"

# creamos los objetos
ven = Ventana.Ventana()
players = Jugadores.Jugadores()
pelota = Balones.Balones()

# creamos los componentes del juego
ven.crear_ventana()
ven.crear_marcador()
pelota.crear_balon()
players.crear_jugadorA()
players.crear_jugadorB()


ven.wn.listen()
ven.wn.onkeypress(players.paddle_A_up, "w")
ven.wn.onkeypress(players.paddle_A_down, "s")
ven.wn.onkeypress(players.paddle_B_up, "Up")
ven.wn.onkeypress(players.paddle_B_down, "Down")

# ciclo del juego
while True:
    ven.wn.update()
    pelota.mover_balon()

    # Rebote de la pelota con las paredes
    if pelota.ball.ycor() > 290:
        pelota.ball.sety(290)
        pelota.ball.dy *= -1
        if sistema == "windows":
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        else:
            os.system("aplay bounce.wav&")

    if pelota.ball.ycor() < -290:
        pelota.ball.sety(-290)
        pelota.ball.dy *= -1
        if sistema == "windows":
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        else:
            os.system("aplay bounce.wav&")

    # Marcamos las anotaciones
    if pelota.ball.xcor() > 490:
        pelota.ball.goto(0, 0)
        pelota.ball.dx *= -1
        ven.score_a += 1
        ven.actualizar_marcador()

    if pelota.ball.xcor() < -490:
        pelota.ball.goto(0, 0)
        pelota.ball.dx *= -1
        ven.score_b += 1
        ven.actualizar_marcador()

    # Rebote de la pelota con los paneles
    if (pelota.ball.xcor() > 440 and pelota.ball.xcor() < 450) and (pelota.ball.ycor() < players.paddle_b.ycor() + 50 and pelota.ball.ycor() > players.paddle_b.ycor() - 50):
        pelota.ball.setx(440)
        pelota.ball.dx *= -1
        if sistema == "windows":
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        else:
            os.system("aplay bounce.wav&")

    if (pelota.ball.xcor() < -440 and pelota.ball.xcor() > -450) and (pelota.ball.ycor() < players.paddle_a.ycor() + 50 and pelota.ball.ycor() > players.paddle_a.ycor() - 50):
        pelota.ball.setx(-440)
        pelota.ball.dx *= -1
        if sistema == "windows":
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        else:
            os.system("aplay bounce.wav&")

    # Ganador
    if ven.score_a == 1 or ven.score_b == 1:
        ven.wn.reset()
        pen2 = turtle.Turtle()
        pen2.speed(0)
        pen2.color("white")
        pen2.penup()
        pen2.hideturtle()
        pen2.goto(0, 0)
        if ven.score_a > ven.score_b:
            pen2.write("Player A Wins", align="center", font=("Courier", 24, "normal"))
        else:
            pen2.write("Player B Wins", align="center", font=("Courier", 24, "normal"))

        # salir al dar click a la pantalla
        ven.wn.exitonclick()