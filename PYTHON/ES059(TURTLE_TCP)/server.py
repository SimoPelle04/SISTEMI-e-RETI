import imp
import socket
import turtle

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8000))
pen = turtle.Turtle()

def main():
   
    s.listen()
    print("In attesa di connessione...")
    connection, address = s.accept()
    connection.sendall("F=forword, R= right, L=left ---> (commond,number)".encode())
    while True:
        dati, ind_client = connection.recvfrom(4096) # dimensione del buffer (area di memoria) di ricezione 
        dati = dati.decode()
        ls = dati.split(",")

        if(ls[0] == "F"):
            pen.forward(int(ls[1]))
        elif(ls[0] == "R"):
            pen.right(int(ls[1]))
        elif(ls[0] == "L"):
            pen.left(int(ls[1]))
        else:
            connection.sendall("comando non valido")


if __name__=="__main__":
    main()