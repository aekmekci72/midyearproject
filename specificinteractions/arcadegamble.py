import pygame
import os
import time

global surv1
global health, happiness, hunger,money
global variable


pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/PermanentMarker-Regular.ttf', 20)

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35)
text = smallfont.render('S T A R T' , True , color)


splash_page = pygame.image.load('images_fonts/rooms/commons.png')
scaled_splash = pygame.transform.scale(splash_page, (800, 800))

player1=pygame.image.load('images_fonts/person1.png')
player2=pygame.image.load('images_fonts/person2.png')
player3=pygame.image.load('images_fonts/person3.png')



def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

variable="commons"
health = 100
wealth = 100

clock_game = 0
global min, hour, count, var, pmam
booleee=False
file =open("main_files/infofile.txt")

list=[]
for line in file:
    line=line.strip()
    list=line.split(",")

health=list[0]
happiness=list[1]
hunger=list[2]
money=list[3]
hour=11
min=0
pmam="AM"
thing=False
count=1

file=open("day1/mhm.txt")
for line in file:
    if line=="yah":
        hour=5
        pmam="PM"
        count=2
        thing=True
    elif "character spoke" in line:
        line=line.split()
        hour=int(line[-2]+1)
        pmam=line[-1]
    else:
        hour=11
        pmam="AM"
        

b=False
for line in file:
    if line!="75,35,60,10":
        b=True

if b==True:
    hour=5
    pmam="PM"

var=0


def clockfunc():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    global min, hour, count, var,pmam
    if hour==3:
        os.system("python day1/day1_part2.py 1")

    if hour==11 and pmam=="PM":
        print("detected")
        os.system("python day2/day2.py 1")
        pygame.quit()


    time.sleep(0.03)
    min+=1
    if min<10:
        mindisp="0"+str(min)
    else:
        mindisp=str(min)
    clock_game = f"{hour}:{mindisp} "+pmam
    
    if min==60:
        min=0
        hour+=1
        if count%2!=0:
            pmam="AM"
        else:
            pmam="PM"
        clock_game = f"{hour}:{mindisp} "+pmam
        
    if hour == 12:
        if count%2!=0:
            pmam="PM"
        else:
            pmam="AM"
        clock_game = f"{hour}:{mindisp} "+pmam
        hour = 1
        count+=1
    if thing==True:
        count=2
    clock_game = f"{hour}:{mindisp} "+pmam
    text_splash=font1.render(clock_game, False, 'black')
    
    
    pygame.draw.rect(screen, "white", pygame.Rect(0, 0, 10000, 40))
    screen.blit(text_splash, (10,10))

    pygame.draw.rect(screen, "white", pygame.Rect(width-250, height-250, 250, 250))
    hungerdisp=font1.render("hunger: "+str(hunger)+"/100",False,"black")
    screen.blit(hungerdisp,(width-200,height-200))
    healthdisp=font1.render("health: "+str(health)+"/100",False,"black")
    screen.blit(healthdisp,(width-200,height-150))
    happydisp=font1.render("happiness: "+str(happiness)+"/100",False,"black")
    screen.blit(happydisp,(width-200,height-100))
    moneydisp=font1.render("money: $"+str(money),False,"black")
    screen.blit(moneydisp,(width-200,height-50))
    

while True:
    
    if variable=="commons":
        screen.blit(player1,(500,150))
    if variable=="hallway":
        screen.blit(player2,(1000,100))
    if variable=="medbay":
        screen.blit(player3,(300,240))
    
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:

            if event.key==pygame.K_q and variable=="commons":
                file=open("day1/charspeak.txt","w")
                file.write(str(hour)+ " "+pmam)
                file.close()
                os.system("python day1/person1interact.py 1")
                pygame.quit()
            if event.key==pygame.K_w and variable=="hallway":
                print("person2 interact")
            if event.key==pygame.K_e and variable=="medbay":
                print("person3 interact")

            if event.key == pygame.K_LEFT and variable=="commons" or event.key==pygame.K_DOWN and variable=="hallway" or event.key==pygame.K_UP and variable=="rooms":
                variable="stores"
                splash_page = pygame.image.load('images_fonts/rooms/stores.png')
            elif event.key == pygame.K_RIGHT and variable=="commons" or event.key==pygame.K_DOWN and variable=="outsideup" or event.key==pygame.K_UP and variable=="outsidedown":       
                variable="captain"
                splash_page = pygame.image.load('images_fonts/rooms/captainquarters.png')
            elif event.key == pygame.K_UP and variable=="commons" or event.key==pygame.K_LEFT and variable=="outsideup" or event.key==pygame.K_RIGHT and variable=="hallway":
                variable="arcade"
                splash_page = pygame.image.load('images_fonts/rooms/arcade.png')
            elif event.key == pygame.K_DOWN and variable=="commons" or event.key ==pygame.K_LEFT and variable=="outsidedown" or event.key==pygame.K_RIGHT and variable=="rooms":
                variable="medbay"
                splash_page = pygame.image.load('images_fonts/rooms/medbay.png')
            elif event.key == pygame.K_LEFT and variable=="arcade" or event.key == pygame.K_UP and variable=="stores":
                variable="hallway"
                splash_page = pygame.image.load('images_fonts/hallway.png')
            elif event.key == pygame.K_DOWN and variable =="captain" or event.key ==pygame.K_RIGHT and variable=="medbay":
                variable="outsidedown"
                splash_page = pygame.image.load('images_fonts/outsidedown.png')
            elif event.key == pygame.K_UP and variable =="captain" or event.key ==pygame.K_RIGHT and variable=="arcade":
                variable="outsideup"
                splash_page = pygame.image.load('images_fonts/outsideup.png')
            elif event.key == pygame.K_DOWN and variable =="stores" or event.key ==pygame.K_LEFT and variable=="medbay":
                variable="rooms"
                splash_page = pygame.image.load('images_fonts/rooms/rooms.png')
            elif event.key==pygame.K_DOWN and variable=="arcade" or event.key==pygame.K_RIGHT and variable=="stores" or event.key==pygame.K_UP and variable=="medbay" or event.key==pygame.K_LEFT and variable=="captain":
                variable="commons"
                splash_page = pygame.image.load('images_fonts/rooms/commons.png')
            position=pygame.mouse.get_pos()
            scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
            screen.blit(scaled_splash,(0,0))
    clockfunc()
    
        
    pygame.display.update()
        
    text_splash=font1.render("", False, 'black')
    screen.blit(text_splash, (60,70))
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
    screen.blit(scaled_splash,(0,0))