import pandas as pd
import pygame
import sys

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# Create a Pygame window
pygame_icon = pygame.image.load('icon.png')
pygame.display.set_icon(pygame_icon)
window_size = (500, 800)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('MedTrack')

base_font = pygame.font.Font(None, 32)
user_text = ''

# create rectangle
input_rect = pygame.Rect(200, 200, 140, 32)

# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')

# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color = color_passive
active = False

df = pd.read_csv("Drug.csv",
                 header=0,
                 usecols=["Drug", "Information", "Effective"])
drags = df.Drug.unique()
drags = list(drags)
print(drags)

board = [[0 for i in range(50)] for j in range(25)]

for i in board:
    print(i)
page = 0
font = pygame.font.Font(None, 24)
button_surface = pygame.Surface((150, 50))
text = font.render("Next", True, (0, 0, 0))
text_rect = text.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))

button_rect = pygame.Rect(345, 745, 150, 50)


def hover_button(button):
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, 'dark red', (1, 1, 148, 48))
    else:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)


while True:
    clock.tick(60)
    screen.fill('white')

    # Get events from the event queue
    for event in pygame.event.get():
        # Check for the quit event
        if event.type == pygame.QUIT:
            # Quit the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
                color = color_active
            else:
                active = False
                color = color_passive

        if event.type == pygame.KEYDOWN and page == 1:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                drag_choice = user_text.strip()
                df = pd.read_csv("Drug.csv",
                                 header=0,
                                 usecols=["Drug", "Information", "Effective"])
                drags = list(df.Drug.unique())
                print(str(drag_choice) in drags)
                if drag_choice in drags:
                    print("hh")
                    drag_ind = drags.index(drag_choice)
                    print(df.loc[drag_ind + 1])
                    print()
                    user_text = ''
                    print(drag_choice)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if button_rect.collidepoint(event.pos):
                screen.fill('white')
                page += 1
    if page == 0:
        font = pygame.font.SysFont("Arial", 56, 3)
        txt_welcome = font.render("Welcome to", True, 'black')
        screen.blit(txt_welcome, (130, 100))
        font1 = pygame.font.SysFont("Arial", 52, 3)
        txt_welcome1 = font1.render("MedTrack", True, 'dark red')
        screen.blit(txt_welcome1, (150, 160))
        font2 = pygame.font.SysFont("Arial", 40)
        txt_welcome2 = font2.render("This app will make your life easier!", True, 'black')
        screen.blit(txt_welcome2, (5, 240))
    if page == 1:
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, 'red', input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)
        font = pygame.font.SysFont(None, 24)
        img = font.render('search your medicine: ', True, 'red')
        screen.blit(img, (170, 130))

    hover_button(button_rect)

    button_surface.blit(text, text_rect)

    screen.blit(button_surface, (button_rect.x, button_rect.y))

    pygame.display.update()
