import pygame
import sys
import time
import random
pygame.init()
pygame.display.set_caption("The Impossible Test")
displayScreen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

#set the colours
blue = (0,0,242)
lightblue2 = (110,180,202)
darkblue = (41,26,139)
black = (0,0,0)
yellow = (238,232,67)
green = (52,206,67)
red = (255,0,0)
orange = (255,128,0)
purple = (153,51,255)
blue1 = (0,76,153)
blue2 = (51,255,255)
indigo = (75,0,130)

#load images
buttons = pygame.image.load("buttons.png")
buttonsplay = pygame.image.load("buttonsplay.png")
buttonsanswers = pygame.image.load("buttonsanswers.png")
arrows = pygame.image.load("arrows (1).png")
arrow = pygame.image.load("line.png")
arrow2 = pygame.image.load("line2.png")
provinces = pygame.image.load("provinces.png")
cont = pygame.image.load("cont.png")
oceans = pygame.image.load("oceans.png")
eyes = pygame.image.load("eyes.png")
mousehere = pygame.image.load("mousehere.png")
mousehere2 = pygame.image.load("mousehere2.png")
bomba = pygame.image.load("bomb2.png")
owl = pygame.image.load("owl.png")
eagle = pygame.image.load("eagle.png")
penguin = pygame.image.load("penguin.png")
koala = pygame.image.load("koala.png")
arrowleft = pygame.image.load("left.png")
arrowright = pygame.image.load("right.png")
arrowleft2 = pygame.image.load("left2.png")
arrowright2 = pygame.image.load("right2.png")

#set lists and arrays
yay = ("GOOD JOB!","Nice one!","Clever!","Lucky guess?","yeah!")
nope = ("wrong","try again","nope!","are you sure?","yikes!")
lookfor = (1,2,3)
arrowlist = []
grid = [
    "WOOOOBGBGGGBW",
    "GGGOOGOOOOOBW",
    "WOBOOBOOOGBGW",
    "WOGOOGOOOGOOW",
    "WOBGOGBGOBOGB",
    "WOOGOOOGOGOBW",
    "WOOBGGBGOGOGW",
    "WOOOOOOOOGBGW",
    ]
grid2 = [
    "LLRRL",
    "RLRLL",
    "RRRLR",
    "LRLLR",
    "LLRRR",
    ]

#if the player messes up, the computer randomly choses
#something to say so they know it was wrong
def wrong():
    choice = random.choice(nope)
    for i in range(10,100,1):
        displayScreen.fill((255,255,255))
        fontTitle = pygame.font.Font("BurgerFrogDEMO.ttf",i)
        textTitle = fontTitle.render(choice,True,red)
        textleft = 400-(textTitle.get_width()/2)
        texttop = 300-(textTitle.get_height()/2)
        displayScreen.blit(textTitle,(textleft,texttop))
        pygame.display.flip()
    pygame.time.wait(600)

#if the player passes the level, the computer randomly choses
#something to say so they know they got it wrong
def goodjob():
    choice = random.choice(yay)
    for i in range(10,100,1):
        displayScreen.fill((255,255,255))
        fontTitle = pygame.font.Font("BurgerFrogDEMO.ttf",i)
        textTitle = fontTitle.render(choice,True,green)
        textleft = 400-(textTitle.get_width()/2)
        texttop = 300-(textTitle.get_height()/2)
        displayScreen.blit(textTitle,(textleft,texttop))
        pygame.display.flip()
    pygame.time.wait(800)

#display the level number at the top left of the screen
def levelnumber(num):
    pygame.draw.circle(displayScreen,darkblue,(50,40),25,4)
    fontTitle = pygame.font.Font("NicknameDEMO.ttf",32)
    textTitle = fontTitle.render(str(num),True,darkblue)
    textleft = (50-(textTitle.get_width()/2))
    texttop = (42-(textTitle.get_height()/2))
    displayScreen.blit(textTitle,(textleft,texttop))

#display the number of lives the player has left
def lives(num):
    display = "LIVES: " + str(num)
    fontTitle = pygame.font.Font("NicknameDEMO.ttf",42)
    textTitle = fontTitle.render(display,True,darkblue)
    texttop = (590-textTitle.get_height())
    displayScreen.blit(textTitle,(25,texttop))

#display a bomb with the number of seconds left
def bomb(sec):
    displayScreen.blit(bomba,(748,0))
    fontTitle = pygame.font.Font("NicknameDEMO.ttf",26)
    textTitle = fontTitle.render(str(sec),True,(255,255,255))
    displayScreen.blit(textTitle,(758,20))

#for level 7, change the arrow's colour when the
#player hovers over it
def hoverarrow(ax,ay,colour):
    if colour == 1:
        displayScreen.blit(arrowright2,(100+ax*120,125+ay*80))
        pygame.display.flip()
    elif colour == 2:
        displayScreen.blit(arrowleft2,(100+ax*120,125+ay*80))
        pygame.display.flip()

#display all the arrows as their original colour
#for level 7
def allarrows():
    x = 100
    y = 125
    for row in grid2:
        for col in row:
            if col == "L":
                displayScreen.blit(arrowleft,(x,y))
            elif col == "R":
                displayScreen.blit(arrowright,(x,y))
            x += 120
        y += 80
        x = 100
    pygame.display.flip()

def howmany(colour):
    if colour == "r":
        fontTitle = pygame.font.Font("NicknameDEMO.ttf",50)
        textTitle = fontTitle.render("H                         L",True,red)
        displayScreen.blit(textTitle,(190,100))
        textTitle = fontTitle.render("       Y                      L",True,red)
        displayScreen.blit(textTitle,(170,200))
        pygame.display.flip()
    elif colour == "o":
        fontTitle = pygame.font.Font("NicknameDEMO.ttf",50)
        textTitle = fontTitle.render("   O                       I",True,orange)
        displayScreen.blit(textTitle,(190,100))
        textTitle = fontTitle.render("          O                     E",True,orange)
        displayScreen.blit(textTitle,(170,200))
        pygame.display.flip()
    elif colour == "y":
        fontTitle = pygame.font.Font("NicknameDEMO.ttf",50)
        textTitle = fontTitle.render("      W                    V",True,yellow)
        displayScreen.blit(textTitle,(190,100))
        textTitle = fontTitle.render("             U                    F",True,yellow)
        displayScreen.blit(textTitle,(170,200))
        pygame.display.flip()
    elif colour == "g":
        fontTitle = pygame.font.Font("NicknameDEMO.ttf",50)
        textTitle = fontTitle.render("             M                 E",True,green)
        displayScreen.blit(textTitle,(190,100))
        textTitle = fontTitle.render("                   H                T",True,green)
        displayScreen.blit(textTitle,(170,200))
        pygame.display.flip()
    elif colour == "b":
        fontTitle = pygame.font.Font("NicknameDEMO.ttf",50)
        textTitle = fontTitle.render("                A                 S",True,blue)
        displayScreen.blit(textTitle,(190,100))
        textTitle = fontTitle.render("                      A                ?",True,blue)
        displayScreen.blit(textTitle,(170,200))
        pygame.display.flip()
    elif colour == "i":
        fontTitle = pygame.font.Font("NicknameDEMO.ttf",50)
        textTitle = fontTitle.render("                   N",True,indigo)
        displayScreen.blit(textTitle,(190,100))
        textTitle = fontTitle.render("D                      V                 ",True,indigo)
        displayScreen.blit(textTitle,(170,200))
        pygame.display.flip()
    elif colour == "v":
        fontTitle = pygame.font.Font("NicknameDEMO.ttf",50)
        textTitle = fontTitle.render("                      Y",True,purple)
        displayScreen.blit(textTitle,(190,100))
        textTitle = fontTitle.render("  O                      E",True,purple)
        displayScreen.blit(textTitle,(170,200))
        pygame.display.flip()
def answernumber(num):
    File = open("answerkey.txt","r")
    for i in range(num):
        File.readline()
    title = File.readline()
    first = File.readline()
    second = File.readline()
    third = File.readline()
    displayScreen.fill((255,255,255))
    fontTitle = pygame.font.Font("BurgerFrogDEMO.ttf",72)
    textTitle = fontTitle.render(title,True,lightblue2)
    textleft = (400-(textTitle.get_width()/2))
    displayScreen.blit(textTitle,(textleft,50))
    fontTitle = pygame.font.Font("NicknameDEMO.ttf",22)
    textTitle = fontTitle.render(first,True,darkblue)
    textleft = (400-(textTitle.get_width()/2))
    displayScreen.blit(textTitle,(textleft,250))
    fontTitle = pygame.font.Font("NicknameDEMO.ttf",22)
    textTitle = fontTitle.render(second,True,darkblue)
    textleft = (400-(textTitle.get_width()/2))
    displayScreen.blit(textTitle,(textleft,300))
    fontTitle = pygame.font.Font("NicknameDEMO.ttf",22)
    textTitle = fontTitle.render(third,True,darkblue)
    textleft = (400-(textTitle.get_width()/2))
    displayScreen.blit(textTitle,(textleft,350))
    fontTitle = pygame.font.Font("BurgerFrogDEMO.ttf",24)
    textTitle = fontTitle.render("use your left and right arrow keys to see the other answers",True,black)
    textleft = (400-(textTitle.get_width()/2))
    displayScreen.blit(textTitle,(textleft,450))
    fontTitle = pygame.font.Font("BurgerFrogDEMO.ttf",24)
    textTitle = fontTitle.render("hit escape to go back",True,black)
    textleft = (400-(textTitle.get_width()/2))
    displayScreen.blit(textTitle,(textleft,500))
    pygame.display.flip()
    File.close()

#display the answers for all the levels in
#a walkthrough fashion and then go back to
#the title screen when the player hits esc
def answers():
    num = 0
    answernumber(num)
    back = False
    while not back:
        answernumber(num)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "hello sweetie"
                elif event.key == pygame.K_RIGHT:
                    if num < 28:
                        num = num+4
                elif event.key == pygame.K_LEFT:
                    if num > 0:
                        num = num-4
            elif event.type ==pygame.QUIT:
                return "bye felicia"

#display the title screen depending on
#where the user's mouse is
def titlescreen(button):
    displayScreen.fill((255,255,255))
    fontTitle = pygame.font.Font("BurgerFrogDEMO.ttf",60)
    textTitle = fontTitle.render("THE",True,darkblue)
    textleft = (300-(textTitle.get_width()/2))
    displayScreen.blit(textTitle,(textleft,125))
    fontTitle = pygame.font.Font("BurgerFrogDEMO.ttf",100)
    textTitle = fontTitle.render("IMPOSSIBLE",True,purple)
    textleft = (400-(textTitle.get_width()/2))
    displayScreen.blit(textTitle,(textleft,175))
    fontTitle = pygame.font.Font("BurgerFrogDEMO.ttf",60)
    textTitle = fontTitle.render("TEST",True,darkblue)
    textleft = (500-(textTitle.get_width()/2))
    displayScreen.blit(textTitle,(textleft,260))
    displayScreen.blit(button,(100,325))
    fontTitle = pygame.font.Font("NicknameDEMO.ttf",72)
    textTitle = fontTitle.render("Play",True,purple)
    displayScreen.blit(textTitle,(165,390))
    fontTitle = pygame.font.Font("NicknameDEMO.ttf",42)
    textTitle = fontTitle.render("Answers",True,purple)
    displayScreen.blit(textTitle,(480,400))
    pygame.display.flip()
    
def endscreen(button):
    displayScreen.blit(button,(100,325))
    fontTitle = pygame.font.Font("NicknameDEMO.ttf",40)
    textTitle = fontTitle.render("Play",True,purple)
    displayScreen.blit(textTitle,(200,380))
    fontTitle = pygame.font.Font("NicknameDEMO.ttf",40)
    textTitle = fontTitle.render("again",True,purple)
    displayScreen.blit(textTitle,(185,425))
    fontTitle = pygame.font.Font("NicknameDEMO.ttf",42)
    textTitle = fontTitle.render("Quit",True,purple)
    displayScreen.blit(textTitle,(530,400))
    pygame.display.flip()

def start():
    button = 0
    play = False
    while not play:
        titlescreen(buttons)
        go = True
        while go == True:
            for event in pygame.event.get():
                #check where the mouse is and if it's over one
                #of the buttons, make its border thicker with
                #the titlescreen function
                if event.type == pygame.MOUSEMOTION:
                    (mx,my) = pygame.mouse.get_pos()
                    if 350 < my < 500:
                        if 105 < mx < 360:
                            button = 1
                            titlescreen(buttonsplay)
                        elif 460 < mx < 685:
                            button = 2
                            titlescreen(buttonsanswers)
                        else:
                            button = 0
                            titlescreen(buttons)
                    else:
                        button = 0
                        titlescreen(buttons)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #if the player clicks play, start the game
                    if button == 1:
                        end()
                        go = False
                        play = True
                    #if the player clicks answers, go to the answers function
                    elif button == 2:
                        proceed = answers()
                        if proceed == "hello sweetie":
                            go = False
                        elif proceed == "bye felicia":
                            go = False
                            play = True
                    else:
                        pass
                if event.type ==pygame.QUIT:
                    go = False
                    play = True
def levelone():
    global left
    left = 3
    go = False
    while not go:
        if left == 0:
            start()
            go = True
        displayScreen.fill((255,255,255))
        fontTitle = pygame.font.Font("NicknameDEMO.ttf",36)
        textTitle = fontTitle.render("Click on the panda",True,purple)
        textleft = 400-(textTitle.get_width()/2)
        displayScreen.blit(textTitle,(textleft,50))
        displayScreen.blit(owl,(100,100))
        displayScreen.blit(eagle,(450,100))
        displayScreen.blit(penguin,(100,350))
        displayScreen.blit(koala,(450,350))
        levelnumber(1)
        lives(left)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mx,my) = pygame.mouse.get_pos()
                if 100 < mx < 650 and 100 < my < 550:
                    wrong()
                    left-=1
                    continue
                elif 50<my<(textTitle.get_height()+50):
                    if 400<mx<(400+textTitle.get_width()/2):
                        return left
            elif event.type ==pygame.QUIT:
                go = True
def leveltwo():
    leave = False
    left = levelone()
    while not leave:
        if left not in lookfor:
            leave = True
            continue
        goodjob()
        go = False
        while not go:
            if left == 0:
                go = True
                leave = True
                start()
            displayScreen.fill((255,255,255))
            fontTitle = pygame.font.Font("NicknameDEMO.ttf",36)
            textTitle = fontTitle.render("Hint: seas",True,purple)
            textleft = 400-(textTitle.get_width()/2)
            displayScreen.blit(textTitle,(textleft,50))
            displayScreen.blit(provinces,(80,100))
            displayScreen.blit(cont,(420,145))
            displayScreen.blit(eyes,(90,375))
            displayScreen.blit(oceans,(420,355))
            levelnumber(2)
            lives(left)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mx,my) = pygame.mouse.get_pos()
                    if 90 < mx < 390 and 375 < my < 553:
                        return left
                    elif displayScreen.get_at((mx,my)) != (255,255,255):
                        wrong()
                        left-=1
                        continue
                elif event.type ==pygame.QUIT:
                    left = 5
                    go = True
def levelthree():
    please = "nah"
    leave = False
    left = leveltwo()
    while not leave:
        if left not in lookfor:
            leave = True
            continue
        goodjob()
        go = False
        while not go:
            if left == 0:
                start()
                go = True
                leave = True
                please = "ok"
            displayScreen.fill((255,255,255))
            fontTitle = pygame.font.Font("NicknameDEMO.ttf",32)
            textTitle = fontTitle.render("Click on the arrows pointing to the left",True,purple)
            upsidedown = pygame.transform.rotate(textTitle,180)
            textleft = 400-(textTitle.get_width()/2)
            displayScreen.blit(upsidedown,(textleft,50))
            allarrows()
            levelnumber(3)
            lives(left)
            pygame.display.flip()
            if please == "ok":
                mouse = True
            else:
                mouse = False
            while not mouse:
                arrowblue = arrowleft.get_at((60,40))
                arroworange = arrowright.get_at((60,40))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        (mx,my) = pygame.mouse.get_pos()
                        if displayScreen.get_at((mx,my)) == arroworange:
                            ax = ((mx-100)/120)
                            ay = ((my-125)/80)
                            hoverarrow(ax,ay,1)
                        elif displayScreen.get_at((mx,my)) == arrowblue:
                            ax = ((mx-100)/120)
                            ay = ((my-125)/80)
                            hoverarrow(ax,ay,2)
                        elif displayScreen.get_at((mx,my)) == (255,255,255):
                            allarrows()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if ax == 0:
                            if ay == 0:
                                arrowlist.append(1)
                            elif ay == 3:
                                arrowlist.append(2)
                            elif ay == 4:
                                arrowlist.append(3)
                            else:
                                wrong()
                                left-=1
                                mouse = True
                        elif ax == 1:
                            if ay == 0:
                                arrowlist.append(4)
                            elif ay == 1:
                                arrowlist.append(5)
                            elif ay == 4:
                                arrowlist.append(6)
                            else:
                                wrong()
                                left-=1
                                mouse = True
                        elif ax == 2:
                            if ay == 3:
                                arrowlist.append(7)
                            else:
                                wrong()
                                left-=1
                                mouse = True
                        elif ax == 3:
                            if ay == 1:
                                arrowlist.append(8)
                            elif ay == 2:
                                arrowlist.append(9)
                            elif ay == 3:
                                arrowlist.append(10)
                            else:
                                wrong()
                                left-=1
                                mouse = True
                        elif ax == 4:
                            if ay == 0:
                                arrowlist.append(11)
                            elif ay == 1:
                                arrowlist.append(12)
                            else:
                                wrong()
                                left-=1
                                mouse = True
                        else:
                            wrong()
                            left-=1
                            mouse = True
                    elif event.type ==pygame.QUIT:
                        mouse = True
                        go = True
                        leave = True
                if set([1,2,3,4,5,6,7,8,9,10,11,12]).issubset(arrowlist):
                    for i in range(len(arrowlist)):
                        del arrowlist[0]
                    return left
def levelfour():
    click = 0
    thisone = 1
    bad = False
    leave = False
    while not leave:
        left = levelthree()
        if left not in lookfor:
            leave = True
            continue
        goodjob()
        pygame.mouse.set_visible(0)
        play = False
        while not play:
            if left == 0:
                pygame.mouse.set_visible(100)
                start()
                play = True
                leave = True
                bad = True
            displayScreen.fill((255,255,255))
            fontTitle = pygame.font.Font("NicknameDEMO.ttf",36)
            textTitle = fontTitle.render("RBGYOP",True,purple)
            textleft = 400-(textTitle.get_width()/2)
            displayScreen.blit(textTitle,(textleft,50))
            pygame.draw.circle(displayScreen,red,(300,245),20,0)
            pygame.draw.circle(displayScreen,(155,0,0),(300,245),25,5)
            pygame.draw.circle(displayScreen,blue1,(75,120),20,0)
            pygame.draw.circle(displayScreen,(0,26,103),(75,120),25,5)
            pygame.draw.circle(displayScreen,green,(675,175),20,0)
            pygame.draw.circle(displayScreen,(2,156,17),(675,175),25,5)
            pygame.draw.circle(displayScreen,yellow,(190,420),20,0)
            pygame.draw.circle(displayScreen,(168,162,7),(190,420),25,5)
            pygame.draw.circle(displayScreen,orange,(575,450),20,0)
            pygame.draw.circle(displayScreen,(155,78,0),(575,450),25,5)
            levelnumber(4)
            lives(left)
            pygame.display.flip()
            if bad == True:
                go = True
            else:
                go = False
            while not go:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        (mx,my) = pygame.mouse.get_pos()
                        if displayScreen.get_at((mx,my)) == (255,255,255):
                            click = 10
                        elif displayScreen.get_at((mx,my)) == green:
                            pygame.draw.circle(displayScreen,(102,255,117),(675,175),25,5)
                            pygame.display.flip()
                            click = 3
                        elif displayScreen.get_at((mx,my)) == red:
                            pygame.draw.circle(displayScreen,(255,153,153),(300,245),25,5)
                            pygame.display.flip()
                            click = 1
                        elif displayScreen.get_at((mx,my)) == blue1:
                            pygame.draw.circle(displayScreen,(120,146,223),(75,120),25,5)
                            pygame.display.flip()
                            click = 2
                        elif displayScreen.get_at((mx,my)) == yellow:
                            pygame.draw.circle(displayScreen,(248,242,97),(190,420),25,5)
                            pygame.display.flip()
                            click= 4
                        elif displayScreen.get_at((mx,my)) == orange:
                            pygame.draw.circle(displayScreen,(255,178,100),(575,450),25,5)
                            pygame.display.flip()
                            click = 5
                        elif displayScreen.get_at((mx,my)) == purple:
                            fontTitle = pygame.font.Font("NicknameDEMO.ttf",36)
                            textTitle = fontTitle.render("RBGYOP",True,(203,120,255))
                            textleft = 400-(textTitle.get_width()/2)
                            displayScreen.blit(textTitle,(textleft,50))
                            pygame.display.flip()
                            click = 6
                        else:
                            pygame.draw.circle(displayScreen,(155,0,0),(300,245),25,5)
                            pygame.draw.circle(displayScreen,(0,26,103),(75,120),25,5)
                            pygame.draw.circle(displayScreen,(2,156,17),(675,175),25,5)
                            pygame.draw.circle(displayScreen,(168,162,7),(190,420),25,5)
                            pygame.draw.circle(displayScreen,(155,78,0),(575,450),25,5)
                            fontTitle = pygame.font.Font("NicknameDEMO.ttf",36)
                            textTitle = fontTitle.render("RBGYOP",True,purple)
                            textleft = 400-(textTitle.get_width()/2)
                            displayScreen.blit(textTitle,(textleft,50))
                            pygame.display.flip()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if click == 10:
                            wrong()
                            left-=1
                            thisone = 1
                            go = True
                        elif click == thisone:
                            thisone+=1
                        else:
                            wrong()
                            left-=1
                            thisone = 1
                            go = True
                    elif event.type ==pygame.QUIT:
                        go = True
                        play = True
                        leave = True
                if thisone == 7:
                    return left
def levelfive():
    leave = False
    while not leave:
        left = levelfour()
        if left not in lookfor:
            leave = True
            continue
        goodjob()
        pygame.mouse.set_visible(100)
        go = False
        while not go:
            if left == 0:
                start()
                go = True
                leave = True
            bx = 400
            by = 300
            num = (2,-2)
            dbx = random.choice(num)
            dby = random.choice(num)
            y = 270
            yy = 270
            dy = 0
            dyy = 0
            hits = 8
            play = False
            while not play:
                hit = False
                while not hit:
                    displayScreen.fill((255,255,255))
                    fontTitle = pygame.font.Font("NicknameDEMO.ttf",50)
                    textTitle = fontTitle.render(str(hits),True,purple)
                    textleft = 400-(textTitle.get_width()/2)
                    displayScreen.blit(textTitle,(textleft,15))
                    pygame.draw.line(displayScreen,(0,102,102),(0,75),(800,75),5)
                    pygame.draw.line(displayScreen,(0,102,102),(0,525),(800,525),5)
                    pygame.draw.rect(displayScreen,(204,255,255),(0,77,800,446),0)
                    levelnumber(5)
                    lives(left)
                    clock.tick(140)
                    bx=bx+dbx
                    by=by+dby
                    if (bx<=27.5):
                        if (by>=y-5):
                            if (by<=(y+95)):
                                dbx = 2
                                hit = True
                                hits -= 1
                            else:
                                wrong()
                                left-=1
                                hit = True
                                play = True
                        else:
                            wrong()
                            left-=1
                            hit = True
                            play = True
                    elif (bx>=772.5):
                        if (by>=yy-5):
                            if (by<=(yy+95)):
                                dbx = -2
                                hit = True
                                hits-=1
                            else:
                                wrong()
                                left-=1
                                hit = True
                                play = True
                        else:
                            wrong()
                            left-=1
                            hit = True
                            play = True
                    if (by>=517.5):
                        dby = -2
                    elif (by<=82.5):
                        dby = 2
                    
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                dyy = -2
                            elif event.key == pygame.K_DOWN:
                                dyy = 2
                            elif event.key == pygame.K_w:
                                dy = -2
                            elif event.key == pygame.K_s:
                                dy = 2

                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                dyy = 0
                            elif event.key == pygame.K_s or event.key == pygame.K_w:
                                dy = 0
                        elif event.type ==pygame.QUIT:
                            hit = True
                            play = True
                            go = True
                            leave = True
                            continue
                    oldy = y
                    oldyy = yy
                    yy = yy + dyy
                    y = y + dy
                    if yy<=75:
                        yy=oldyy
                    if yy>=(435):
                        yy=oldyy
                    if y<=75:
                        y=oldy
                    if y>=(435):
                        y=oldy

                    pygame.draw.circle(displayScreen,red,(bx,by),15,0)
                    pygame.draw.rect(displayScreen, (0,102,102),(0,y,20,90),0)
                    pygame.draw.rect(displayScreen, (0,102,102),(780,yy,20,90),0)
                    pygame.display.flip()
                    if hits == 0:
                        return left
def levelsix():
    please = "nah"
    leave = False
    while not leave:
        left = levelfive()
        if left not in lookfor:
            leave = True
            continue
        goodjob()
        ok = False
        while not ok:
            go = False
            while not go:
                if left == 0:
                    start()
                    go = True
                    ok = True
                    leave = True
                    please = "ok"
                displayScreen.fill((255,255,255))
                fontTitle = pygame.font.Font("NicknameDEMO.ttf",36)
                textTitle = fontTitle.render("Don't touch the orange!",True,purple)
                textleft = 400-(textTitle.get_width()/2)
                displayScreen.blit(textTitle,(textleft,50))
                fontTitle = pygame.font.Font("writing.ttf",28)
                textTitle = fontTitle.render("Put your mouse here",True,(53,206,67))
                displayScreen.blit(textTitle,(550,220))
                displayScreen.blit(mousehere,(684,250))
                displayScreen.blit(arrow,(670,255))
                pygame.draw.circle(displayScreen,green,(755,355),20,0)
                pygame.draw.circle(displayScreen,(12,166,27),(755,355),25,5)
                levelnumber(6)
                lives(left)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        (mx,my) = pygame.mouse.get_pos()
                        if displayScreen.get_at((mx,my)) == green:
                            go = True
                    elif event.type ==pygame.QUIT:
                        please = "ok"
                        go = True
                        ok = True
                        leave = True
            begin = int(round(pygame.time.get_ticks()/1000))
            if please == "ok":
                go = True
            else:
                go = False
            while not go:
                if left == 0:
                    start()
                since = int(round(pygame.time.get_ticks()/1000))
                displayScreen.fill(orange)
                fontTitle = pygame.font.Font("NicknameDEMO.ttf",36)
                textTitle = fontTitle.render("Don't touch the orange!",True,purple)
                textleft = 400-(textTitle.get_width()/2)
                displayScreen.blit(textTitle,(textleft,50))
                pygame.draw.circle(displayScreen,red,(755,355),20,0)
                pygame.draw.circle(displayScreen,(12,166,27),(755,355),25,5)
                pygame.draw.circle(displayScreen,red,(40,185),20,0)
                pygame.draw.circle(displayScreen,(175,0,0),(40,185),25,5)
                pygame.draw.rect(displayScreen,(123,153,56),(120,100,550,440),0)
                pygame.draw.rect(displayScreen,(123,153,56),(65,155,55,55),0)
                pygame.draw.rect(displayScreen,(123,153,56),(650,330,55,55),0)
                (x,y) = (65,100)
                for row in grid:
                    for col in row:
                        if col == "W":
                            pygame.draw.rect(displayScreen,orange,(x,y,55,55),0)
                        elif col == "O":
                            pygame.draw.rect(displayScreen,orange,(x,y,55,55),0)
                        elif col == "B":
                            pygame.draw.rect(displayScreen,blue1,(x,y,55,55),0)
                        elif col == "G":
                            pygame.draw.rect(displayScreen,blue1,(x,y,55,55),0)
                        x+=55
                    y+=55
                    x = 65
                displayScreen.blit(arrow2,(50,220))
                fontTitle = pygame.font.Font("writing.ttf",28)
                textTitle = fontTitle.render("Now get",True,red)
                displayScreen.blit(textTitle,(10,255))
                fontTitle = pygame.font.Font("writing.ttf",28)
                textTitle = fontTitle.render("here",True,red)
                displayScreen.blit(textTitle,(25,280))
                levelnumber(6)
                lives(left)
                sec = 10-(since-begin)
                bomb(sec)
                pygame.display.flip()
                if sec == 0:
                    wrong()
                    left=0
                    go = True
                    leave = True
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        (mx,my) = pygame.mouse.get_pos()
                        if mx > 65:
                            if displayScreen.get_at((mx,my)) == orange:
                                wrong()
                                left-=1
                                go = True
                        else:
                            return left

def levelseven():
    leave = False
    left = levelsix()
    while not leave:
        if left not in lookfor:
            leave = True
            continue
        goodjob()
        go = False
        while not go:
            if left == 0:
                start()
                go = True
                leave = True
            displayScreen.fill((255,255,255))
            levelnumber(7)
            fontTitle = pygame.font.Font("NicknameDEMO.ttf",36)
            textTitle = fontTitle.render("Which arrow is pointing straight down?",True,purple)
            textleft = 400-(textTitle.get_width()/2)
            displayScreen.blit(textTitle,(textleft,75))
            displayScreen.blit(arrows,(80,105))
            lives(int(left))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mx,my) = pygame.mouse.get_pos()
                    #if the player clicks anything that's not white, take away a life
                    if displayScreen.get_at((mx,my)) != (255,255,255):
                        wrong()
                        left-=1
                        continue
                elif event.type ==pygame.QUIT:
                    go = True
                    leave = True
                #if the player hits the down key, continue
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        return left
def leveleight():
    leave = False
    left = levelseven()
    while not leave:
        if left not in lookfor:
            leave = True
            continue
        goodjob()
        go = False
        while not go:
            if left == 0:
                start()
                go = True
                leave = True
            displayScreen.fill((255,255,255))
            pygame.draw.rect(displayScreen,black,(328+35,350+70,76,70),5)
            pygame.draw.rect(displayScreen,red,(331+35,353+70,10,65),0)
            pygame.draw.rect(displayScreen,orange,(341+35,353+70,10,65),0)
            pygame.draw.rect(displayScreen,yellow,(351+35,353+70,10,65),0)
            pygame.draw.rect(displayScreen,green,(361+35,353+70,10,65),0)
            pygame.draw.rect(displayScreen,blue,(371+35,353+70,10,65),0)
            pygame.draw.rect(displayScreen,indigo,(381+35,353+70,10,65),0)
            pygame.draw.rect(displayScreen,purple,(391+35,353+70,10,65),0)
            levelnumber(8)
            lives(left)
            pygame.display.flip()
            colours = False
            while not colours:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        (mx,my) = pygame.mouse.get_pos()
                        if displayScreen.get_at((mx,my)) == red:
                            pygame.draw.rect(displayScreen,(255,255,255),(160,95,600,150),0)
                            howmany("r")
                        elif displayScreen.get_at((mx,my)) == orange:
                            pygame.draw.rect(displayScreen,(255,255,255),(160,95,600,150),0)
                            howmany("o")
                        elif displayScreen.get_at((mx,my)) == yellow:
                            pygame.draw.rect(displayScreen,(255,255,255),(160,95,600,150),0)
                            howmany("y")
                        elif displayScreen.get_at((mx,my)) == green:
                            pygame.draw.rect(displayScreen,(255,255,255),(160,95,600,150),0)
                            howmany("g")
                        elif displayScreen.get_at((mx,my)) == blue:
                            pygame.draw.rect(displayScreen,(255,255,255),(160,95,600,150),0)
                            howmany("b")
                        elif displayScreen.get_at((mx,my)) == indigo:
                            pygame.draw.rect(displayScreen,(255,255,255),(160,95,600,150),0)
                            howmany("i")
                        elif displayScreen.get_at((mx,my)) == purple:
                            pygame.draw.rect(displayScreen,(255,255,255),(160,95,600,150),0)
                            howmany("v")
                        elif displayScreen.get_at((mx,my)) == (255,255,255):
                            pygame.draw.rect(displayScreen,(255,255,255),(160,95,600,150),0)
                            pygame.display.flip()
                    if event.type == pygame.KEYDOWN:
                        if left == 3:
                            if event.key == pygame.K_3:
                                return left
                            else:
                                wrong()
                                left-=1
                                colours = True
                        elif left == 2:
                            if event.key == pygame.K_2:
                                return left
                            else:
                                wrong()
                                left-=1
                                colours = True
                        elif left == 1:
                            if event.key == pygame.K_1:
                                return left
                            else:
                                wrong()
                                left-=1
                                colours = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        wrong()
                        left-=1
                        colours = True
                    elif event.type ==pygame.QUIT:
                        print "leave"
                        colours = True
                        go = True
                        leave = True
def end():
    leave = False
    left = leveleight()
    while not leave:
        if left not in lookfor:
            leave = True
            continue
        for i in range(1,18,1):
            clock.tick(50)
            displayScreen.fill((255,255,255))
            fontTitle = pygame.font.Font("BurgerFrogDEMO.ttf",i*4)
            textTitle = fontTitle.render("CONGRATULATIONS!",True,purple)
            textleft = 400-(textTitle.get_width()/2)
            texttop = 140-(textTitle.get_height()/2)
            displayScreen.blit(textTitle,(textleft,texttop))
            fontTitle = pygame.font.Font("BurgerFrogDEMO.ttf",i*3)
            textTitle = fontTitle.render("YOU'VE PASSED THE IMPOSSIBLE TEST!",True,orange)
            textleft = 400-(textTitle.get_width()/2)
            texttop = 250-(textTitle.get_height()/2)
            displayScreen.blit(textTitle,(textleft,texttop))
            pygame.display.flip()
        pygame.time.wait(400)
        endscreen(buttons)
        go = False
        while not go:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    (mx,my) = pygame.mouse.get_pos()
                    if 350 < my < 500:
                        if 105 < mx < 360:
                            button = 1
                            endscreen(buttonsplay)
                        elif 460 < mx < 685:
                            button = 2
                            endscreen(buttonsanswers)
                        else:
                            button = 0
                            endscreen(buttons)
                    else:
                        button = 0
                        endscreen(buttons)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button == 1:
                        start()
                        go = True
                        leave = True
                    elif button == 2:
                        go = True
                        leave = True
                    else:
                        pass
start()
pygame.quit()
sys.exit()
