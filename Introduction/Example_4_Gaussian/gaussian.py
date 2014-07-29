__author__ = 'Timotheus Kampik'
import sys
import random
# import and init pygame
import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))

def draw():
    # get random number of gaussian distribution with mean=window_width/2 and standard deviation=60
    num = random.gauss(window.get_width()/2, 60)
    pygame.draw.circle(window, (255, 255, 255), (int(num), int(window.get_height()/2)), 10, 0)
    pygame.display.flip()

#draw continuously:
while True:
   draw()
   #handle quit event
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit(0)

