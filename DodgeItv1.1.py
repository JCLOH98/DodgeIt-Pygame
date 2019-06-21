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

pygame.display.set_caption("Dodge It.v1.1")
Font = pygame.font.Font('Fonts/victorycomics.ttf',32)

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
                pygame.draw.rect(Display,WHITE,Rect[draw])
                yspeed = 5
                Rect[draw].y = Rect[draw].y + yspeed

def RecordScreen():
        Display.fill(BLACK)

        TimeName = Font.render("Time(s)",True,WHITE)
        TimeNameRect = TimeName.get_rect()
        TimeNameRect.center = ((SCREEN_WIDTH/2),(TimeNameRect.height)*2)
        Display.blit(TimeName,TimeNameRect)

        LevelName = Font.render("Level(s)",True,WHITE)
        LevelNameRect = LevelName.get_rect()
        #LevelNameRect.center = ((SCREEN_WIDTH/2) + (TimeNameRect.width)*2,(LevelNameRect.height)*2)
        Display.blit(LevelName,((SCREEN_WIDTH/2) + TimeNameRect.width,(TimeNameRect.height)*1.5))

        PlayerName = Font.render("Player Name",True,WHITE)
        PlayerNameRect = PlayerName.get_rect()
        #PlayerNameRect.center = ((SCREEN_WIDTH/2) - (TimeNameRect.width)*2,(PlayerNameRect.height)*2)
        Display.blit(PlayerName,((SCREEN_WIDTH/2) - PlayerNameRect.width - TimeNameRect.width,(TimeNameRect.height)*1.5))

        pygame.display.update()
        
def StartScreen():
        
        Display.fill(BLACK)
        Title = Font.render("Dodge it_v1.1",True,WHITE)
        TitleRect = Title.get_rect()
        TitleRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/4)
        Display.blit(Title,TitleRect)

        Coder = Font.render("by JCLOH",True,GREY)
        CoderRect = Coder.get_rect()
        CoderRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/4) + CoderRect.height)
        Display.blit(Coder,CoderRect)

        StartButton = Font.render("-> Start",True,GREY)
        StartRect = StartButton.get_rect()
        StartRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        Display.blit(StartButton,StartRect)

        Record = Font.render("Previous Record",True,WHITE)
        RecordRect = Record.get_rect()
        RecordRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + RecordRect.height)
        Display.blit(Record,RecordRect)

        Exit = Font.render("Exit",True,WHITE)
        ExitRect = Exit.get_rect()
        ExitRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + RecordRect.height + ExitRect.height)
        Display.blit(Exit,ExitRect)

        Condition = 1

        Start = True

        PreviousClick = (0,0,0)

        pygame.display.update()
        pygame.time.Clock().tick(30) #30fps

        while Start:
                print(Condition)
                if (Condition == 0 or Condition < 0):
                        Condition = 0
                        Display.fill(BLACK)
                        
                elif (Condition == 1):
                        #cover up the previous one
                        pygame.draw.rect(Display,BLACK,StartRect)
                        pygame.draw.rect(Display,BLACK,RecordRect)
                        pygame.draw.rect(Display,RED,ExitRect)

                        #new one
                        StartButton = Font.render("-> Start",True,GREY)
                        StartRect = StartButton.get_rect()
                        StartRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                        Display.blit(StartButton,StartRect)

                        Record = Font.render("Previous Record",True,WHITE)
                        RecordRect = Record.get_rect()
                        RecordRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + RecordRect.height)
                        Display.blit(Record,RecordRect)

                        Exit = Font.render("Exit",True,WHITE)
                        ExitRect = Exit.get_rect()
                        ExitRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + RecordRect.height + ExitRect.height)
                        Display.blit(Exit,ExitRect)
                                        
                        pygame.display.update()

                elif (Condition == 2):
                        #cover up the previous one
                        pygame.draw.rect(Display,BLACK,StartRect)
                        pygame.draw.rect(Display,BLACK,RecordRect)
                        pygame.draw.rect(Display,GREEN,ExitRect)

                        #new one
                        StartButton = Font.render("Start",True,WHITE)
                        StartRect = StartButton.get_rect()
                        StartRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                        Display.blit(StartButton,StartRect)

                        Record = Font.render("-> Previous Record",True,GREY)
                        RecordRect = Record.get_rect()
                        RecordRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + RecordRect.height)
                        Display.blit(Record,RecordRect)

                        Exit = Font.render("Exit",True,WHITE)
                        ExitRect = Exit.get_rect()
                        ExitRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + RecordRect.height + ExitRect.height)
                        Display.blit(Exit,ExitRect)
                                        
                        pygame.display.update()

                elif (Condition == 3):
                        #cover up the previous one
                        pygame.draw.rect(Display,BLACK,StartRect)
                        pygame.draw.rect(Display,BLACK,RecordRect)
                        pygame.draw.rect(Display,BLUE,ExitRect)

                        #new one
                        StartButton = Font.render("Start",True,WHITE)
                        StartRect = StartButton.get_rect()
                        StartRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                        Display.blit(StartButton,StartRect)

                        Record = Font.render("Previous Record",True,WHITE)
                        RecordRect = Record.get_rect()
                        RecordRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + RecordRect.height)
                        Display.blit(Record,RecordRect)

                        Exit = Font.render("-> Exit",True,GREY)
                        ExitRect = Exit.get_rect()
                        ExitRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + RecordRect.height + ExitRect.height)
                        Display.blit(Exit,ExitRect)
                                        
                        pygame.display.update()
                                        
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()

                        elif event.type == KEYDOWN:
                                #Pressed Enter 
                                if (event.key == K_RETURN):
                                        if (Condition == 1):
                                                Start = False

                                        elif (Condition == 2):
                                                Condition = 0
                                                RecordScreen()
                                                #----------------------------------
                                                #----------------------------------
                                                #----------------------------------
                                                #THE PROBLEM IS HERE, NEED TO SHOW THE LIST
                                                #MAYBE CAN PUT THE READ FILE IN RECORDSCREEN()
                                                #----------------------------------
                                                #----------------------------------
                                                #----------------------------------

                                        elif (Condition == 3):
                                                pygame.quit()
                                                sys.exit()
                                                
                                                
                                elif (event.key == K_w or event.key == K_UP):
                                        if (Condition != 1):
                                                Condition -=1

                                elif (event.key == K_s or event.key == K_DOWN):
                                        if (Condition != 3):
                                                Condition += 1
                                        
                                elif (event.key == K_BACKSPACE):
                                                return StartScreen()

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
                                        #Pressed Start
                                        if(pygame.mouse.get_pos()[0] > StartRect.x and\
                                           pygame.mouse.get_pos()[0] < StartRect.x + StartRect.width and\
                                           pygame.mouse.get_pos()[1] > StartRect.y and\
                                           pygame.mouse.get_pos()[1] < StartRect.y + StartRect.height):
                                                Start = False

                                        #Pressed Previous Record   
                                        elif(pygame.mouse.get_pos()[0] > RecordRect.x and\
                                             pygame.mouse.get_pos()[0] < RecordRect.x + RecordRect.width and\
                                             pygame.mouse.get_pos()[1] > RecordRect.y and\
                                             pygame.mouse.get_pos()[1] < RecordRect.y + RecordRect.height):

                                                Display.fill(BLACK)

                                                TimeName = Font.render("Time(s)",True,WHITE)
                                                TimeNameRect = TimeName.get_rect()
                                                TimeNameRect.center = ((SCREEN_WIDTH/2),(TimeNameRect.height)*2)
                                                Display.blit(TimeName,TimeNameRect)

                                                LevelName = Font.render("Level(s)",True,WHITE)
                                                LevelNameRect = LevelName.get_rect()
                                                #LevelNameRect.center = ((SCREEN_WIDTH/2) + (TimeNameRect.width)*2,(LevelNameRect.height)*2)
                                                Display.blit(LevelName,((SCREEN_WIDTH/2) + TimeNameRect.width,(TimeNameRect.height)*1.5))

                                                PlayerName = Font.render("Player Name",True,WHITE)
                                                PlayerNameRect = PlayerName.get_rect()
                                                #PlayerNameRect.center = ((SCREEN_WIDTH/2) - (TimeNameRect.width)*2,(PlayerNameRect.height)*2)
                                                Display.blit(PlayerName,((SCREEN_WIDTH/2) - PlayerNameRect.width - TimeNameRect.width,(TimeNameRect.height)*1.5))

                                                pygame.display.update()
                                
        
def main():
        
        #Initial position of falling items
        InitialRect()

        #Game Loop
        running = True

        left = False
        right = False

        #THE START SCREEN LOOP
        StartScreen()

        TheTime = 0 #time counter
        Start = time.time() #current time
        
        
        #THE GAME LOOP
        while running:

                #background color
                Display.fill(BLACK)

                End = time.time()#end time

                if (int(End) - int(Start) == 1):
                        TheTime = TheTime + 1
                        Start = time.time()
                        
                #player square
                pygame.draw.rect(Display,GREY,userRect)

                #draw falling items
                DrawFallingItems()

                #show time
                TimesWidth = Font.render("Time(s):",True,GREY).get_rect().width
                Display.blit(Font.render("Time(s):",True,GREY),(SCREEN_WIDTH - TimesWidth*2,10))
                Timer = Font.render(str(TheTime),True,GREY)
                Display.blit(Timer, ((SCREEN_WIDTH - TimesWidth) + 1,10))

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
                                Display.fill(BLACK)
                                gameover = Font.render("GAME OVER!!!",True,WHITE)
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

