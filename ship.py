import pygame
import os

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('Neucha-Regular.ttf',60)
font1 = pygame.font.Font('PermanentMarker-Regular.ttf', 90)

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35)
text = smallfont.render('S T A R T' , True , color)


splash_page = pygame.image.load('commons.png')

scaled_splash = pygame.transform.scale(splash_page, (800, 800))


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

variable="commons"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and variable=="commons" or event.key==pygame.K_DOWN and variable=="hallway" or event.key==pygame.K_UP and variable=="rooms":
                variable="stores"
                splash_page = pygame.image.load('stores.png')
            elif event.key == pygame.K_RIGHT and variable=="commons" or event.key==pygame.K_DOWN and variable=="outsideup" or event.key==pygame.K_UP and variable=="outsidedown":       
                variable="captain"
                splash_page = pygame.image.load('captainquarters.png')
            elif event.key == pygame.K_UP and variable=="commons" or event.key==pygame.K_LEFT and variable=="outsideup" or event.key==pygame.K_RIGHT and variable=="hallway":
                variable="arcade"
                splash_page = pygame.image.load('arcade.png')
            elif event.key == pygame.K_DOWN and variable=="commons" or event.key ==pygame.K_LEFT and variable=="outsidedown" or event.key==pygame.K_RIGHT and variable=="rooms":
                variable="medbay"
                splash_page = pygame.image.load('medbay.png')
            elif event.key == pygame.K_LEFT and variable=="arcade" or event.key == pygame.K_UP and variable=="stores":
                variable="hallway"
                splash_page = pygame.image.load('hallway.png')
            elif event.key == pygame.K_DOWN and variable =="captain" or event.key ==pygame.K_RIGHT and variable=="medbay":
                variable="outsidedown"
                splash_page = pygame.image.load('outsidedown.png')
            elif event.key == pygame.K_UP and variable =="captain" or event.key ==pygame.K_RIGHT and variable=="arcade":
                variable="outsideup"
                splash_page = pygame.image.load('outsideup.png')
            elif event.key == pygame.K_DOWN and variable =="stores" or event.key ==pygame.K_LEFT and variable=="medbay":
                variable="rooms"
                splash_page = pygame.image.load('rooms.png')
            elif event.key==pygame.K_DOWN and variable=="arcade" or event.key==pygame.K_RIGHT and variable=="stores" or event.key==pygame.K_UP and variable=="medbay" or event.key==pygame.K_LEFT and variable=="captain":
                variable="commons"
                splash_page = pygame.image.load('commons.png')
            position=pygame.mouse.get_pos()
            scaled_splash = pygame.transform.scale(splash_page, (800, 800))
            screen.blit(scaled_splash,(0,0))
            scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height))

       
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height))
         
    pygame.display.update()
    clock.tick(60)