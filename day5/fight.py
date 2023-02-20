#WHEN SHOP STUFF IS FIGURED OUT READ STUFF FROM INVENTORY.TXT AND GET HEALTH, ARMOR, FOOD, ETC.

import pygame

pygame.init()

attackstuff=["Dagger(5 damage)","Bow(3 damage)", "Sword(10 damage)"]
armorstuff=["Helmet(+2 protection)","Chestplate(+7 protection)","Boots(+1 protection)"]
foodstuff=["Apple(+2 hunger)", "Bread(+5 hunger)", "Steak(+10 hunger)"]
healthstuff=["small-health-potion(+5 health)", "medium-health-potion(+10 health)", "large-health-potion(+20 health)"]


infofile=open("main_files/infofile.txt")
for line in infofile:
    line=line.strip()
    line=line.split(",")

    health=float(line[0])
    happiness=float(line[1])
    hunger=float(line[2])
    money=float(line[3])

items=[]

inventory=open("main_files/inventory.txt")
extrastrength=0
moreproct=0
for line in inventory:
    print(line)
    line=line.split(",")
    print(line)
for thing in line:
    thingg=thing
    thing=thing.split("-")
    print(thing)
    if thing[0] in attackstuff:
        extrastrength+=float(thing[1])
    if thing[0] in armorstuff:
        moreproct+=float(thing[1])
    else:
        items.append(thingg)

opponenthealth=75
opponentdext=50
dext=35+(hunger/4)
opponentstrength=60
opponentstrength-=moreproct
strength=40+extrastrength






screen_width = 1000
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Final Battle")

image1 = pygame.image.load("day5/image1.png")
image2 = pygame.image.load("day5/image2.png")

image_width = image1.get_width()
image_height = image1.get_height()

font = pygame.font.Font(None, 36)

textt = font.render("Attack", True, (255, 255, 255))

text_width = textt.get_width()
text_height = textt.get_height()

image1_x = 50
image1_y = (screen_height - image_height) // 2
image2_x = screen_width - image_width - 50
image2_y = (screen_height - image_height) // 2

button_x = (screen_width - text_width) // 2
button_y = (screen_height - text_height) // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            if position[0]>button_x+190 and position[0]<(button_x+190+text_width+20) and position[1]>button_y-10 and position[1]<(button_y-10+text_height+20):
                print("attacked")
            for i in range(len(items)):
                item = items[i]
                text = font.render(item, True, (0,0,0))
                rect = text.get_rect()
                rect.x = 10
                rect.y = 10 + i * 30
                if rect.collidepoint(position):
                    print(item)
                    g=items.index(item)
                    print(g)
                    print(items)
                    items.remove(items[g])

    screen.fill((255, 255, 255))

    screen.blit(image1, (image1_x+200, image1_y))
    screen.blit(image2, (image2_x+200, image2_y))

    pygame.draw.rect(screen, (0, 0, 255), (button_x +190, button_y - 10, text_width + 20, text_height + 20))
    screen.blit(textt, (button_x, button_y))

    for i in range(len(items)):
        item = items[i]
        text = font.render(item, True, (0,0,0))
        rect = text.get_rect()
        rect.x = 10
        rect.y = 10 + i * 30
        screen.blit(text, rect)

    pygame.display.update()

pygame.quit()