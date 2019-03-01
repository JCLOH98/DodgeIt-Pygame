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

#initial xposition
randomx = 0

#random y speed
yspeed = 0


itemx = 0
itemy = 0

Rect = []
RandomNum = []
RandomNum2 = []

pygame.init()
Display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

for rect in range(5):
        randomx = random.randint(0,SCREEN_WIDTH - IMAGE_WIDTH)
        while True:
            if (randomx % INTERVAL == 0 and (randomx not in RandomNum) and (randomx not in RandomNum2)):

                #previous position
                RandomNum.append(randomx)

                #positions beside previous position
                RandomNum2.append(randomx + IMAGE_WIDTH)
                RandomNum2.append(randomx - IMAGE_WIDTH)
                
                break;
            
            else:
                randomx = random.randint(0,SCREEN_WIDTH - IMAGE_WIDTH)

        Rect.append(pygame.Rect(randomx,itemy,IMAGE_WIDTH,IMAGE_HEIGHT))

while True:

    #background color
    Display.fill(GREY)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #print("Random Num:", RandomNum)
    #print("Random Num2:", RandomNum2)
    RandomNum = RandomNum2 = []
    
    for draw in range(5):
        pygame.draw.rect(Display,BLUE,Rect[draw])
        yspeed = 5
        Rect[draw].y = Rect[draw].y + yspeed

    for check in range(5):
        #fall out the screen
        if (Rect[check].y > SCREEN_HEIGHT - IMAGE_HEIGHT):
            randomx = random.randint(0,SCREEN_WIDTH - IMAGE_WIDTH)
            while True:
                if (randomx % INTERVAL == 0 and (randomx not in RandomNum) and (randomx not in RandomNum2)):

                    #previous position
                    RandomNum.append(randomx)

                    #positions beside previous position
                    RandomNum2.append(randomx + IMAGE_WIDTH)
                    RandomNum2.append(randomx - IMAGE_WIDTH)

                    #Set the new x for the items
                    Rect[check].x = randomx
                    
                    break;
                
                else:
                    randomx = random.randint(0,SCREEN_WIDTH - IMAGE_WIDTH)
                    
            Rect[check].y = 0

    
    pygame.display.update()
    pygame.time.Clock().tick(30) #30fps

    #for i in range(5):
        #print(Rect[i])
    #print("Random Num:", RandomNum)
    #print("Random Num2:", RandomNum2)

