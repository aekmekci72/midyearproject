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

global scaled_splash, scaled_start, text_splash, text_splash1, counter, text_splash2
splash_page = pygame.image.load('images_fonts/persontalk.png')
start_img = pygame.image.load('images_fonts/talking.jpeg')
scaled_start = pygame.transform.scale(start_img, (1600, 1068))


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

text_start = font1.render('You see somebody in the commons of the ship', False, 'black')
text_start1 = font1.render('You decide to meet them!', False, 'black')
text_splash=font1.render('', False, "black")
text_splash1=font1.render('', False, "black")
text_splash2 = font.render('', False, "black")
counter=1

global eventvar

eventvar="na"

screen.blit(scaled_start, (0,0))
screen.blit(text_start , (60,80))
screen.blit(text_start1, (60, 140))


def sync():
    global scaled_splash, text_splash, text_splash1, text_splash2, counter, eventvar, money, happy
    screen.blit(text , (0,0))
    screen.blit(scaled_splash,(0,0))
    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))
    screen.blit(text_splash2, (60,210))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
def masterloop():
    global scaled_splash, text_splash, text_splash1, text_splash2, counter, eventvar, money, happy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if counter==100:
            eventvar="e3_1"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if eventvar=="na":
                if counter==1:
                    text_splash = font1.render("Hiii I'm person 1!", False, "black")
                    text_splash1 = font1.render("I'm glad to hear that we finally have a new captain!", False, "black")
                    text_splash2=font1.render('', False, "black")
                    sync()
                    counter+=1
                    
                if counter==2:
                    text_splash = font1.render("I am a crewmate on this ship, and am happy to oblige to your orders", False, "black")
                    text_splash1 = font1.render("[RIGHT-INCITE CONVO ABOUT WHY PERSON ON SHIP]", False, "black")
                    text_splash2 = font1.render("[LEFT-ASK THEM WHO THE PREVIOUS CAPTAIN WAS]", False, "black")
                    eventvar="e1"
                    sync()
                
                if counter==4:
                    text_splash = font1.render("Anyways, the disease. *laughs", False, "black")
                    text_splash1 = font1.render("I'm sorry to hear that your family suffered. Mine did too :(", False, "black")
                    text_splash2=font1.render('', False, "black")
                    counter+=1
                    sync()
                if counter==5:
                    ext_splash = font1.render("ADD MORE STUFF", False, "black")
                    text_splash1 = font1.render("IN THE FUTURE WHEN STORYLINE MORE DEVELOPED", False, "black")
                    text_splash2=font1.render('', False, "black")
                    counter=13
                    sync()
                if counter==13:
                    pygame.quit()
                

        if event.type == pygame.KEYDOWN:
            if eventvar=="e1":
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("Why am I on this ship?", False, "black")
                    text_splash1 = font1.render("Let's just say the disease had a huge toll on me.", False, "black")
                    text_splash2=font1.render('', False, "black")
                    counter=4
                    eventvar="na"
                    sync()
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("Who was the previous captain?", False, "black")
                    text_splash1 = font1.render("He was kind of mean, we think he had the disease before he vanished...", False, "black")
                    text_splash2=font1.render('', False, "black")
                    counter=4
                    eventvar="na"
                    sync()

            if eventvar=="e2":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You navigate your ship towards the sharks... \nAnd are surprised to see they did not attack you.", False, "white")
                    text_splash1 = font1.render("In addition, you discover a new species of shark! \nYou get 10 coins for your achievement", False, "white")
                    text_splash2=font1.render('', False, "black")
                    money+=10
                    counter=9
                    eventvar="na"
                    sync()
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("You steer your ships towards the fishies, surprised when they eat some of your boat!", False, "white")
                    text_splash1 = font1.render("You have to spend 10 coins to fix it. ", False, "white")
                    text_splash2=font1.render('', False, "black")
                    eventvar="na"
                    money-=10
                    counter=9
                    sync()
            if eventvar=="e3":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You pass the town.", False, "white")
                    text_splash1 = font1.render("Maybe you missed something important...", False, "white")
                    text_splash2=font1.render('', False, "black")
                    eventvar="na"
                    counter=11
                    sync()
                if event.key==pygame.K_RIGHT:
                    eventvar="na"
                    text_splash = font1.render("You look around and see some resources! \nYou eat some food and get +10 on your hunger bar!", False, "white")
                    text_splash1 = font1.render("You see a cat and a dog. Do you (right) leave them or (left) take them?", False, "white")
                    text_splash2=font1.render('', False, "black")
                    counter=100
                    sync()
            if eventvar=="e3_1":
                if event.key==pygame.K_LEFT:
                    text_splash = font1.render("You take the cat and dog with you! Hopefully they aren't sick", False, "white")
                    text_splash1 = font1.render("You gain 10 happiness!", False, "white")
                    text_splash2=font1.render('', False, "black")
                    counter=11
                    happy+=10
                    eventvar="na"
                    sync()
                if event.key==pygame.K_RIGHT:
                    text_splash = font1.render("Who knows, the cat and dog might be sick. You leave them", False, "white")
                    text_splash1 = font1.render("You lose 10 happiness!", False, "white")
                    text_splash2=font1.render('', False, "black")
                    eventvar="na"
                    happy-=10
                    counter=11
                    sync()
                             
            
                
            

        scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
        

        
        file=open("day1/charspeak.txt","w")
        file.write("character spoke")
        file.close()

        file1=open("day1/mhm.txt","w")
        file1.write('')
        file1.close()

        pygame.display.update()
        clock.tick(60)

while True:
    masterloop()
    