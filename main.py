import pygame
import constant
from character import Character

pygame.init()

screen= pygame.display.set_mode((constant.witdh,constant.height))

clock= pygame.time.Clock()

running= True

player=Character(40,50)

while running:

    player.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
            if event.key == pygame.K_d:
            if event.key == pygame.K_w:
            if event.key == pygame.K_s:    

    pygame.display.update()
    clock.tick(constant.FPS)