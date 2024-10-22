import pygame

class Character():

    def __init__(self,x,y,Panimation_list):

        #Esto fue lo que hice
        self.flip=False
        self.animation_list= Panimation_list
        self.frame_index=0
        
        self.update_time=pygame.time.get_ticks()
        ##Explicar prox clase 
        self.image=self.animation_list[self.frame_index]
        ##
        self.rect=pygame.Rect(0,0,40,40)
        self.rect.center=(x, y)

    def draw(self,superficie):
        #pygame.draw.rect(superficie, (255, 0, 0), self.rect)
        flip_image= pygame.transform.flip(self.image,self.flip,False)
        superficie.blit(flip_image,self.rect)
        
    #eXPLICAR PROXIMA CLASEEEEEEEEE
    def move(self,dx,dy):
        if dx<0:
            self.flip=True
        elif dx>0:
            self.flip=False

        self.rect.x+=dx
        self.rect.y+=dy
        print(self.rect.x,self.rect.y)

    def update(self):

        animation_cooldown= 100
        self.image= self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index +=1
            self.update_time = pygame.time.get_ticks()

        if self.frame_index>= len(self.animation_list):
            self.frame_index=0