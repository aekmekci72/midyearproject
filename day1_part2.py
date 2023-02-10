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
splash_page = pygame.image.load('standinimage.png')

scaled_splash = pygame.transform.scale(splash_page, (800, 800))


global money
money=0

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('You are casually hanging out on the ship when you hear the alarm blare', False, 'white')
text_splash1 = font1.render('You dash to the captain room and look outside from behind the wheel', False, 'white')
counter=1

global eventvar

eventvar="na"

def masterloop():
    global scaled_splash, text_splash, text_splash1, counter, eventvar

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if eventvar=="na":
                if counter==1:
                    text_splash = font1.render("There, you see dangerous waters.", False, "white")
                    text_splash1 = font1.render("On the left, there is a thunderstorm, and on the right, there is a whirlpool", False, "white")
                    counter+=1
                if counter==2:
                    text_splash = font1.render("Which way do you want to direct your ship?", False, "white")
                    text_splash1 = font1.render("[left arrow --> thunderstorm, right arrow --> whirlpool]", False, "white")
                    eventvar="e1"
                
                if counter==4:
                    text_splash = font1.render("Now, you are faced with another challenge...", False, "white")
                    text_splash1 = font1.render("Towards your left, you see sharks, and towards your right, you see pirhanas.", False, "white")
                    counter+=1
                if counter==5:
                    text_splash = font1.render("Which way do you want to direct your ship?", False, "white")
                    text_splash1 = font1.render("[left arrow --> sharks, right arrow --> piranhas]", False, "white")
                    eventvar="e2"
                if counter==6:
                    text_splash = font1.render("You navigate your ship towards the sharks...", False, "white")
                    text_splash1 = font1.render("And are surprised to see they did not attack you.", False, "white")
                    counter+=1
                if counter==7:
                    text_splash = font1.render("In addition, you discover a new species of shark!", False, "white")
                    text_splash1 = font1.render("You get 10 coins for your achievement", False, "white")
                    counter+=1
                if counter==8:
                    text_splash = font1.render("Anyways, you survived!", False, "white")
                    text_splash1 = font1.render("You see something in the distance...", False, "white")
                    counter+=1

        if event.type == pygame.KEYDOWN:
            print("keypress")
            if eventvar=="e1":
                print('event1')
                if event.key==pygame.K_RIGHT:
                    print('right')
                    counter+=2
                    text_splash = font1.render("You navigate your ship towards the whirlpool...", False, "white")
                    text_splash1 = font1.render("And are able to circumnavigate the dangers.", False, "white")
                    counter+=1
                    eventvar="na"
                if event.key==pygame.K_LEFT:
                    os.system("python death.py 1")
                    pygame.quit()

            if eventvar=="e2":
                if event.type==pygame.K_LEFT:
                    counter+=1
                    eventvar="na"
                if event.type==pygame.K_RIGHT:
                    text_splash = font1.render("You steer your ships towards the fishies, surprised when they eat some of your boat!", False, "white")
                    text_splash1 = font1.render("You have to spend 10 coins to fix it. ", False, "white")
                    eventvar="na"
                    counter=8
            
            
                
            

                
        screen.blit(text , (0,0))
        position=pygame.mouse.get_pos()
        screen.blit(scaled_splash,(0,0))
        screen.blit(text_splash, (60,70))
        screen.blit(text_splash1, (60,140))

        scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
                
        pygame.display.update()
        clock.tick(60)

while True:
    masterloop()
    