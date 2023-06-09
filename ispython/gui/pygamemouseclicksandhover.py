import pygame
pygame.init()

#Window dimensions
window_width = 1000
window_height = 800

#Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#Create the pygame window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mouse clicks and hover effects")

#Rectangle dimensions and position
rect_width = 200
rect_height = 100
rect_x = (window_width - rect_width) // 2
rect_y = (window_height - rect_height) // 2

#Create the rectangle object
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rect.collidepoint(event.pos):
                print("Rectangle Clicked!")
    return False

def draw():
    window.fill(BLACK)
    if rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(window, GREEN, rect)
    else:
        pygame.draw.rect(window, RED, rect)
    pygame.display.update()

running = True
while running:
    running = not handle_events()
    draw()

pygame.quit()