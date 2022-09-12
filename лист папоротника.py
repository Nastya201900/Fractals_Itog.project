from turtle import *
# прописываем функцию  рисования частичного папоротника, для переменных размера, угла,

def draw_partial_fern(t, razmer, ug, c1, c2):
    t.left(ug)#движение на лево
    draw_fern(t, razmer * c1)
    t.right(ug)# движение вправо на заданный угол
    t.backward(razmer * c2) # движение назад

# функция, которая рисует папоротник лист
def draw_fern(t, razmer):
    if razmer > 1: # если размер больше 1 пикселя
        t.forward(razmer)
        draw_partial_fern(t, razmer, 5, 0.8, 0.05)
        draw_partial_fern(t, razmer, -40, 0.45, 0.2)
        draw_partial_fern(t, razmer, 35, 0.4, 0.75)

# функция для рисования листа папоротника в цвете
def draw_art():
    window = Screen()
    fr = Turtle()
    fr.color("green") # цвет
    fr.speed(49**3009) # скорость
    fr.hideturtle() # скрытая черепаха
    fr.left(90)
    draw_fern(fr, 60)
    window.exitonclick()


draw_art()
turtle.done()