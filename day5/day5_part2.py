import pygame
import os

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/PermanentMarker-Regular.ttf', 30)

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35)
text = smallfont.render('S T A R T' , True , color)
continueb = pygame.image.load('images_fonts/continue.png')

global scaled_splash, text_splash, text_splash1, counter
splash_page = pygame.image.load('images_fonts/standinimage.png')

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

text_splash = font1.render("As concern of finding the infected person grows...", False, "white")
text_splash1 = font1.render("You focus your efforts solely on finding the infected person!", False, "white")
screen.blit(text_splash, (60,70))
screen.blit(text_splash1, (60,140))
counter=1

global eventvar

eventvar="na"

def sync():
    global scaled_splash, text_splash, text_splash1, counter, eventvar, money, happy
    screen.blit(text , (0,0))
    screen.blit(scaled_splash,(0,0))
    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 

def masterloop():
    global scaled_splash, text_splash, text_splash1, counter, eventvar, money, happy, health
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if counter==100:
            text_splash = font1.render("Oh no! You slip and fall...that hurt!", False, "white")
            text_splash1 = font1.render("-5 health", False, "white")
            health-=5
            counter+=1
            sync()
        
        if counter==101:
            text_splash = font1.render("As concern of finding the infected person grows, whose room do you search?", False, "white")
            text_splash1 = font1.render("[left arrow --> The chef, right arrow --> Lady Mary]", False, "white")
            
            eventvar="e3_1"
            sync()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if eventvar=="na":
                if counter==1:
                    text_splash = font1.render("You hear of a case of food poisoning going around the ship.", False, "white")
                    text_splash1 = font1.render("This could be incredibly detrimental to one's health.", False, "white")
                    counter+=1
                    sync()
                if counter==2:
                    text_splash = font1.render("To start off, whose room do you search?", False, "white")
                    text_splash1 = font1.render("[left arrow --> The mechanic's, right arrow --> Lady Margaret]", False, "white")
                    eventvar="e1"
                    sync()
                
                if counter==4:
                    text_splash = font1.render("You sigh, growing tired and restless...what do you do?", False, "white")
                    text_splash1 = font1.render("[left arrow --> Take a walk, right arrow --> Stay inside]", False, "white")
                    eventvar="e2"
                    sync()
                if counter==7:
                    sync()

                if counter==10:
                    text_splash = font1.render("When you're back on the ship early, you decide to explore some more! Where do you look?", False, "white")
                    text_splash1 = font1.render("[left arrow --> Nurse's chamber, right arrow --> Under the flower vase of commons]", False, "white")
                    eventvar="e3_2"
                    sync()
                if counter==11:
                    text_splash = font1.render("You decide to go back to what you were doing before", False, "white")
                    text_splash1 = font1.render("Events over for today.", False, "white")
                    counter+=2
                    sync()
                if counter==13:
                    fi=open("main_files/infofile.txt")
                    stuff=""
                    for line in fi:
                        stuff+=line
                    stuff=stuff.split(",")
                    file=open("main_files/infofile.txt", "w")
                    info=str(int(stuff[0])+int(health))+"," +str(int(stuff[1])+int(happy)) +","+str(int(stuff[2])+int(hunger))+","+str(int(stuff[3])+int(money))
                    file.write(info)
                    file.close()
                    os.system("python day1/day1_part3.py")
                    pygame.quit()


        if event.type == pygame.KEYDOWN:
            if eventvar=="e1":
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("As you search her room, it's all clear!", False, "white")
                    text_splash1 = font1.render("You get +5 health.", False, "white")
                    health+=5
                    counter=4
                    eventvar="na"
                    sync()
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("All you find are masks and cleared health logs!", False, "white")
                    text_splash1 = font1.render("You get +5 health", False, "white")
                    health+=5
                    counter=4
                    eventvar="na"
                    sync()

            if eventvar=="e2":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("As you go out on the deck for some fresh air, you see the nurse and medic", False, "white")
                    text_splash1 = font1.render("Talking in hushed voices while looking at Sir Cavaret's room...what does it mean?", False, "white")
                    counter=100
                    eventvar="na"
                    sync()
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("You decide to read a book! How relaxing", False, "white")
                    text_splash1 = font1.render("+5 health", False, "white")
                    eventvar="na"
                    health+=5
                    counter=101
                    sync()            
            if eventvar=="e3_1":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("OMG! You find a diary with dark poems reflected on his life!", False, "white")
                    text_splash1 = font1.render("You did it...you found the infected! +10 health +10 wealth", False, "white")
                    eventvar="na"
                    money+=10
                    health+=10
                    counter=11
                    sync()
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("She's not infected...all clear!", False, "white")
                    text_splash1 = font1.render(" +5 health", False, "white")
                    eventvar="na"
                    health+=5
                    counter=11
                    sync()
            
                
            

        scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
        

        
        pygame.display.update()
        clock.tick(60)

while True:
    masterloop()