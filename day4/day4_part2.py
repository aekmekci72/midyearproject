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

text_splash = font1.render("As you stop at another port city to get more food...you come across some merchants selling stuff", False, "white")
text_splash1 = font1.render("This could be interesting, you might learn some new stuff!", False, "white")
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
        if counter==101:
            text_splash = font1.render("You come across a great suit in town...do you buy it? Maybe you can impress a certain someone! ", False, "white")
            text_splash1 = font1.render("[left arrow --> Hell yeah, right arrow --> Pass]", False, "white")
            
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
                    text_splash = font1.render("Do you buy the stone claiming to be of good fortune (costs $10)?", False, "white")
                    text_splash1 = font1.render("[left arrow --> yes, right arrow --> nah]", False, "white")
                    eventvar="e1"
                    sync()
                
                if counter==4:
                    text_splash = font1.render("Now, you are faced with another challenge...", False, "white")
                    text_splash1 = font1.render("Lightning strikes and part of the boat was destroyed!", False, "white")
                    counter+=1
                    sync()
                if counter==5:
                    text_splash = font1.render("In town, you're entranced by a second hand journal...Do you buy it?", False, "white")
                    text_splash1 = font1.render("[left arrow --> No, right arrow --> Of course]", False, "white")
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
                    text_splash = font1.render("Wow. Keep up the savings!", False, "white")
                    text_splash1 = font1.render("You get +5 wealth.", False, "white")
                    money+=7
                    counter=4
                    eventvar="na"
                    sync()
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You take the stone: Wow. You feel a sense of zen wash over yourself. (+5 health)(-10 wealth)", False, "white")
                    text_splash1 = font1.render("The stone helps you get a vision...You realize that the plumber doesn't have the disease!!", False, "white")
                    health-=7
                    counter=4
                    eventvar="na"
                    sync()

            if eventvar=="e2":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("Oh well!", False, "white")
                    text_splash1 = font1.render("You don't gain or lose anything...", False, "white")
                    counter=10
                    eventvar="na"
                    sync()
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("How perfect for mental health! (+5 health)", False, "white")
                    text_splash1 = font1.render("You end up finding a note saying: 'Never trust a skinny chef'....you wonder what that means...", False, "white")
                    eventvar="na"
                    health+=10
                    counter=101
                    sync()            
            if eventvar=="e3_1":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You definitely got yourself a date once you make it out of here!", False, "white")
                    text_splash1 = font1.render("Plus, you find some $5 in the suit pocket! -10 wealth, +5health, + 5wealth", False, "white")
                    eventvar="na"
                    money+=5
                    money-=10
                    health+=5
                    counter=11
                    sync()
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("Oh well...at least you saved money", False, "white")
                    text_splash1 = font1.render(" +5 wealth, -5 health", False, "white")
                    eventvar="na"
                    health-=5
                    money+=5
                    counter=11
                    sync()
                             
            if eventvar=="e3_2":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("In the nurse's chamber, you end up finding that none of the crewmates had the sickness!", False, "white")
                    text_splash1 = font1.render("Whew! What a relief. (+5 health)", False, "white")
                    eventvar="na"
                    health+=5
                    counter=101
                    sync()
                if event.key==pygame.K_RIGHT:
                    eventvar="na"
                    text_splash = font1.render("You end up finding a diary which says: 'never trust a skinny chef'...", False, "white")
                    text_splash1 = font1.render("Hmm you wonder what that means... +health", False, "white")
                    health+=5
                    counter=101
                    sync()

            
                
            

        scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
        

        
        pygame.display.update()
        clock.tick(60)

while True:
    masterloop()