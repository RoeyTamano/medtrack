import pandas as pd

#
df = pd.read_csv("Drug.csv",
                 header=0,
                 usecols=["Drug", "Information", "Effective"])
drags = df.Drug.unique()
drags = list(drags)
print(drags)
drag_choice = ''
drag_ind = drags.index("Azithromycin")
print(df.loc[drag_ind + 1])
print()

# import sys module
import pygame
import sys

# pygame.init() will initialize all
# imported module
pygame.init()

clock = pygame.time.Clock()

# it will display on screen
screen = pygame.display.set_mode([600, 500])

# basic font for user typed
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
lst = []
active = False

while True:
    for event in pygame.event.get():

        # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
                color = color_active
            else:
                active = False
                color = color_passive

        if event.type == pygame.KEYDOWN:
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

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)

    pygame.display.flip()

