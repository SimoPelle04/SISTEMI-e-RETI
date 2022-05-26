from http import client
from socket import socket
import socket
import sys
from urllib import request
target_host = "info.cern.ch"
target_port = 80
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
msg = ""

s.connect((target_host,target_port))

request ="GET / HTTP/1.1\r\nHost:%s\r\n\r\n"% target_host
s.send(request.encode())

response = s.recv(512)
while len(response)>0:
    msg = msg + response.decode()
    print("\n\n")
    response = s.recv(512)

msg = msg[231:]
file = open("SitoCERN.html","w")
file.write(msg)