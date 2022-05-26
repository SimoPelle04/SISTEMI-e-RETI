import turtle

snow = turtle.Turtle()
finestra = turtle.Screen()
f = open("./file.txt","r")
righe =  f.readlines()
for riga in righe:
    comando = riga.split(":")
    if(comando[0] == "goto"):
        go = comando[1].split(",")
        snow.goto(go[0],go[1][:-1])
    elif(comando[0] == "left"):
        snow.left(comando[1][:-1])
    elif(comando[0] == "forward"):
        snow.forward(int(comando[1][:-1]))
    elif(comando[0] == "right"):
        snow.right(int(comando[1][:-1]))
    elif(comando[0] == "backward"):
        snow.backward(int(comando[1][:-1]))
    else:
        print("Fine")
f.close()
finestra.exitonclick()