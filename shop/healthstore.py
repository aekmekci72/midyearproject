import pygame

pygame.init()

width = 400
height = 300
screen = pygame.display.set_mode((400,300))
money=0

infofile=open("main_files/infofile.txt")
for line in infofile:
    line=line.strip()
    line=line.split(",")
    money=float(line[3])

pygame.display.set_caption("Sink or Swim Shop")

font = pygame.font.SysFont('Arial',15)
items = [("small-health-potion(+5 health)", 10), ("medium-health-potion(+10 health)", 17.5), ("large-health-potion(+20 health)", 30)]

inventory = []

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            x = position[0]
            y = position[1]

            for i in range(len(items)):
                item = items[i]
                text = font.render(f"{item[0]} - {item[1]} dollars", True, (0,0,0))
                rect = text.get_rect()
                rect.x = 10
                rect.y = 10 + i * 30
                if rect.collidepoint(position):
                    if money >= item[1]:
                        inventory.append(item[0])
                        money -= item[1]
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e:
                stuff=line
                stuff[3]=money
                infofile=open("main_files/infofile.txt","w")
                for thing in stuff:
                    t=str(thing)+","
                    infofile.write(t)
                infofile.close()

                invent=open("main_files/inventory.txt")
                stuff=[]
                for line in invent:
                    line=line.strip()
                    line=line.split()
                    for thing in line:
                        stuff.append(thing)
                for thing in inventory:
                    stuff.append(thing)
                i=open("main_files/inventory.txt","w")
                for thing in stuff:
                    a=thing+","
                    i.write(a)
                i.close()

                
                pygame.quit()

    screen.fill((255,255,255))

    inventory_text = font.render(f"Inventory: {' '.join(inventory)}", True, (0,0,0))
    screen.blit(inventory_text, (10, height - 60))

    money_text = font.render(f"Money: {money}", True, (0,0,0))
    screen.blit(money_text, (10, height - 90))

    instru = font.render("Press e to exit", True, (0,0,0))
    screen.blit(instru, (10, height - 30))

    for i in range(len(items)):
        item = items[i]
        text = font.render(f"{item[0]} - {item[1]} dollars", True, (0,0,0))
        rect = text.get_rect()
        rect.x = 10
        rect.y = 10 + i * 30
        screen.blit(text, rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()