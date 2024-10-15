import pygame
import constant
from character import Character

pygame.init()

screen= pygame.display.set_mode((constant.witdh,constant.height))

clock= pygame.time.Clock()

running= True

player=Character(40,50)

moving_right=False
moving_left = False
moving_up=False
moving_down=False

while running:
    screen.fill((0,255,0))
    #Direcciones
    dx=0
    dy=0
    if moving_right == True: 
        dx=constant.SPEED
    if moving_left == True: 
        dx=-constant.SPEED
    if moving_up == True:
        dy=-constant.SPEED
    if moving_down==True:
        dy=constant.SPEED

    player.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up=True
            if event.key == pygame.K_DOWN:
                moving_down=True
            if event.key == pygame.K_LEFT:
                moving_left=True
            if event.key == pygame.K_RIGHT:   
                moving_right=True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up=False
            if event.key == pygame.K_DOWN:
                moving_down=False
            if event.key == pygame.K_LEFT:
                moving_left=False
            if event.key == pygame.K_RIGHT:   
                moving_right=False
        

    player.move(dx,dy)

    pygame.display.update()
    clock.tick(constant.FPS)