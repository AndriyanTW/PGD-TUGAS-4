import pygame
from pygame import rect
from pygame.locals import *
import time

pygame.init()
screen = pygame.display.set_mode((640,240))
pygame.display.set_caption('Smooth Movement')

text = "ANDRIYAN TATAK WIGUNA"
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, (25,150,50))

rect = img.get_rect()
rect.topleft = (20,20)
cursor = Rect(rect.topright, (3, rect.height))

running = True
baground = 255,50,90

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(text)>0:
                    text = text[:-1]

            else:
                text += event.unicode
            img = font.render(text, True, (25,50,50))
            rect.size = img.get_size()
            cursor.topleft = rect.topright

    screen.fill(baground)
    screen.blit(img,rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, (25,10,50), cursor)
    pygame.display.update()

pygame.quit()