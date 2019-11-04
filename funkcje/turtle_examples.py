import turtle

print(help(turtle))
def wielokat(bok):
    for i in range(bok):
        turtle.right(360/bok) #to jest o ile ma skrecic
        turtle.forward(50) #idzie do przodu o iles krokow

wielokat(200)
turtle.done()