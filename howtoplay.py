import pygame, os

pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('Neucha-Regular.ttf',60)
font1 = pygame.font.Font('Neucha-Regular.ttf', 90)
font2=pygame.font.Font('Neucha-Regular.ttf', 30)

screen = pygame.display.set_mode()
color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Ariel',35)
text = smallfont.render('S T A R T' , True , color)


splash_page = pygame.image.load('howtoplayback.png')
continueb = pygame.image.load('continue.png')

scaled_splash = pygame.transform.scale(splash_page, (width/2, height/2))


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('How to Play', False, 'white')
text_splash_name = font2.render('this is the game description ig', False, 'white')

play_button = pygame.image.load('play_button.png').convert_alpha()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            (width/2-500,height/2+200)
            if width/2-500 <= pygame.mouse.get_pos()[0] <= width/2-360 and height/2+200 <= pygame.mouse.get_pos()[1] <= height/2+400:
                os.system("python screen2.py 1")
                pygame.quit()
        
    screen.blit(text , (width/2+50,height/2))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))
    screen.blit(text_splash, (200,70))
    screen.blit(continueb, (width/2-500,height/2+200))
    continueb = pygame.transform.smoothscale(continueb, (140, 200)) 
    screen.blit(text_splash_name, (165,270))
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height)) 
    
         
    pygame.display.update()
    clock.tick(60)





while True:
    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT:
            pygame.quit()
              
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= pygame.mouse.get_pos()[0] <= width/2+240 and height/2 <= pygame.mouse.get_pos()[1] <= height/2+40:
                os.system("screen2.py 1")
                pygame.quit()
                  
    screen.fill((0,0,0))
      
    if width/2 <= pygame.mouse.get_pos()[0] <= width/2+140 and height/2 <= pygame.mouse.get_pos()[1] <= height/2+40:
        pygame.draw.rect(screen,color_light,[width/2,height/2,240,40])
          
    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2,240,40])
      
    screen.blit(text , (width/2+50,height/2))
      
    pygame.display.update()