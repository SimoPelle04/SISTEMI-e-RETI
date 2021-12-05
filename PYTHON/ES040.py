import turtle

n = int(input("Inserisci il numeo di lati: "))
poligono = []
poligono.append[0] = turtle.Turtle()
poligono.append[1] = turtle.Turtle()
finestra = turtle.Screen()

lato = 100
for _ in range(1,n+1):
    poligono[0].forward(lato)
    poligono[1].forward(lato)
    poligono[0].left(360/n)
    poligono[1].right(360/n)


finestra.exitonclick()