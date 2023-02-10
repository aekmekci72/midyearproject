import pygame
import os
import time

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


splash_page = pygame.image.load('images_fonts/event1_1_1.png')
scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))



def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)  
    target.blit(temp, location)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                os.system("python death.py 1")
                pygame.quit()
            elif event.key ==pygame.K_RIGHT:
                os.system("python day1/events/event1_1surv.py 1")
                pygame.quit()
                
            
            position=pygame.mouse.get_pos()
            scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
    
        
    pygame.display.update()
        
    text_splash=font1.render("", False, 'black')
    screen.blit(text_splash, (60,70))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height))
         