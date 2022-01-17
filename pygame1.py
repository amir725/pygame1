import pygame
import time
from pygame import display
import random


pygame.init()

display_width  = 800
display_height = 600

#Colors

black  = (0,0,0)
white  = (255,255,255)
red    = (255,0,0) 

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Race Car')

clock = pygame.time.Clock()

carImg  = pygame.image.load('carImg1.png')

Car_width = 48

def stuff(stuffx,stuffy,stuffw,stuffh,color):
    pygame.draw.rect(gameDisplay,color,[stuffx,stuffy,stuffw,stuffh])

def  Car(x,y):
      
      gameDisplay.blit(carImg,(x,y))
 
def text_objects(text, font):
     textSurface = font.render(text , True , black)   
     return  textSurface, textSurface.get_rect()
          
          
def  message_display(text):
     largeText = pygame.font.Font('freesansbold.ttf', 40)
     TextSurf, TextRect = text_objects(text,largeText)
     TextRect.center = ((display_width/2),(display_height/2))
     gameDisplay.blit(TextSurf, TextRect)
     pygame.display.update()

     time.sleep(2)
     game_loop()

def  crash ():
     message_display('YOU CRASHED')    
        
 
   
def game_loop():
      x = (display_width * 0.45)
      y = (display_height * 0.8)

      x_change = 0
      
      stuff_startx = random.randrange(0,display_width)
      stuff_starty = -700
      stuff_speed = 7
      stuff_width = 100
      stuff_height = 100

      gameExit = False

      while not gameExit:
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  pygame.quit()     
                  quit()  
  
            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_LEFT:
                        x_change = -5
                  elif event.key == pygame.K_RIGHT:
                        x_change = 5
            if event.type == pygame.KEYUP:             
                  if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                     x_change = 0    
                                          
        x += x_change  
        gameDisplay.fill(white) 
          
        # stuffx,stuffy,stuffw,stuffh,color
        stuff(stuff_startx,stuff_starty,stuff_width,stuff_height,red)
        stuff_starty += stuff_speed 

        Car(x,y)
            
        if  x > display_width - Car_width or x < 0:
         crash()
         
        if stuff_starty > display_height:
            stuff_starty = 0 - stuff_height  
            stuff_startx = random.randrange(0,display_width)
            
        pygame.display.update()  
        clock.tick(60)
      
game_loop()      
pygame.quit()     
quit()  

