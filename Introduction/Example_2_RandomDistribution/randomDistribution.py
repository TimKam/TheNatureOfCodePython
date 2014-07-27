__author__ = 'Timotheus Kampik'
import sys
from random import randint
from optparse import OptionParser
# import and init pygame
import pygame

pygame.init()

#option parser, get maximum of distribution
parser = OptionParser()
parser.add_option("--rangeMax", type="int", dest="rangeMax",
                  help="Set maximum of distinct distribution. Minimum is 0.")
(options, args) = parser.parse_args()
rangeMax = options.rangeMax
# +1 as array contains 0, ..., rangeMax, so rangeMax + 1 elements:
range = options.rangeMax + 1
print("distribution ranges from 0 to " + str(options.rangeMax))

#create screen
window = pygame.display.set_mode((640, 480))

# create distribution array
distArray = [0] * (range)

#determine width of each rectangle. cast to int -> no gaps, but the distribution will not fill the whole screen
width = (int) (window.get_width() / range)

# increase random integer in array and draw new distribution
def draw():
    choice = randint(0, rangeMax)
    distArray[choice] += 1
    count = 0
    for i in distArray:
        pygame.draw.rect(window, (255, 255, 255), (0 + count*width, window.get_height() - i, width, i))
        pygame.display.flip()
        count += 1
        print(str(i));


#input handling:
while True:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        else:
            print(event)
