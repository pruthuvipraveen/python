import pygame
from pygame.locals import*

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width,height))

class Button:
    def __init__(self,text,position):
        self.text = text
        self.position = position
        self.font = pygame.font.Font(None, 32)
        self.rect = pygame.Rect (position,(200,50))
        self.is_hovered = False

    def draw(self, surface):
        color = (255,0,0) if self.is_hovered else (0,255,0)
        pygame.draw.rect (surface, color, self.rect)
        text_surface = self.font.render(self.text, True, (255,255,255))
        text_rect = text_surface.get_rect(center = self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event (self,event):
        if event.type == MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint (event.pos)
        elif event.type == MOUSEBUTTONDOWN:
            if self.is_hovered:
                print (f"Button {self.text} clicked!")


button1 = Button("Button 1", (100,100))
button2 = Button("Button 2", (100,200))
buttons = [button1,button2]

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        for button in buttons:
            button.handle_event(event)

    screen.fill((0,0,0))
    for button in buttons:
        button.draw(screen)
    pygame.display.update()

pygame.quit()
