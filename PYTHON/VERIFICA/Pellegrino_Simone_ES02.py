import turtle

griglia = turtle.Turtle()
finestra = turtle.Screen()
for x in range(1,5):
    for _ in range(1,5):
        griglia.forward(10)#/4)
        griglia.right(90)
        griglia.forward(10)#/4)
        griglia.backward(10)#/4)
        griglia.left(90)
    griglia.backward(10*4)#/4)
    griglia.right(90)
    griglia.forward(10)#/4)
    griglia.left(90)
griglia.forward(10*4)#/4
finestra.exitonclick()