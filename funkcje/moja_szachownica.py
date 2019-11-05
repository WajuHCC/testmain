import turtle

"""
setheading
0   - east
90  - north
180 - west
270 - south

"""
f = int(input("Aby narysowac szachownice, wpisz liczbe żądanych pol (minimum 2): "))
if f <2:
    print("SERIO?! Szachownica z jednym polem?")
    quit()

turtle.speed(0)

#empty box
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

# full_box()
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

# whole_line()
def whole_line_odd(f): #linia nieparzysta, f oznacza liczbę pól szachownicy
    for b in range(f // 2):
        empty_box()
        full_box()

def whole_line_even(f): #linia parzysta
    for b in range(f // 2):
        full_box()
        empty_box()

def back_to_start(f,steps=60): #nawrotka
    if f % 2 > 0 and f >= 4:
        turtle.setheading(180)
        turtle.forward(f//2*2*steps)
        turtle.setheading(270)
        turtle.forward(steps)
    elif f % 2 ==0 and f >=4:
        turtle.setheading(180)
        turtle.forward(f * steps)
        turtle.setheading(270)
        turtle.forward(steps)
    else:
        turtle.setheading(180)
        turtle.forward(2*steps)
        turtle.setheading(270)
        turtle.forward(steps)

def szachownica(f):
    for c in range(f//2):
        whole_line_odd(f)
        back_to_start(f)
        whole_line_even(f)
        back_to_start(f)

szachownica(f)
turtle.done()
