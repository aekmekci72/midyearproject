import pygame
import os
import time

global surv1
global health, happiness, hunger,money



pygame.init()
screen= pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images_fonts/Neucha-Regular.ttf',60)
font1 = pygame.font.Font('images_fonts/PermanentMarker-Regular.ttf', 20)
global scaled_splash

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',35)
text = smallfont.render('S T A R T' , True , color)


splash_page = pygame.image.load('day4/kitchenn.png')
scaled_splash = pygame.transform.scale(splash_page, (800, 800))



def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)


scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
health = 100
wealth = 100

clock_game = 0
global bookshelfchecked,key1,listenunlock1,listenunlock11,listenunlock111,key2,listenunlock2,listenunlock22,listenunlock222,listenesc
bookshelfchecked=False
key1=False
key2=False
booleee=False

listenesc=False

global screenn
screenn="captain"
var=0
listenunlock1=False
listenunlock11=False
listenunlock111=False

listenunlock2=False
listenunlock22=False
listenunlock222=False

global wheelpuzzlestr

wheelpuzzlestr=""

class Button:
    
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = font.render('Back', True, (0,0,0))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text, (self.rect.centerx - self.text.get_width() // 2, self.rect.centery - self.text.get_height() // 2))

    def handle_event(self, event):
        global screenn,scaled_splash
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.color = (225,0,0)
                screenn="captain"
                print(screenn)
                splash_page = pygame.image.load('day4/kitchenn.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                screen.blit(scaled_splash,(0,0))


def clickedOven():
    pass
def clickedPuzzle():
    pass
def clickedFridge():
    pass
def clickedMicrowave():
    pass
def clickedClock():
    pass

while True:

    back = Button(0, 0, 200, 50, (225,225,225))
    

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN and screenn=="captain":

            position=pygame.mouse.get_pos()
            print(position)
            if position[0]>465 and position[0]<563:
                if position[1]> 69 and position[1]<170:
                    clickedClock()
            if position[0]>37 and position[0]<419:
                if position[1]>50 and position[1]<570:
                    clickedFridge()
            if position[0]>1220 and position[0]<1446:
                if position[1]>297 and position[1]<415:
                    clickedMicrowave()
            if position[0]>855 and position[0]<1189:
                if position[1]>385 and position[1]<550:
                    clickedOven()
          #  if position[0]>1041 and position[0]<1261:
           #     if position[1]>98 and position[1]<255:
            #        clickedPuzzle()
        if event.type==pygame.MOUSEBUTTONDOWN and screenn=="drawer":
            if listenunlock111==True:
                splash_page = pygame.image.load('day2/openeddrawer.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                screen.blit(scaled_splash,(0,0))

            elif listenunlock11==True:
                splash_page = pygame.image.load('day2/unlockeddrawer.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                screen.blit(scaled_splash,(0,0))
                listenunlock111=True

            elif listenunlock1==True:
                splash_page = pygame.image.load('day2/lockeddrawer.png')
                scaled_splash = pygame.transform.smoothscale(splash_page, (width, height))
                listenunlock11=True
                screen.blit(scaled_splash,(0,0))
        if event.type==pygame.MOUSEBUTTONDOWN and screenn=="wheel":
            pass
        if event.type==pygame.MOUSEBUTTONDOWN and screenn=="rug":
            if listenesc==True:
                os.system("python day4/day4_part2.py")
                pygame.quit()


            
        
        
        
    screen.blit(scaled_splash,(0,0))
    back.handle_event(event)
    back.draw(screen)
    
        
    pygame.display.update()
        
    text_splash=font1.render("", False, 'black')
    screen.blit(text_splash, (60,70))
    screen.blit(text , (0,0))
    position=pygame.mouse.get_pos()
    screen.blit(scaled_splash,(0,0))