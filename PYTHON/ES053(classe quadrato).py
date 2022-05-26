from cmath import sqrt
import turtle

class Quadrato():
    def __init__(self,lato,x,y):
        self.x = x
        self.y = y
        self.lato = lato
        """
        x1,y1,x2,y2
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.lato = sqrt((x1-x2)*(y1-y2))
        """
       

    def area(self):
        return self.lato**2

    def perimetro(self):
        return self.lato*4
    
    def puntoEsterno(self,x,y):
        if(x<self.x or  x > (self.x + self.lato) or y < self.y or  y > (self.y + self.lato)):
            punto = "esterno"
        else:
            punto = "interno"

        return punto

    def disegno(self):
        s=turtle.Turtle()
        finestra = turtle.Screen()

        s.penup()
        s.setposition(self.x,self.y)
        s.pendown()
        s.speed(100)
        for _ in range(5):
            s.forward(self.dim)
            s.right(90)

        
    



def main():
    lato = float(input("inserisci la lunghezza del lato"))
    x = int(input("inserisci la x del verticein alto a sinistra"))
    y = int(input("inserisci la y del verticein alto a sinistra"))
    quadrato = Quadrato(lato,x,y)
    print (f"area = {quadrato.area()}")
    print(f"perimeto = {quadrato.perimetro()}")
    
    xPunto = int(input("inserisci la x del punto"))
    yPunto = int(input("inserisci la y del punto"))
    print(f"il punto è {quadrato.puntoEsterno(xPunto,yPunto)}")

    quadrato.disegno()
    


if __name__=="__main__":
    main() 
    
    


if __name__=="__main__":
    main() 