import socket

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("127.0.0.1",8000))
    msg = s.recv(4096)
    print(msg.decode())

    while True:
        msg = input("inserisci comando: ")
        msg = msg.upper()
        s.sendall(msg.encode())


if __name__=="__main__":
    main()