import random
import pygame,sys
from pygame.locals import*

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
IMAGE_WIDTH = 50
IMAGE_HEIGHT = 50

BLACK = (0,0,0)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

INTERVAL = 50

#items 
Rect = []
RandomNums = []
numfalls = 5
randx = 0
RandomSpeed = []

pygame.init()
Display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Dodge It")
Font = pygame.font.Font('freesansbold.ttf',32)

#initial position of falling items
def InitialItems():
    for num in range(numfalls):
        randx = random.randint(0,SCREEN_WIDTH -IMAGE_WIDTH)
        
        while True:
            if (randx % INTERVAL == 0 and randx not in RandomNums):
                RandomNums.append(randx)
                RandomNums.append(randx + INTERVAL)
                RandomNums.append(randx - INTERVAL)
                break;
            
            else:
                randx = random.randint(0,SCREEN_WIDTH - IMAGE_WIDTH)
                
        Rect.append(pygame.Rect(randx,0,IMAGE_WIDTH,IMAGE_HEIGHT))

#item falling
def FallingItems():
    for num in range(numfalls):
        pygame.draw.rect(Display,WHITE,Rect[num])
        yspeed = RandomSpeed[num]
        Rect[num].y = Rect[num].y + yspeed

#check if item fall out of screen
def CheckItems():
    for num in range(numfalls):
        if (Rect[num].y + IMAGE_HEIGHT >= SCREEN_HEIGHT):
            print(RandomNums,"\n ===")
            RandomNums.remove(Rect[num].x)
            RandomNums.remove(Rect[num].x + INTERVAL)
            RandomNums.remove(Rect[num].x - INTERVAL)

            Rect[num].x = random.randrange(0,SCREEN_WIDTH -IMAGE_WIDTH,IMAGE_WIDTH)
        
            while True:
                if (Rect[num].x not in RandomNums):
                    #print(Rect[num].x,"\n***")
                    RandomNums.append(Rect[num].x)
                    RandomNums.append(Rect[num].x + INTERVAL)
                    RandomNums.append(Rect[num].x - INTERVAL)
                    break;
            
                else:
                    #print(Rect[num],"\n***")
                    Rect[num].x = random.randrange(0,SCREEN_WIDTH -IMAGE_WIDTH,IMAGE_WIDTH)
                    
            Rect[num].y = 0

            #RandomNums.append(Rect[num].x)
            #RandomNums.append(Rect[num].x + INTERVAL)
            #RandomNums.append(Rect[num].x - INTERVAL)

def TheSpeed():
    thespeed = 0
    for num in range(numfalls):
        thespeed = random.randint(3,9)

        while True:
            if (thespeed not in RandomSpeed):
                RandomSpeed.append(thespeed)
                break
            else:
                thespeed = random.randint(3,9)
def main():
    #initial falling itemsS
    InitialItems()

    #determine the speed
    TheSpeed()
    #print(RandomSpeed)

    #the positions
    print(RandomNums,"\n")

    while True:

        #background color
        Display.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #items are falling    
        FallingItems()

        #check if items fall out the screen
        CheckItems()

        pygame.display.update()
        pygame.time.Clock().tick(30) #30fps

#call main
main()
