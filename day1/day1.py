import pygame
import os

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/PermanentMarker-Regular.ttf', 90)

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35)
text = smallfont.render('S T A R T' , True , color)
continueb = pygame.image.load('images_fonts/continue.png')

splash_page = pygame.image.load('images_fonts/ship_sink.jpeg')
splash_water = pygame.image.load('images_fonts/water_drop.png')

scaled_splash = pygame.transform.scale(splash_page, (800, 800))
scaled_water = pygame.transform.scale(splash_water, (800, 495))
splash_water1 = pygame.transform.flip(scaled_water, True, False)


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('DAY 1', False, 'white')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            (width/2-500,height/2+200)
            if width/2-500 <= pygame.mouse.get_pos()[0] <= width/2-360 and height/2+200 <= pygame.mouse.get_pos()[1] <= height/2+400:
                f = open("main_files/infofile.txt", "w")
                
                f.write("75,35,60,10")
                f.close()
                os.system("python day1/day1_part1.py 1")
                pygame.quit()
        
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))
    blit_alpha(screen, scaled_water,(0,0),150)
    blit_alpha(screen, splash_water1,(0,450),150)
    screen.blit(text_splash, (60,70))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
    scaled_water = pygame.transform.smoothscale(scaled_water, (width, height)) 
    screen.blit(continueb, (width/2-500,height/2+200))
    continueb = pygame.transform.smoothscale(continueb, (140, 200)) 
         
    pygame.display.update()
    clock.tick(60)