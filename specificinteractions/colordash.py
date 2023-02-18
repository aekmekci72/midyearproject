import pygame,sys,random
pygame.init()
screen = pygame.display.set_mode([600, 500])
clock = pygame.time.Clock()

counter, text = 10, '10'.rjust(3)
textt=""

textset=["red","orange","yellow","green","blue","purple", "black"]
colorset=["red","orange","yellow","green","blue","purple","white"]

colortext=""

pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

input_rect = pygame.Rect(100, 100, 140, 32)
thing_rect = pygame.Rect(100,250,140,32)
points_rect=pygame.Rect(100,400,140,32)
  
color_active = pygame.Color('lightskyblue3')

color_passive = pygame.Color('chartreuse4')
color = color_passive
  
active = False
  
points=-1

correctvar=True

run = True
while run:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(e.pos):
                active = True
            else:
                active = False
        if e.type == pygame.KEYDOWN:
            
            if e.key == pygame.K_BACKSPACE:
                textt = textt[:-1]
            else:
                textt += e.unicode
            print(textt)
            if e.key==pygame.K_RETURN:
                print(textt,textss)
                if textt==textss:
                    correctvar=True
        if correctvar==True:
            colorr=colorset[random.randint(0,6)]
            print(colorr)
            textss=textset[random.randint(0,6)]
            colortext=text
            thing_rect=pygame.Rect(100, 100, 140,32)
            correctvar=False
            points+=1
            textt=""

    if active:
        color = color_active
    else:
        color = color_passive
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, input_rect)
    pygame.draw.rect(screen, colorr, thing_rect)
    pygame.draw.rect(screen, color, points_rect)
  
    text_surface = font.render(text, True, (0, 0, 0))
    textt_surface = font.render(textt, True, (255,255,255))
      
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    screen.blit(textt_surface, (input_rect.x, input_rect.y+55))
      
    input_rect.w = max(100, text_surface.get_width()+10)
    
    pygame.display.flip()
    clock.tick(60)