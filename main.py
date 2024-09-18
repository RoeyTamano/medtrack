import pygame
import sys

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# Create a Pygame window
window_size = (500, 800)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pygame Clickable Button')

board = [[0 for i in range(50)] for j in range(25)]

for i in board:
    print(i)

font = pygame.font.Font(None, 24)
button_surface = pygame.Surface((150, 50))
text = font.render("Next", True, (0, 0, 0))
text_rect = text.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))

button_rect = pygame.Rect(345, 745, 150, 50)

def hover_button(button):
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
    else:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)


while True:
    clock.tick(60)
    screen.fill((155, 255, 155))

    # Get events from the event queue
    for event in pygame.event.get():
        # Check for the quit event
        if event.type == pygame.QUIT:
            # Quit the game
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if button_rect.collidepoint(event.pos):
                print("Button clicked!")


    hover_button(button_rect)

    button_surface.blit(text, text_rect)

    screen.blit(button_surface, (button_rect.x, button_rect.y))

    pygame.display.update()
