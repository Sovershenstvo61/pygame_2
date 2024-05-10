import pygame
import sys
pygame.init()

sc=pygame.display.set_mode((600,40))
def draw():
    sc.fill((255,0,0))
    font = pygame.font.Font(None, 20)
    
    text = font.render("Hello world!", True, [0,0,0])
    sc.blit(text,(20,20))
    pygame.display.update()
draw()
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
