import turtle
def draw_koh_segment(t, ln): # функция которая буде рисовать сам сегмент снежинки коха шестой интерпритации дойдя до ветки else
    if ln > 6: # проверяется если длина > 6 пикселей
        ln3 = ln // 3
        draw_koh_segment(t, ln3)
        t.left(60)
        draw_koh_segment(t, ln3)
        t.right(120)
        draw_koh_segment(t, ln3)
        t.left(60)
        draw_koh_segment(t, ln3)
    else: # рисование фигуры начнётся только с этого блока
        t.fd(ln) # движение прямо на длину ln
        t.left(60) # поворот на лево на 60 град.
        t.fd(ln)
        t.right(120) # поворот на право на 120 град.
        t.fd(ln)
        t.left(60)
        t.fd(ln)
t = turtle.Turtle() # чтобы не писать по несколько раз turtle присваиваем это значение перменной
t.speed(600) # скорость
ln = 200
t.ht() # черепашка становится невидимой ( необязательная команда)
draw_koh_segment(t, ln)
t.left(120) # чтобы получилась снежинка шестой интерпритации необходимо повернуть на лево на 120 град.
draw_koh_segment(t, ln)
t.left(120)
draw_koh_segment(t, ln)
turtle.done() # окно с нарисованной фигурой не исчезнет после того, как закончится выполнение программы