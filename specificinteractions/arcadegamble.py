import pygame

# --- constants --- (UPPER_CASE names)

DISPLAY_WIDTH  = 900
DISPLAY_HEIGHT = 600

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (250,  0,  0)
GREEN = (  0,250,  0)
BRIGHT_RED   = (200,  0,  0)
BRIGHT_GREEN = (  0,200,  0)

# --- classes --- (CamelCase names)

# empty

# --- functions --- (lower_case names)

def button_check(button):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if button['rect'].collidepoint(mouse):
        if click[0] == 1 and button['action']:
            button['action']()         


def button_draw(button):
    font = pygame.font.SysFont("comicsansms", 20)

    mouse = pygame.mouse.get_pos()

    if button['rect'].collidepoint(mouse):
        color = button['ac']
    else:
        color = button['ic']

    pygame.draw.rect(game_display, color, button['rect'])

    image, rect = text_objects(button['msg'], font)
    rect.center = button['rect'].center
    game_display.blit(image, rect)

def text_objects(text, font):
    image = font.render(text, True, BLACK)
    rect  = image.get_rect()
    return image, rect

def message_display(text):
    font = pygame.font.Font("Arial" ,60)

    image, rect = text_objects(text, font)
    rect.center = game_display_rect.center
    game_display.blit(image, rect)

    pygame.display.update()

def quit_game():
    pygame.quit()
    quit()

def game_intro():
    font = pygame.font.SysFont("comicsansms", 115)

    game_display.fill(WHITE)

    image, rect = text_objects("A math's game", font)
    rect.center = game_display_rect.center
    game_display.blit(image, rect)

    buttons = [
        {
            'msg': 'GO!',
            'rect': pygame.Rect(150, 450, 100, 50),
            'ac': GREEN, 
            'ic': BRIGHT_GREEN,
            'action': game_loop,
        },
        {
            'msg': 'Quit',
            'rect': pygame.Rect(550, 450, 100, 50),
            'ac': RED,   
            'ic': BRIGHT_RED,
            'action': game_loop
        }
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_check(buttons[0])
                button_check(buttons[1])

        button_draw(buttons[0])
        button_draw(buttons[1])

        pygame.display.update()

def game_loop():
    font = pygame.font.SysFont("comicsansms",48)

    game_display.fill(WHITE)

    image, rect = text_objects("A math's game", font)
    rect.center = (game_display_rect.centerx, 100)
    game_display.blit(image, rect)

    image, rect = text_objects("Pick a choice", font)
    rect.center = (game_display_rect.centerx, 200)
    game_display.blit(image, rect)

    image, rect = text_objects("1 QUESTION", font)
    rect.center = (game_display_rect.centerx, 280)
    game_display.blit(image, rect)

    buttons = [
        {
            'msg': 'Option1',
            'rect': pygame.Rect(120, 350, 300, 150),
            'ac': RED, 
            'ic': BRIGHT_RED,
            'action': option1_loop,
        },
        {
            'msg': 'Option2',
            'rect': pygame.Rect(520, 350, 300, 150),
            'ac': RED,   
            'ic': BRIGHT_RED,
            'action': None
        }
    ]

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_check(buttons[0])
                button_check(buttons[1])

        button_draw(buttons[0])
        button_draw(buttons[1])

        pygame.display.update()

def option1_loop():
    font = pygame.font.SysFont("comicsansms",48)

    game_display.fill(WHITE)

    image, rect = text_objects("A math's game", font)
    rect.center = (game_display_rect.centerx, 100)
    game_display.blit(image, rect)

    image, rect = text_objects("Pick a choice", font)
    rect.center = (game_display_rect.centerx, 200)
    game_display.blit(image, rect)

    image, rect = text_objects("2 QUESTION", font)
    rect.center = (game_display_rect.centerx, 280)
    game_display.blit(image, rect)

    buttons = [
        {
            'msg': 'Option1.1',
            'rect': pygame.Rect(120, 350, 300, 150),
            'ac': RED, 
            'ic': BRIGHT_RED,
            'action': option1_loop,
        },
        {
            'msg': 'Option2.1',
            'rect': pygame.Rect(520, 350, 300, 150),
            'ac': RED,   
            'ic': BRIGHT_RED,
            'action': None
        }
    ]

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_check(buttons[0])
                button_check(buttons[1])

        button_draw(buttons[0])
        button_draw(buttons[1])

        pygame.display.update()

# --- main ---

pygame.init()

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
game_display_rect = game_display.get_rect()

pygame.display.set_caption("A MATH'S GAME")

game_intro()