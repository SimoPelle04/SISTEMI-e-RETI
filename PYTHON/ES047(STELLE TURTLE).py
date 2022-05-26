import turtle
import random

Stella=turtle.Turtle()
finestra = turtle.Screen()


def Disegno_stella(x,y,dim):
    Stella.penup()
    Stella.setposition(x,y)#setta la posizione di partenza
    Stella.pendown()

    Stella.speed(50)#velocità

    for _ in range(5): #disegno stella
        Stella.forward(dim)
        Stella.right(144)
        
def main():
    for _ in range(50):
        Disegno_stella(random.randint(-480,480),random.randint(-480,480),random.randint(10,20))
    finestra.exitonclick()

if __name__=="__main__":
    main()