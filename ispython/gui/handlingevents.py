import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("My very first python game!")
clock = pygame.time.Clock() #Used to control the frame rate

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((255,255,255)) #Window colour white

    font = pygame.font.Font (None, 36) 
    text = font.render("Hello, welcome to Pygame!", True, (0,0,0)) #Render the text
    screen.blit(text,(320,240)) #Draw the text on the screen

    pygame.display.flip() # Updating the display

    clock.tick(60) #Limiting FPS to 60FPS

pygame.quit()
