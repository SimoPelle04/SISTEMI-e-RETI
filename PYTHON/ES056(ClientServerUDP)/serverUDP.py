import socket
from threading import Thread


class Mythread(Thread):
    def __init__(self,socket):
        Thread.__init__(self)
        self.s = socket
        self.running = True

    def run(self):
        while self.running:
            dati, ind_client = s.recvfrom(4096) # dimensione del buffer (area di memoria) di ricezione 
            print(f"{dati.decode()} ricevuto da {ind_client}")
            if dati.decode() == "exit":
                self.running = False

       

#                         IPv4              UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1",5000)) #OPERAZIONE FATTA SOLO SU SERVER NON SU CLIENT

ricezione = Mythread(s)
ricezione.start()

msg = input("Inserisci stringa : ")
s.sendto(msg.encode(),({ricezione.ind_client}, 5000) ) #encode() per trasformo
while (msg != "exit"):
    msg = input("Inserisci stringa : ")
    s.sendto(msg.encode(),({ricezione.ind_client}, 5000) ) #encode() per trasformo

ricezione.join()
