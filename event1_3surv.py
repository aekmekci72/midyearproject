import pygame
import os

global surv1
surv1=True

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('Neucha-Regular.ttf',60)
font1 = pygame.font.Font('PermanentMarker-Regular.ttf', 30)

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35)
text = smallfont.render('S T A R T' , True , color)
continueb = pygame.image.load('continue.png')


splash_page = pygame.image.load('standinimage.png')

scaled_splash = pygame.transform.scale(splash_page, (800, 800))


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('Meh-you pass the town, it could be dangerous', False, 'white')
text_splash1 = font1.render('You survived!', False, 'white')
counter=1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            f = open("infofile.txt", "w")
            f.write("event1_3_meh")
            f.close()
            os.system("python ship1.py 1")

        
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))
    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))

    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
         
    pygame.display.update()
    clock.tick(60)