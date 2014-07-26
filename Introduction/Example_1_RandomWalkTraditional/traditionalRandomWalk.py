__author__ = 'Timotheus Kampik'
import sys
from random import randint
#import and init pygame
import pygame
pygame.init()

#create screen
window = pygame.display.set_mode((640, 480))

class Walker():
    #initiate and draw walker
    def __init__(self):
        self.x = int(window.get_width() / 2)
        self.y = int(window.get_height() / 2)
         #draw circle & display
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), 1, 0)
        pygame.display.flip()

    # "move" walker to random direction (right, left, up, down)
    def draw(self):
        self.step()
        #draw circle & display
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), 1, 0)
        pygame.display.flip()

    # randomly choose new direction, but prevent walker from "leaving" screen
    def step(self):
        choice = randint(0, 3)
        if 0 == choice and self.x < window.get_width():
            self.x += 1
        elif 1 == choice and self.x > 0:
            self.x -= 1
        elif 2 == choice and self.y < window.get_height():
            self.y += 1
        elif 3 == choice and self.y > 0:
            self.y -= 1


#create and init new walker object
walker = Walker()


#input handling:
while True:
   walker.draw()
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit(0)
      else:
          print(event)













