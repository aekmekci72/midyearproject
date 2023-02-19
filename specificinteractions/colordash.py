import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Color Game")

typed_color=""

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Define the fonts to be used for the game
font = pygame.font.Font(None, 36)

# Define the countdown timer for the game
COUNTDOWN_TIMER = 25

# Define the colors to be used in the game
COLORS = {
    "red": RED,
    "green": GREEN,
    "blue": BLUE,
    "yellow": YELLOW,
    "cyan": CYAN,
    "magenta": MAGENTA
}

# Set up the initial game state
current_color1 = random.choice(list(COLORS.keys()))
current_color2 = random.choice(list(COLORS.keys()))
score = 0
time_left = COUNTDOWN_TIMER * 60

# Define a function to update the game state
def update_game():
    global current_color1,current_color2, score, time_left
    if current_color2 == typed_color.lower():
        score += 1
        current_color2 = random.choice(list(COLORS.keys()))
        current_color1 = random.choice(list(COLORS.keys()))
    

# Set up the game loop
game_running = True
while game_running:
    # Handle events
    time_left -= 0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
            else:
                # Check if the user typed the correct color
                if event.key == pygame.K_RETURN:
                    typed_color = typed_color.lower()
                    update_game()
                    typed_color = ""
                elif event.key == pygame.K_BACKSPACE:
                    typed_color = typed_color[:-1]
                elif event.unicode.isalpha():
                    typed_color += event.unicode

    # Draw the background and the text
    background_color = COLORS[current_color2]
    game_display.fill(background_color)
    text = font.render(current_color1.capitalize(), True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    game_display.blit(text, text_rect)

    # Draw the score and the time left
    score_text = font.render("Score: {}".format(score), True, WHITE)
    score_text_rect = score_text.get_rect(topright=(WINDOW_WIDTH-10, 10))
    game_display.blit(score_text, score_text_rect)
    time_text = font.render("Time left: {}s".format(int(time_left/60)), True, WHITE)
    time_text_rect = time_text.get_rect(topleft=(10, 10))
    game_display.blit(time_text, time_text_rect)

    # Draw the typed text
    typed_text = font.render(typed_color, True, WHITE)
    typed_rect = typed_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2+50))
    game_display.blit(typed_text, typed_rect)

    # Update the screen
    pygame.display.update()

    # Check if the game is over
    if time_left <= 0:
        game_running = False