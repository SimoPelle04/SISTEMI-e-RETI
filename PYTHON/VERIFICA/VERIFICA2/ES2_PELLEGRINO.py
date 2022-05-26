
def dec2bin(numero,nbit):
    numeroBin = bin(numero)[2:]
    return "0" * (nbit-len(numeroBin))+numeroBin

class IPAddres():
    def __init__(self,ip):
        self.ipdec = ip
        self.ipbin = self

    def Ipbinario(self):
        listaNum = []
        ipbin = ""
        numeri = self.ipdec.split(".")
        for numero in numeri:
            listaNum.append(dec2bin(int(numero), 8))
        ipbin = (f"{listaNum[0]}.{listaNum[1]}.{listaNum[2]}.{listaNum[3]}")
        print( ipbin)
        return ipbin
    
       
    #def subnet(self):
        #ok = false
        #for k in 32:
            #if "1"*k + "0"*(32-k) == self.Ipbinario():
                #ok=True
                #break
        #return ok
        

    #def validita(self):
        #pezzi,ok = self.ipdec.split("."),True
        #for cella in pezzi:
            #if int(cella) > 255:
                #ok=False
        #return ok 








def main():
    ip = IPAddres("192.168.0.0")

    ip.Ipbinario()
    


if __name__=="__main__":
    main() 