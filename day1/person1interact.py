import pygame
import os

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/PermanentMarker-Regular.ttf', 30)

width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35, "black")
continueb = pygame.image.load('images_fonts/continue.png')

global scaled_splash, text_splash, text_splash1, counter
splash_page = pygame.image.load('day1/persontalk.png')

scaled_splash = pygame.transform.scale(splash_page, (800, 800))


global money, happy
health=0
happy=0
hunger=0
money=0

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('Hi! Are you the new captain?', False, 'black')
text_splash1 = font1.render('My name is ____, and Im a crewmate! Happy to work for you, boss :)', False, 'black')
counter=1

global eventvar

eventvar="na"

def sync():
    global scaled_splash, text_splash, text_splash1, counter, eventvar, money, happy
    screen.blit(scaled_splash,(0,0))
    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
def masterloop():
    global scaled_splash, text_splash, text_splash1, counter, eventvar, money, happy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if counter==100:
            eventvar="e3_1"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if eventvar=="na":
                if counter==1:
                    text_splash = font1.render("The disease, you ask? Well, it's very sad, very sad indeed", False, "black")
                    text_splash1 = font1.render("My family died too, you know...", False, "black")
                    counter+=1
                    sync()
                if counter==2:
                    text_splash = font1.render("[OTHER STANDIN STUFFFF]", False, "black")
                    text_splash1 = font1.render("[MORE CONVERSATION]", False, "black")
                    eventvar="e1"
                    sync()

        scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
        
        fi=open("main_files/infofile.txt")
        stuff=""
        for line in fi:
            stuff+=line
        stuff=stuff.split(",")
        file=open("main_files/infofile.txt", "w")
        info=str(int(stuff[0])+health)+"," +str(int(stuff[1])+happy) +","+str(int(stuff[2])+hunger)+","+str(int(stuff[3])+money)
        file.write(info)
        file.close()
        file=open("day1/mhm.txt","w")
        file.write("yah")
        file.close()

        pygame.display.update()
        clock.tick(60)

while True:
    masterloop()
    