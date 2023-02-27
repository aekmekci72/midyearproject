import pygame
import os
import time

global surv1
global health, happiness, hunger,money



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


splash_page = pygame.image.load('images_fonts/rooms/captainquarters.png')
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

min=0
hour=11

pmam="AM"
b=False
for line in file:
    if line!="75,35,60,10":
        b=True

if b==True:
    hour=5
    pmam="PM"

count=1
global screenn
screenn="captain"
var=0

def clickedbookshelf():
    global screenn
    screenn="bookshelf"

def clickedbed():
    global screenn
    screenn="bed"

def clickedwheel():
    global screenn
    screenn="wheel"


def clickedrug():
    global screenn
    screenn="rug"

def clickeddrawer():
    global screenn
    screenn="drawer"

def clickeddoor():
    global screenn
    screenn="door"

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN and screenn=="captain":
            position=pygame.mouse.get_pos()
            if position[0]>71 and position[0]<607:
                if position[1]> 68 and position[1]<255:
                    clickedbookshelf()
            if position[0]>82 and position[0]<538:
                if position[1]>600 and position[1]<802:
                    clickedbed()
            if position[0]>1195 and position[0]<1382:
                if position[1]>561 and position[1]<863:
                    clickedwheel()
            if position[0]>548 and position[0]<1032:
                if position[1]>285 and position[1]<557:
                    clickedrug()
            if position[0]>1041 and position[0]<1261:
                if position[1]>98 and position[1]<255:
                    clickeddrawer()
            if position[0]<50 or position[1]<50 or position[1]>800:
                clickeddoor()
            
            
            
            
            
            
            print(position)
        
        
        scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
        screen.blit(scaled_splash,(0,0))
        print(screenn)
    
        
    pygame.display.update()
        
    text_splash=font1.render("", False, 'black')
    screen.blit(text_splash, (60,70))
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
    screen.blit(scaled_splash,(0,0))