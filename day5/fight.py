#WHEN SHOP STUFF IS FIGURED OUT READ STUFF FROM CHARINVENTORYSTATS.TXT AND GET HEALTH, ARMOR, FOOD, ETC.

import pygame

pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Two Images and a Button")

image1 = pygame.image.load("day5/image1.png")
image2 = pygame.image.load("day5/image2.png")

image_width = image1.get_width()
image_height = image1.get_height()

font = pygame.font.Font(None, 36)

text = font.render("Attack", True, (255, 255, 255))

text_width = text.get_width()
text_height = text.get_height()

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
            if position[0]>button_x-10 and position[0]<(button_x-10+text_width+20) and position[1]>button_y-10 and position[1]<(button_y-10+text_height+20):
                print("attacked")

    screen.fill((255, 255, 255))

    screen.blit(image1, (image1_x, image1_y))
    screen.blit(image2, (image2_x, image2_y))

    pygame.draw.rect(screen, (0, 0, 255), (button_x - 10, button_y - 10, text_width + 20, text_height + 20))
    screen.blit(text, (button_x, button_y))

    pygame.display.update()

pygame.quit()