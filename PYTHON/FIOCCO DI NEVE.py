import turtle

snow = turtle.Turtle()
finestra = turtle.Screen()
f = open("./file.txt","w")
angolo = 0
riga = 50
trattini=10
for _ in range(1,26):
    snow.goto(10,10)
    f.write("goto:10,10\n")
    snow.left(angolo)
    f.write(f"left:{angolo}\n")
    snow.forward(riga)
    f.write(f"forward:{riga}\n")
    snow.left(30)
    f.write(f"left:30\n")
    snow.forward(trattini)
    f.write(f"forward:{trattini}\n")
    snow.backward(trattini)
    f.write(f"backward:{trattini}\n")
    snow.right(60)
    f.write(f"right:60\n")
    snow.forward(trattini)
    f.write(f"forward:{trattini}\n")
    snow.backward(trattini)
    f.write(f"backward:{trattini}\n")
    angolo += 15
    f.write("anglolo:angolo+=15\n")

f.close()
finestra.exitonclick()