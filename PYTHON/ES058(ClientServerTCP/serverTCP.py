import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#                                                       TCP
s.bind(("127.0.0.1", 8000))
s.listen()
print("In attesa di connessione...")
connection, address = s.accept()
while True:
    msg = input("messaggio: ")
    connection.sendall(msg.encode())
    dati, ind_client = connection.recvfrom(4096) # dimensione del buffer (area di memoria) di ricezione 
    print(f"{dati.decode()} ricevuto da {ind_client}")
    

s.close