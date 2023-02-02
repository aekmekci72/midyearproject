import pygame, os

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('Neucha-Regular.ttf',60)
font1 = pygame.font.Font('Neucha-Regular.ttf', 90)

screen = pygame.display.set_mode()
color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Ariel',35)
text = smallfont.render('S T A R T' , True , color)
continueb = pygame.image.load('continue.png')


splash_page = pygame.image.load('ship_sink.jpeg')
splash_water = pygame.image.load('water_drop.png')

scaled_splash = pygame.transform.scale(splash_page, (width/2, height/2))
scaled_water = pygame.transform.scale(splash_water, (width/2, height/4))
splash_water1 = pygame.transform.flip(scaled_water, True, False)


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('Sick Or Swim', False, 'white')
text_splash_name = font.render('By: Shreeja And Anna', False, 'white')

play_button = pygame.image.load('play_button.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            (width/2-500,height/2+200)
            if width/2-500 <= pygame.mouse.get_pos()[0] <= width/2-360 and height/2+200 <= pygame.mouse.get_pos()[1] <= height/2+400:
                os.system("howtoplay.py 1")
                pygame.quit()
        
    screen.blit(text , (width/2+50,height/2))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))
    blit_alpha(screen, scaled_water,(0,0),150)
    blit_alpha(screen, splash_water1,(0,450),150)
    screen.blit(text_splash, (200,70))
    screen.blit(text_splash_name, (165,570))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
    scaled_water = pygame.transform.smoothscale(scaled_water, (width, height)) 
    screen.blit(continueb, (width/2-500,height/2+200))
    continueb = pygame.transform.smoothscale(continueb, (140, 200)) 
         
    pygame.display.update()
    clock.tick(60)