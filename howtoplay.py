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


splash_page = pygame.image.load('howtoplayback.png')
continueb = pygame.image.load('continue.png')
#splash_water = pygame.image.load('water_drop.png')

scaled_splash = pygame.transform.scale(splash_page, (width/2, height/2))
#scaled_water = pygame.transform.scale(splash_water, (width/2, height/4))
#splash_water1 = pygame.transform.flip(scaled_water, True, False)


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

text_splash = font1.render('How to Play', False, 'white')
text_splash_name = font.render('this is the game description ig', False, 'white')

play_button = pygame.image.load('play_button.png').convert_alpha()

# class Button():
#     def __init__(self, x, y, width,height, image):
#         self.image=image
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x,y)
#         self.width=width
#         self.height=height
   
#     def draw(self):
#         screen.blit(self.image, (self.rect.x, self.rect.y))

# start_button= Button(500, 500, 100,100,play_button)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            (width/2-500,height/2+200)
            if width/2-500 <= pygame.mouse.get_pos()[0] <= width/2-360 and height/2+200 <= pygame.mouse.get_pos()[1] <= height/2+400:
                os.system("screen2.py 1")
                pygame.quit()
        
    screen.blit(text , (width/2+50,height/2))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))
   # blit_alpha(screen, scaled_water,(0,0),150)
   # blit_alpha(screen, splash_water1,(0,450),150)
    screen.blit(text_splash, (200,70))
    screen.blit(continueb, (width/2-500,height/2+200))
    continueb = pygame.transform.smoothscale(continueb, (140, 200)) 
    screen.blit(text_splash_name, (165,270))
    #scaled_water = pygame.transform.scale(splash_water, (width/2, height/4))
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