


def libera(m,x):
    """controllo vuoto o pieno"""
    ok = True
    if(griglia[m] == " "):
        if(griglia[m+7]==" "):
            if(griglia[m+14]==" "):
                if(griglia[m+21]== " "):
                    if(griglia[m+28]== " "):
                        if(griglia[m+35]== " "):
                            griglia[m+35]=x
                        else:
                                griglia[m+28]=x
                    else:
                        griglia[m+21] = x
                else:
                        griglia[m+14]= x
            else:
                griglia[m+7]=x
        else:
            griglia[m]=x
    else:
        ok = False
    return ok

def controlloCella(m):
    """controllo numero inserito utente"""
    if(m >= 0 and m <= 6):
        ok = True
    else:
        ok = False
    return oko

def combinazioni(g):
    comb=[[14,21,28,35],[15,22,29,36],[16,23,30,37],[17,24,31,38],[18,25,32,39],[19,26,33,40],[20,27,34,41],
          [7,14,21,28],[8,15,22,29],[9,16,23,30],[10,17,24,31],[11,18,25,32],[12,19,26,33],[13,20,27,34],
          [0,7,14,21],[1,8,15,22],[2,9,16,23],[3,10,17,24],[4,11,18,25],[5,12,19,26],[6,13,20,27],
          [35,36,37,38],[28,29,30,31],[21,22,23,24],[14,15,16,17],[7,8,9,10],[0,1,2,3],
          [36,37,38,39],[29,30,31,32],[22,23,24,25],[15,16,17,18],[8,9,10,11],[1,2,3,4],
          [37,38,39,40],[30,31,32,33],[23,24,25,26],[16,17,18,19],[9,10,11,12],[2,3,4,5],
          [38,39,40,41],[31,32,33,34],[24,25,26,27],[17,18,19,20],[10,11,12,13],[3,4,5,6],
          [35,29,23,17],[36,30,24,18],[37,31,25,19],[38,32,26,20],
          [41,33,25,17],[40,32,24,16],[39,31,23,15],[38,30,22,14],
          [28,22,16,10],[29,23,17,11],[30,24,18,12],[31,25,19,13],
          [34,26,18,10],[33,25,17,9],[32,24,16,8],[31,23,15,7],
          [21,15,9,3],[22,16,10,4],[23,17,11,5],[24,18,12,6],
          [27,19,11,3],[26,18,10,2],[25,17,9,1],[24,16,8,0]]
    vittoria=False
    k=0
    while(vittoria==False and k < 69):
        f4=comb[k]
        if( g[f4[0]]==g[f4[1]]==g[f4[2]]==g[f4[3]] and  g[f4[0]]!=" "):
            vittoria = True
        k+=1
    return vittoria

def vincitore(conta,G1,G2):
    ok = False
    if (conta == 42):
        print("PAREGGIO")
        ok = True   
    elif(combinazioni(griglia)):
        if(conta%2 == 0):
            print(f"HA VINTO {G2}") 
            ok = True            
        else:
            print(f"HA VINTO {G1}")
            ok = True  
    return ok 


def disegnaGriglia(g, g1, g2):
    for i in range(42):
        if g[i] == " ":
            print("   ",end="")
        elif g[i] == g1:
            print(" X ",end="")
        elif g[i] == g2:
            print(" O ",end="")
        
        if( i==6 or i==13 or i==20 or i==27 or i==34 or i==41):
            print("\n----------------------------")
        elif i==42:
            print("\n")
        else: 
            print("|",end="")

    print(" 0   1   2   3   4   5   6\n")
        
        

griglia = {0: " ", 1: " ",2: " ",3: " ",4: " ",5: " ",6: " ",7: " ",8: " ",9: " ",10: " ",11: " ",12: " ",
13: " ",14: " ",15: " ",16: " ",17: " ",18: " ",19: " ",20: " ",21: " ",22: " ",23: " ",24: " ",25: " ",26: " ",27: " ",
28: " ",29: " ",30: " ",31:" ",32: " ",33:" ",34: " ",35: " ",36: " ",37: " ",38: " ",39: " ",40: " ",41: " "}
def main():
    G1 = input("Nome Giocatore1[X]: ")
    G2 = input("Nome Giocatore2[O]: ")

    disegnaGriglia(griglia,G1,G2)

    conta = 0
    while(True):
        t1 = False
        print(f"{G1}")
        while t1 == False:
            m = int(input("Inserici numero colonna : "))
            if controlloCella(m):
                if libera(m,G1):
                    t1 = True
                    conta = conta + 1
        
        disegnaGriglia(griglia,G1,G2)
            
        if vincitore(conta,G1,G2):
            break
        
        t2 = False
        print(f"{G2}")
        while t2 == False:
            m = int(input("Inserici numero colonna: "))
            if controlloCella(m):
                if libera(m,G2):
                    t2 = True
                    conta=conta +1
                
        disegnaGriglia(griglia,G1,G2)
        
        if vincitore(conta,G1,G2):
            break

if __name__ == "__main__":
    main()