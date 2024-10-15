import pygame

class Character():

    def __init__(self,x,y,Panimation_list):

        #Esto fue lo que hice
        self.flip=False
        self.animation_list= Panimation_list
        self.frame_index=0
        self.action=0 #No lo utilizaremos ahorita
        self.running=0 #No lo utilizaremos ahorita
        self.update_time=pygame.time.get_ticks()
        ##Explicar prox clase 
        self.image=self.animation_list[self.frame_index]
        ##
        self.rect=pygame.Rect(0,0,40,40)
        self.rect.center=(x, y)

    def draw(self,superficie):
        pygame.draw.rect(superficie, (255, 0, 0), self.rect)

    def move(self,dx,dy):
        self.rect.x+=dx
        self.rect.y+=dy
        print(self.rect.x,self.rect.y)