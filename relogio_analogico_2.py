import turtle
import datetime
import math

# Cria a tela
tela = turtle.Screen()
tela.bgcolor("white")
tela.setup(width=500, height=500)

# Cria o desenho do relógio
desenho = turtle.Turtle()
desenho.speed(0)
desenho.pensize(3)

# Desenha o círculo externo
desenho.penup()
desenho.goto(0, -200)
desenho.pendown()
desenho.circle(200)

# Desenha os números
desenho.penup()
desenho.goto(0, 0)
for i in range(12):
    angulo = i * 30
    x = math.sin(math.radians(angulo)) * 160
    y = math.cos(math.radians(angulo)) * 160
    desenho.goto(x, y)
    desenho.write(i+1, align="center", font=("Arial", 12, "normal"))

# Desenha os ponteiros
agora = datetime.datetime.now()
hora = agora.hour
minuto = agora.minute
segundo = agora.second

# Desenha o ponteiro das horas
desenho.penup()
desenho.goto(0, 0)
desenho.setheading(90)
desenho.rt(hora * 30 + minuto / 2)
desenho.pendown()
desenho.fd(80)

# Desenha o ponteiro dos minutos
desenho.penup()
desenho.goto(0, 0)
desenho.setheading(90)
desenho.rt(minuto * 6)
desenho.pendown()
desenho.fd(120)

# Desenha o ponteiro dos segundos
desenho.penup()
desenho.goto(0, 0)
desenho.setheading(90)
desenho.rt(segundo * 6)
desenho.pendown()
desenho.fd(150)

# Mantém a janela aberta
turtle.done()
