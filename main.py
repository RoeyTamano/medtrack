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

board = [[0 for i in range(50)] for j in range(25)]

for i in board:
    print(i)
page1 = True
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

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if button_rect.collidepoint(event.pos):
                screen.fill('white')
                page1 = False
    if page1:
        font = pygame.font.SysFont("Arial", 56, 3)
        txt_welcome = font.render("Welcome to", True, 'black')
        screen.blit(txt_welcome, (130, 100))
        font1 = pygame.font.SysFont("Arial", 52, 3)
        txt_welcome1 = font1.render("MedTrack", True, 'dark red')
        screen.blit(txt_welcome1, (150, 160))
        font2 = pygame.font.SysFont("Arial", 40)
        txt_welcome2 = font2.render("This app will make your life easier!", True, 'black')
        screen.blit(txt_welcome2, (5, 240))

    hover_button(button_rect)

    button_surface.blit(text, text_rect)

    screen.blit(button_surface, (button_rect.x, button_rect.y))

    pygame.display.update()
