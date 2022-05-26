import sys,pygame,random,math,os,time
def disegnaGriglia(r,c,mappa,adiacenze):#disegno la griglia con pygame
    ok = True
    while(True):
        size = (500,500)
        BLACK,BLU,RED,GREEN = (0, 0, 0),(0, 0, 255),(128,0,0),(0, 255, 0)
        pygame.init()
        screen = pygame.display.set_mode(size)
        screen.fill(BLACK)
        area = (((size[0]-4)**2)/(r*c))-(r-1+c-1)
        lato = math.sqrt(area)
        y = 8
        x = y
        fnt = pygame.font.SysFont("Times New Roman", 12)
        for i in range(c):
            for k in range(r):
                if(mappa[i][k] == -1):
                    #pygame.draw.rect(screen, BLACK, (x, y, lato, lato),1)
                    pygame.draw.rect(screen, RED, (x+1, y+1, lato-2, lato-2))
                    pygame.draw.rect(screen, BLACK, (x, y, lato, lato),1)
                    surf_text = fnt.render("X", True, BLACK)
                    screen.blit(surf_text,(x+4,y+4))
                else: 
                    #pygame.draw.rect(screen, BLACK, (x, y, lato, lato),1)
                    pygame.draw.rect(screen, GREEN, (x+1, y+1, lato-2, lato-2))
                    pygame.draw.rect(screen, BLACK, (x, y, lato, lato),1)
                    surf_text = fnt.render(str(mappa[i][k]), True, BLACK)
                    screen.blit(surf_text,(x+4,y+4))
                x += lato-2
            y += lato-3
            x = 8
        if ok : 
            palla,mappaPalla = disegnaPalla(mappa,adiacenze,lato,screen)
            ok = False
        else: mappaPalla = muoviPalla(mappaPalla,palla,screen,lato,adiacenze,mappa)
        """for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()"""
        pygame.display.flip()
def controlloMovimento(mappaPalla,palla,adiacenze,lato,mappa,n,num,coordinata,segno):
    if adiacenze[n][num] != -1:
        for k,y in enumerate(mappaPalla):
            for i,x in enumerate(y):
                if (x == adiacenze[n][num]):
                    if coordinata : 
                        if segno : palla.centerx -= lato
                        else: palla.centerx += lato
                    else:
                        if segno : palla.centery -= lato
                        else: palla.centery += lato
                    for z,y in enumerate(mappaPalla):
                        for f,x in enumerate(y):
                            if mappaPalla[z][f] == -2:
                                mappaPalla[z][f] = mappa[z][f]
                    mappaPalla[k][i] = -2
                    break
    return mappaPalla
def muoviPalla(mappaPalla,palla,screen,lato,adiacenze,mappa):
    #pygame.draw.circle(screen,(0,0,255),(palla.centerx,palla.centery),palla.height/2)
    for k,y in enumerate(mappaPalla):
        for i,x in enumerate(y):
            if x == -2:
                n = mappa[k][i]
                break
    for event in pygame.event.get():
        #if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: 
            if event._dict_["unicode"] == "a":
                mappaPalla = controlloMovimento(mappaPalla,palla,adiacenze,lato,mappa,n,0,True,True)#mappa della palla, ogetto palla,dizionario delle adiacenze, lunghezza del lato, mappa , posizione palla nella mappa, True = coordinata x, True = meno
            if event._dict_["unicode"] == "w":
                mappaPalla = controlloMovimento(mappaPalla,palla,adiacenze,lato,mappa,n,3,False,True)
            if event._dict_["unicode"] == "s":
                mappaPalla = controlloMovimento(mappaPalla,palla,adiacenze,lato,mappa,n,2,False,False)
            if event._dict_["unicode"] == "d":
                mappaPalla = controlloMovimento(mappaPalla,palla,adiacenze,lato,mappa,n,1,True,False)
    pygame.draw.circle(screen,(0,0,255),(palla.centerx,palla.centery),palla.height/2)
    return mappaPalla
def disegnaPalla(mappa,adiacenze,lato,screen):
    mappaPalla = [i.copy() for i in mappa]
    n = 0
    for k in adiacenze:
        num = 0
        for x in adiacenze[k]:
            if(x == -1):
                num += 1
        if num <= 2:
            n = k
            break
    for k,y in enumerate(mappa):
        for i,x in enumerate(y):
            if(x == n):
                coordinate = ((i*lato)+(lato/2)+8,(k*lato)+(lato/2)+8)
                mappaPalla[k][i] = -2
    palla = pygame.draw.circle(screen,(0,0,255),coordinate,(lato/2)/2)
    return palla,mappaPalla          
def creaDiz(mappa):
    adiacenze ={}
    n = 0
    for i,x in enumerate(mappa): 
        for num,k in enumerate(x):
            if k == 0:
                mappa[i][num] = n
                adiacenze[n] = []
                n += 1
    return adiacenze,mappa
def creaMappa():
    r = random.randint(3,10)
    mappa = [celle(r) for _ in range(r)]
    return mappa,r,r
def celle(c):
    y = [random.choice([0,-1,0]) for _ in range(c)]
    return y
def stampaMappa(mappa):
    for x in mappa:
        str = ""
        for i in x:
            str += " %2d " %i
        print(str)
def adiacenza(mappa,adiacenze):
    for i,x in enumerate(mappa): 
        for num,k in enumerate(x):
            if(k != -1):
                if((mappa[i][num-1] != -1)):
                    if(num-1 >= 0):
                        adiacenze[k].append(mappa[i][num-1])
                    else :
                        adiacenze[k].append(-1)
                else:
                        adiacenze[k].append(-1)
                if(num+1 < len(x)):
                    if(mappa[i][num+1] != -1):
                        adiacenze[k].append(mappa[i][num+1])  
                    else:
                        adiacenze[k].append(-1)
                else:
                        adiacenze[k].append(-1)
                if(i+1 < len(mappa)):
                    if(mappa[i+1][num] != -1):
                        adiacenze[k].append(mappa[i+1][num])
                    else:
                        adiacenze[k].append(-1)
                else:
                        adiacenze[k].append(-1)
                if( (mappa[i-1][num] != -1)):
                    if(i-1 >= 0):
                        adiacenze[k].append(mappa[i-1][num])
                    else:
                        adiacenze[k].append(-1)
                else:
                        adiacenze[k].append(-1)
    return adiacenze
def stampaDict(dic):
    dict = {i:dic[i] for i in dic}
    for x in dict:
        print(f"{x} --> {dict[x]}")

def main():
    while True:
        os.system("cls")
        mappa,r,c = creaMappa()
        #mappa = [[0,0,0,1],[1,0,0,1],[0,0,0,0],[1,1,1,0]]
        adiacenze,mappa = creaDiz(mappa)
        stampaMappa(mappa)
        adiacenze = adiacenza(mappa,adiacenze)
        #print(f"possibili mosse:\n {adiacenze}") 
        stampaDict(adiacenze)
        disegnaGriglia(r,c,mappa,adiacenze) 
if __name__=="__main__":
    main()