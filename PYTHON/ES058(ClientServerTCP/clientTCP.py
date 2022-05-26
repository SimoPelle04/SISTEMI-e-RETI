import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#                                          TCP
s.connect(("127.0.0.1",5000))
while True:
    msg = s.recv(4096)
    print(msg.decode())
    msg = input("messaggio: ")
    s.sendto(msg.encode(),("127.0.0.1",8000) ) #encode() per trasformo

s.close()
