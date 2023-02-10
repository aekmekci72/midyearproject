import pygame
import os

global surv1
surv1=True

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


splash_page = pygame.image.load('images_fonts/standinimage.png')

scaled_splash = pygame.transform.scale(splash_page, (800, 800))


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('You explore the town, and find money! + 15 money :)', False, 'white')
text_splash1 = font1.render('You see a cat and dog, do you want take them onboard (right), or leave them behind (left)?', False, 'white')
counter=1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                os.system("python day1/events/event1_3leave.py 1")
                pygame.quit()
            elif event.key ==pygame.K_RIGHT:
                os.system("python day1/events/event1_3take.py 1")
                pygame.quit()

        
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))
    screen.blit(text_splash, (60,70))
    screen.blit(text_splash1, (60,140))

    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
         
    pygame.display.update()
    clock.tick(60)