f = open("./mask.txt","w")

ip_address=["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
for x in ip_address:
    f.write(x[-3:]+ "\n")

f.close()