#import libraries
import pygame

#initialize pygame
pygame.init()

#game window dimensions
S_WIDTH =400
S_HIGHT=600

#create the game window
screen = pygame.display.set_mode((S_WIDTH, S_HIGHT)) #() is called a tuple, it is a data type.
pygame.display.set_caption('FALL KNIGHT')

#load images
bg_image = pygame.image.load('bg.png').convert_alpha()
char_image = pygame.image.load('very_green.png').convert_alpha()
char_rekt = pygame.Rect(0,200,70,72)
speed = 0

#player class
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale()
        self.widht=25
        self.hight=40
        self.rect = pygame.REct(0, 0, self.width, self.height)
        self.rect.center=(x, y)

guy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
#game loop
run = True
while run:
    #draw the background
    screen.blit(bg_image, (0, 0))
    screen.blit(char_image, char_rekt)
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
 #       elif event.type==pygame.KEYDOWN:
  #             speed=3
   #         if event.key == pygame.K_a:
    #            speed=-3
     #   elif event.type==pygame.KEYUP:
      #      if event.key==pygame.K_d:
       #         speed=0
        #    if event.key == pygame.K_a:
         #       speed=0
    char_rekt.x+=speed

                
    #update display window
    pygame.display.update()

pygame.quit()
