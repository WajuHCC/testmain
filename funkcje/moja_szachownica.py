import turtle

"""
setheading
0   - east
90  - north
180 - west
270 - south

"""
turtle.speed(0)


def empty_box(steps=60):
    turtle.setheading(270)
    turtle.forward(steps)
    turtle.setheading(0)
    turtle.forward(steps)
    turtle.setheading(90)
    turtle.forward(steps)
    turtle.setheading(180)
    turtle.forward(steps)
    turtle.setheading(0)
    turtle.forward(steps)


# empty_box()

def full_box(steps=60):
    for a in range(30):
        turtle.setheading(270)
        turtle.forward(steps)
        turtle.setheading(0)
        turtle.forward(1)
        turtle.setheading(90)
        turtle.forward(steps)
        turtle.setheading(0)
        turtle.forward(1)


# full_box()
def full_line_odd(f): #linia nieparzysta, f oznacza liczbę pól szachownicy
    for b in range(f // 2):
        if f >= 4:
            empty_box()
            full_box()
        else:
            empty_box()


def full_line_even(f): #linia parzysta
    for b in range(f // 2):
        if f >= 4:
            full_box()
            empty_box()
        else:
            full_box()

def back_to_start(f,steps=60): #nawrotka
    if f % 2 > 0:
        turtle.setheading(180)
        turtle.forward(f//2*2*steps) #to trzeba poprawic zweby nawrotki przy nieparzystych sie zgadzaly
        turtle.setheading(270)
        turtle.forward(steps)
    else:
        turtle.setheading(180)
        turtle.forward(f * steps)  # to trzeba poprawic zweby nawrotki przy nieparzystych sie zgadzaly
        turtle.setheading(270)
        turtle.forward(steps)

def szachownica(f):
    for c in range(f//2):
        full_line_odd(f)
        back_to_start(f)
        full_line_even(f)
        back_to_start(f)

szachownica(4)
turtle.done()
