import pygame
pygame.init()
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Python Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            runnning = False
            
screen.fill((0,0,0))

pygame.display.flip()

pygame.quit()
