import pygame
import os
import time

global surv1

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('Neucha-Regular.ttf',60)
font1 = pygame.font.Font('PermanentMarker-Regular.ttf', 20)

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35)
text = smallfont.render('S T A R T' , True , color)


splash_page = pygame.image.load('commons.png')

scaled_splash = pygame.transform.scale(splash_page, (800, 800))


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
global min, hour, count, var,label
booleee=False
file =open("infofile.txt")
for line in file:
    line=line.strip()
    if line=="event1_1":
        boleee=True

if booleee==True:
    hour=9
    label=font1.render("You survived the choppy waters", False,"black")
else:
    hour=7
    label=font1.render("You wake up at 7 on your ship",False,"black")

count=1
var=0
min=0


def event1():
    global hour
    os.system("python event1_1.py 1")
    hour=10

def clockfunc():
    global min, hour, count, var
    if hour==9:
        os.system("python event1_1.py 1")
    time.sleep(0.1)
    min+=1
    if min<10:
        mindisp="0"+str(min)
    else:
        mindisp=str(min)
    if count%2!=0:
        clock_game = f"{hour}:{mindisp} AM"
    else:
        clock_game = f"{hour}:{mindisp} PM"
    
    if min==60:
        min=0
        hour+=1
        if count%2!=0:
            clock_game = f"{hour}:{mindisp} AM"
        else:
            clock_game = f"{hour}:{mindisp} PM"

    if hour == 12:
        if count%2!=0:
            clock_game = f"{hour}:{mindisp} PM"
        else:
            clock_game = f"{hour}:{mindisp} AM"
        hour = 1
        count+=1
    text_splash=font1.render(clock_game, False, 'black')
    
    
    pygame.draw.rect(screen, "white", pygame.Rect(0, 0, 10000, 40))
    screen.blit(text_splash, (10,10))

    screen.blit(label,(300,10))
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            print(event.key, variable)
            if event.key == pygame.K_LEFT and variable=="commons" or event.key==pygame.K_DOWN and variable=="hallway" or event.key==pygame.K_UP and variable=="rooms":
                variable="stores"
                splash_page = pygame.image.load('stores.png')
            elif event.key == pygame.K_RIGHT and variable=="commons" or event.key==pygame.K_DOWN and variable=="outsideup" or event.key==pygame.K_UP and variable=="outsidedown":       
                variable="captain"
                splash_page = pygame.image.load('captainquarters.png')
            elif event.key == pygame.K_UP and variable=="commons" or event.key==pygame.K_LEFT and variable=="outsideup" or event.key==pygame.K_RIGHT and variable=="hallway":
                variable="arcade"
                splash_page = pygame.image.load('arcade.png')
            elif event.key == pygame.K_DOWN and variable=="commons" or event.key ==pygame.K_LEFT and variable=="outsidedown" or event.key==pygame.K_RIGHT and variable=="rooms":
                variable="medbay"
                splash_page = pygame.image.load('medbay.png')
            elif event.key == pygame.K_LEFT and variable=="arcade" or event.key == pygame.K_UP and variable=="stores":
                variable="hallway"
                splash_page = pygame.image.load('hallway.png')
            elif event.key == pygame.K_DOWN and variable =="captain" or event.key ==pygame.K_RIGHT and variable=="medbay":
                variable="outsidedown"
                splash_page = pygame.image.load('outsidedown.png')
            elif event.key == pygame.K_UP and variable =="captain" or event.key ==pygame.K_RIGHT and variable=="arcade":
                variable="outsideup"
                splash_page = pygame.image.load('outsideup.png')
            elif event.key == pygame.K_DOWN and variable =="stores" or event.key ==pygame.K_LEFT and variable=="medbay":
                variable="rooms"
                splash_page = pygame.image.load('rooms.png')
            elif event.key==pygame.K_DOWN and variable=="arcade" or event.key==pygame.K_RIGHT and variable=="stores" or event.key==pygame.K_UP and variable=="medbay" or event.key==pygame.K_LEFT and variable=="captain":
                variable="commons"
                splash_page = pygame.image.load('commons.png')
            position=pygame.mouse.get_pos()
            scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
            screen.blit(scaled_splash,(0,0))
    clockfunc()
    
        
    pygame.display.update()
        
    text_splash=font1.render("", False, 'black')
    screen.blit(text_splash, (60,70))
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))
         