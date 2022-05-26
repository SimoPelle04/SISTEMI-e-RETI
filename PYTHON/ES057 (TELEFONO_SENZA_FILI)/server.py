import socket
#                         IPv4              UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("192.168.0.124",5000)) #OPERAZIONE FATTA SOLO SU SERVER NON SU CLIENT

while True:
    msg,id_client = s.recvfrom(4096)
    print(msg.decode())

    