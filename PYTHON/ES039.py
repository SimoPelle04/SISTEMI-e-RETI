import turtle

n = int(input("Inserisci il numeo di lati: "))
poligono = turtle.Turtle()
finestra = turtle.Screen()

lato = 100
for _ in range(1,n+1):
    poligono.forward(lato)
    poligono.left(360/n)

finestra.exitonclick()