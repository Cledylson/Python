import turtle
import time
import math

# Configuração da janela gráfica
window = turtle.Screen()
window.bgcolor("white")
window.setup(width=600, height=600)
window.title("Relógio Analógico")

# Configuração dos marcadores de hora
hour_markers = turtle.Turtle()
hour_markers.speed(0)
hour_markers.pensize(6)

for i in range(12):
    hour_markers.penup()
    hour_markers.goto(0, 200)
    hour_markers.pendown()
    hour_markers.forward(30)
    hour_markers.penup()
    hour_markers.goto(0, 0)
    hour_markers.right(30)

# Configuração dos ponteiros
hour_hand = turtle.Turtle()
hour_hand.speed(0)
hour_hand.pensize(10)
hour_hand.shapesize(1, 5)
hour_hand.penup()

min_hand = turtle.Turtle()
min_hand.speed(0)
min_hand.pensize(6)
min_hand.shapesize(1, 7)
min_hand.penup()

sec_hand = turtle.Turtle()
sec_hand.speed(0)
sec_hand.pensize(3)
sec_hand.shapesize(1, 9)
sec_hand.penup()

# Função que atualiza o relógio a cada segundo
def update_clock():
    current_time = time.localtime()
    sec_angle = current_time.tm_sec * 6
    min_angle = current_time.tm_min * 6 + current_time.tm_sec / 10
    hour_angle = current_time.tm_hour * 30 + current_time.tm_min / 2

    sec_hand.setheading(90 - sec_angle)
    min_hand.setheading(90 - min_angle)
    hour_hand.setheading(90 - hour_angle)

    window.ontimer(update_clock, 1000)

# Inicialização do relógio
update_clock()

turtle.mainloop()
