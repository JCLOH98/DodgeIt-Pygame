import time
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

userx = SCREEN_WIDTH/2-IMAGE_WIDTH/2
usery = SCREEN_HEIGHT-IMAGE_HEIGHT*2

LEFT_CLICK = (1,0,0)
RIGHT_CLICK = (0,0,1)

#user rectangle
userRect = pygame.Rect(userx,usery,IMAGE_WIDTH,IMAGE_HEIGHT)
userspeed = 9

INTERVAL = 50

#initial xposition
randomx = 0

#random y speed
yspeed = 0

Rect = []
RandomNum = []
RandomNum2 = []

#number of falling items
fallingnum = 6

pygame.init()
Display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Dodge It.v1")
Font = pygame.font.Font('freesansbold.ttf',32)

def InitialRect():
        #fallingitems initial position
        for rect in range(fallingnum):
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

                Rect.append(pygame.Rect(randomx,0,IMAGE_WIDTH,IMAGE_HEIGHT))

def DrawFallingItems():
        #draw falling items
            for draw in range(fallingnum):
                pygame.draw.rect(Display,BLUE,Rect[draw])
                yspeed = 5
                Rect[draw].y = Rect[draw].y + yspeed

def StartScreen():
        Display.fill(GREY)
        Title = Font.render("Dodge it.v1",True,BLUE)
        TitleRect = Title.get_rect()
        TitleRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - TitleRect.height)
        Display.blit(Title,TitleRect)

        Coder = Font.render("by JCLOH",True,BLUE)
        CoderRect = Coder.get_rect()
        CoderRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2))
        Display.blit(Coder,CoderRect)

        StartButton = Font.render("Start",True,RED)
        StartRect = StartButton.get_rect()
        StartRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + CoderRect.height + StartRect.height)
        Display.blit(StartButton,StartRect)

        Start = True

        PreviousClick = (0,0,0)

        pygame.display.update()
        pygame.time.Clock().tick(30) #30fps

        while Start:
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()

                        elif event.type == KEYDOWN:
                                if (event.key == K_RETURN):
                                                Start = False

                        elif event.type == MOUSEBUTTONDOWN:
                                #left click
                                PreviousClick = pygame.mouse.get_pressed()
                                #if (pygame.mouse.get_pressed() == LEFT_CLICK):
                                        #if(pygame.mouse.get_pos()[0] > StartRect.x and\
                                           #pygame.mouse.get_pos()[0] < StartRect.x + StartRect.width and\
                                           #pygame.mouse.get_pos()[1] > StartRect.y and\
                                           #pygame.mouse.get_pos()[1] < StartRect.y + StartRect.height):
                                                #Start = False
                                                
                        elif event.type == MOUSEBUTTONUP:
                                if (PreviousClick == LEFT_CLICK):
                                        if(pygame.mouse.get_pos()[0] > StartRect.x and\
                                           pygame.mouse.get_pos()[0] < StartRect.x + StartRect.width and\
                                           pygame.mouse.get_pos()[1] > StartRect.y and\
                                           pygame.mouse.get_pos()[1] < StartRect.y + StartRect.height):
                                                Start = False
                                
        
def main():
        
        #Initial position of falling items
        InitialRect()

        #Game Loop
        running = True

        left = False
        right = False

        #THE START SCREEN LOOP
        StartScreen()
                
        #THE GAME LOOP
        while running:

                #background color
                Display.fill(GREY)

                #colorman square
                pygame.draw.rect(Display,RED,userRect)

                #draw falling items
                DrawFallingItems()

                #check if the items fall out of the screen
                #use 1 rect to check if it fall out the screen as all falling items has same speed
                if (Rect[0].y > usery):
                        RandomNum = RandomNum2 = []
                        for check in range(fallingnum):
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

                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()

                        elif event.type == pygame.KEYDOWN:

                                #left
                                if event.key == K_LEFT or event.key == K_a:
                                        left = True
                                        right = False

                                #right
                                elif event.key == K_RIGHT or event.key == K_d:
                                        right = True
                                        left = False

                if (left == True and right == False):
                        userRect.x = userRect.x - userspeed

                elif (right == True and left == False):
                        userRect.x = userRect.x + userspeed

                if (userRect.x < 0):
                        userRect.x = 0
                
                elif (userRect.x > SCREEN_WIDTH - IMAGE_WIDTH):
                        userRect.x = SCREEN_WIDTH - IMAGE_WIDTH

                #collision check
                for collision in range(fallingnum):
                        if (userRect.colliderect(Rect[collision]) == True):
                                Display.fill(GREY)
                                gameover = Font.render("GAME OVER!!!",True,BLUE)
                                gameoverRect = gameover.get_rect()
                                gameoverRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                                Display.blit(gameover,gameoverRect)
                                running = False

                pygame.display.update()
                pygame.time.Clock().tick(30) #30fps

        #wait 3 seconds
        time.sleep(3)
        #quit game
        pygame.quit()
        sys.exit()
    
main()

