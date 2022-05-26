import sys, pygame

width, height = 640, 480
size=(width, height)
speed = [1, 1]
black = (0, 0, 0)

tasto = " "
screen = pygame.display.set_mode(size)

ball = pygame.image.load("./fucile.gif")
ballrect = ball.get_rect()
s = 5
while True:
    #tasto=" "
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            tasto = event.__dict__["unicode"]
            print(tasto)
            if(tasto == "w"):
                if ballrect.top < 0 :
                    speed[0],speed[1] = 0,-s
                    ballrect = ballrect.move(speed)
            elif(tasto == "s"):
                if ballrect.bottom > height:
                    speed[0],speed[1] = 0,s
                    ballrect = ballrect.move(speed)
            elif(tasto == "a"):
                if ballrect.left > 0: 
                    speed[0],speed[1] = -s,0
                    ballrect = ballrect.move(speed)
            elif(tasto == "d"):
                if ballrect.right > width:
                    speed[0],speed[1] = s,0
                    ballrect = ballrect.move(speed)
            else:
                speed[0],speed[1] = 0,0
    
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()