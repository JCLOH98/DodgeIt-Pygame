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
RandomNums = []

#number of falling items
fallingnum = 6

#Level 2's random speed
RandomSpeed = []

pygame.init()
Display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Dodge It.v1.1")
Font = pygame.font.Font('Fonts/victorycomics.ttf',32)

def InitialRect():
        #fallingitems initial position
        for rect in range(fallingnum):
                randomx = random.randint(0,SCREEN_WIDTH - IMAGE_WIDTH)
                while True:
                    if (randomx % INTERVAL == 0 and randomx not in RandomNums):

                        #previous position
                        RandomNums.append(randomx)
                        #positions beside previous position
                        RandomNums.append(randomx + IMAGE_WIDTH)
                        RandomNums.append(randomx - IMAGE_WIDTH)
                        
                        break;
                    
                    else:
                        randomx = random.randint(0,SCREEN_WIDTH - IMAGE_WIDTH)

                Rect.append(pygame.Rect(randomx,0,IMAGE_WIDTH,IMAGE_HEIGHT))

def Level1():
        #draw falling items
            for draw in range(fallingnum):
                pygame.draw.rect(Display,WHITE,Rect[draw])
                yspeed = 5
                Rect[draw].y = Rect[draw].y + yspeed
def Level2():
    for num in range(fallingnum):
        pygame.draw.rect(Display,WHITE,Rect[num])
        yspeed = RandomSpeed[num]
        Rect[num].y = Rect[num].y + yspeed

def Level2ItemsCheck():
    for num in range(fallingnum):
        if (Rect[num].y + IMAGE_HEIGHT >= SCREEN_HEIGHT):
            RandomNums.remove(Rect[num].x)
            RandomNums.remove(Rect[num].x + INTERVAL)
            RandomNums.remove(Rect[num].x - INTERVAL)

            Rect[num].x = random.randrange(0,SCREEN_WIDTH -IMAGE_WIDTH,IMAGE_WIDTH)
        
            while True:
                if (Rect[num].x % INTERVAL == 0 and Rect[num].x not in RandomNums):
                    RandomNums.append(Rect[num].x)
                    RandomNums.append(Rect[num].x + INTERVAL)
                    RandomNums.append(Rect[num].x - INTERVAL)
                    break;
            
                else:
                    Rect[num].x = random.randrange(0,SCREEN_WIDTH -IMAGE_WIDTH,IMAGE_WIDTH)
                    
            Rect[num].y = 0
            
def TheSpeed():
    thespeed = 0
    for num in range(fallingnum):
        thespeed = random.randint(3,9)

        while True:
            if (thespeed not in RandomSpeed):
                RandomSpeed.append(thespeed)
                break
            else:
                thespeed = random.randint(3,9)        

def RecordScreen():        
        Display.fill(BLACK)

        TimeName = Font.render("Time(s)",True,WHITE)
        TimeNameRect = TimeName.get_rect()
        TimeNameRect.center = ((SCREEN_WIDTH/2),(TimeNameRect.height)*2)
        Display.blit(TimeName,TimeNameRect)

        LevelName = Font.render("Level(s)",True,WHITE)
        LevelNameRect = LevelName.get_rect()
        LevelNameRect.center = (SCREEN_WIDTH - TimeNameRect.width,(LevelNameRect.height)*2)
        Display.blit(LevelName,LevelNameRect)
        #Display.blit(LevelName,((SCREEN_WIDTH/2) + TimeNameRect.width,(TimeNameRect.height)*1.5))

        PlayerName = Font.render("Player Name",True,WHITE)
        PlayerNameRect = PlayerName.get_rect()
        PlayerNameRect.center = (LevelNameRect.width,(PlayerNameRect.height)*2)
        Display.blit(PlayerName,PlayerNameRect)
        #Display.blit(PlayerName,((SCREEN_WIDTH/2) - PlayerNameRect.width - TimeNameRect.width,(TimeNameRect.height)*1.5))
        
        #Read the data
        File = open('Data.dat','r')
        Read = File.read()

        #All the datas in Datas
        Datas = Read.splitlines()
        #print(Datas)

        #Show the set of datas
        SetOfData = len(Read.splitlines())
        #print(SetOfData)

        #The screen only shows 11 user data
        ScreenShowing = 11

        #Increment and decrement to next data
        NextData = 0

        NewData = []
        for i in range(SetOfData):
                #print(Datas[i].split(','))
                NewData.append((Datas[i].split(',')))

        for i in range(ScreenShowing):
                for j in range(3):
                        if (j == 0):
                                TheName = Font.render(NewData[i][j],True,GREY)
                                TheNameRect = TheName.get_rect()
                                TheNameRect.center = (LevelNameRect.width,(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                Display.blit(TheName,TheNameRect)
                                
                        elif (j == 1):
                                TheTime = Font.render(NewData[i][j],True,GREY)
                                TheTimeRect = TheTime.get_rect()
                                TheTimeRect.center = ((SCREEN_WIDTH/2),(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                Display.blit(TheTime,TheTimeRect)

                        elif (j == 2):
                                TheLevel = Font.render(NewData[i][j],True,GREY)
                                TheLevelRect = TheLevel.get_rect()
                                TheLevelRect.center = (SCREEN_WIDTH - TimeNameRect.width,(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                Display.blit(TheLevel,TheLevelRect)

        pygame.display.update()

        PreviousRun = True

        while PreviousRun:
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()

                        #mouse scroll
                        elif (event.type == MOUSEBUTTONDOWN):
                                #scroll up
                                if (event.button == 4):
                                        print("scrolling up")
                                        #if NextData = 0, do nothing
                                        if (NextData != 0):
                                            NextData -=1

                                        #clean prevois screen
                                        Display.fill(BLACK)
                                        
                                        #add record title
                                        Display.blit(PlayerName,PlayerNameRect)
                                        Display.blit(TimeName,TimeNameRect)
                                        Display.blit(LevelName,LevelNameRect)

                                        
                                        for i in range(ScreenShowing):
                                                for j in range(3):
                                                        if (j == 0):
                                                                TheName = Font.render(NewData[i+NextData][j],True,GREY)
                                                                TheNameRect = TheName.get_rect()
                                                                TheNameRect.center = (LevelNameRect.width,(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                Display.blit(TheName,TheNameRect)
                                                                
                                                        elif (j == 1):
                                                                TheTime = Font.render(NewData[i+NextData][j],True,GREY)
                                                                TheTimeRect = TheTime.get_rect()
                                                                TheTimeRect.center = ((SCREEN_WIDTH/2),(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                Display.blit(TheTime,TheTimeRect)

                                                        elif (j == 2):
                                                                TheLevel = Font.render(NewData[i+NextData][j],True,GREY)
                                                                TheLevelRect = TheLevel.get_rect()
                                                                TheLevelRect.center = (SCREEN_WIDTH - TimeNameRect.width,(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                Display.blit(TheLevel,TheLevelRect)
                                        pygame.display.update()

                                #scrolldown
                                elif (event.button == 5):
                                        print("scrolling down")
                                        #if NextData = SetOfData - ScreenShowing, which means reach the end of file, then do nothing
                                        if (NextData != (SetOfData - ScreenShowing)):
                                                NextData += 1

                                        #clean previous screen
                                        Display.fill(BLACK)
                                        
                                        #add record title
                                        Display.blit(PlayerName,PlayerNameRect)
                                        Display.blit(TimeName,TimeNameRect)
                                        Display.blit(LevelName,LevelNameRect)
                                        
                                        for i in range(ScreenShowing):
                                                for j in range(3):
                                                        if (j == 0):
                                                                TheName = Font.render(NewData[i+NextData][j],True,GREY)
                                                                TheNameRect = TheName.get_rect()
                                                                TheNameRect.center = (LevelNameRect.width,(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                Display.blit(TheName,TheNameRect)
                                                                
                                                        elif (j == 1):
                                                                TheTime = Font.render(NewData[i+NextData][j],True,GREY)
                                                                TheTimeRect = TheTime.get_rect()
                                                                TheTimeRect.center = ((SCREEN_WIDTH/2),(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                Display.blit(TheTime,TheTimeRect)

                                                        elif (j == 2):
                                                                TheLevel = Font.render(NewData[i+NextData][j],True,GREY)
                                                                TheLevelRect = TheLevel.get_rect()
                                                                TheLevelRect.center = (SCREEN_WIDTH - TimeNameRect.width,(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                Display.blit(TheLevel,TheLevelRect)
                                        pygame.display.update()
                                
                                
                        elif event.type == KEYDOWN:
                                if (event.key == K_w or event.key == K_UP):
                                        print("up")
                                        #if NextData = 0, do nothing
                                        if (NextData != 0):
                                            NextData -=1

                                        #clean prevois screen
                                        Display.fill(BLACK)
                                        
                                        #add record title
                                        Display.blit(PlayerName,PlayerNameRect)
                                        Display.blit(TimeName,TimeNameRect)
                                        Display.blit(LevelName,LevelNameRect)

                                        
                                        for i in range(ScreenShowing):
                                                for j in range(3):
                                                        if (j == 0):
                                                                TheName = Font.render(NewData[i+NextData][j],True,GREY)
                                                                TheNameRect = TheName.get_rect()
                                                                TheNameRect.center = (LevelNameRect.width,(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                Display.blit(TheName,TheNameRect)
                                                                
                                                        elif (j == 1):
                                                                TheTime = Font.render(NewData[i+NextData][j],True,GREY)
                                                                TheTimeRect = TheTime.get_rect()
                                                                TheTimeRect.center = ((SCREEN_WIDTH/2),(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                Display.blit(TheTime,TheTimeRect)

                                                        elif (j == 2):
                                                                TheLevel = Font.render(NewData[i+NextData][j],True,GREY)
                                                                TheLevelRect = TheLevel.get_rect()
                                                                TheLevelRect.center = (SCREEN_WIDTH - TimeNameRect.width,(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                Display.blit(TheLevel,TheLevelRect)
                                        pygame.display.update()

                                elif (event.key == K_s or event.key == K_DOWN):
                                        print("down")
                                        #if NextData = SetOfData - ScreenShowing, which means reach the end of file, then do nothing
                                        if (NextData != (SetOfData - ScreenShowing)):
                                                NextData += 1

                                        #clean previous screen
                                        Display.fill(BLACK)
                                        
                                        #add record title
                                        Display.blit(PlayerName,PlayerNameRect)
                                        Display.blit(TimeName,TimeNameRect)
                                        Display.blit(LevelName,LevelNameRect)
                                        
                                        for i in range(ScreenShowing):
                                                for j in range(3):
                                                        if (j == 0):
                                                                TheName = Font.render(NewData[i+NextData][j],True,GREY)
                                                                TheNameRect = TheName.get_rect()
                                                                TheNameRect.center = (LevelNameRect.width,(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                Display.blit(TheName,TheNameRect)
                                                                
                                                        elif (j == 1):
                                                                TheTime = Font.render(NewData[i+NextData][j],True,GREY)
                                                                TheTimeRect = TheTime.get_rect()
                                                                TheTimeRect.center = ((SCREEN_WIDTH/2),(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                Display.blit(TheTime,TheTimeRect)

                                                        elif (j == 2):
                                                                TheLevel = Font.render(NewData[i+NextData][j],True,GREY)
                                                                TheLevelRect = TheLevel.get_rect()
                                                                TheLevelRect.center = (SCREEN_WIDTH - TimeNameRect.width,(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                Display.blit(TheLevel,TheLevelRect)
                                        pygame.display.update()
                                        
                                elif (event.key == K_BACKSPACE):
                                        print("backspace is pressed")
                                        #close file
                                        File.close()
                                        #Clear the screen
                                        Display.fill(BLACK)
                                        pygame.display.update()
                                        PreviousRun = False
        
def StartScreen():
        Display.fill(BLACK)

        Title = Font.render("Dodge it_v1.1",True,WHITE)
        TitleRect = Title.get_rect()
        TitleRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/4)

        Coder = Font.render("by JCLOH",True,GREY)
        CoderRect = Coder.get_rect()
        CoderRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/4) + CoderRect.height)

        StartButton = Font.render("-> Start",True,GREY)
        StartRect = StartButton.get_rect()
        StartRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

        Record = Font.render("Previous Record",True,WHITE)
        RecordRect = Record.get_rect()
        RecordRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + RecordRect.height)

        Exit = Font.render("Exit",True,WHITE)
        ExitRect = Exit.get_rect()
        ExitRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + RecordRect.height + ExitRect.height)

        Condition = 1

        Start = True

        PreviousClick = (0,0,0)

        while Start:
                #print(Condition)
                if (Condition == 0 or Condition < 0):
                        Condition = 0
                        Display.fill(BLACK)
                        
                elif (Condition == 1):
                        #cover up the previous one
                        pygame.draw.rect(Display,BLUE,TitleRect)
                        pygame.draw.rect(Display,BLUE,CoderRect)
                        pygame.draw.rect(Display,BLACK,StartRect)
                        pygame.draw.rect(Display,BLACK,RecordRect)
                        pygame.draw.rect(Display,RED,ExitRect)

                        #new one
                        Display.blit(Title,TitleRect)

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
                                                #print("Enter pressed")

                                        elif (Condition == 2):
                                                #Condition = 0 to clear screen
                                                Condition = 0
                                                RecordScreen()
                                                #Condition = 1 to back to menu
                                                Condition = 1

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
                                
        
def main():
        #Level
        Level = 1
        
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

        TheSpeed()
        
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

                #show time
                TimesWidth = Font.render("Time(s):",True,GREY).get_rect().width
                Display.blit(Font.render("Time(s):",True,GREY),(SCREEN_WIDTH - TimesWidth*2,10))
                Timer = Font.render(str(TheTime),True,GREY)
                Display.blit(Timer, ((SCREEN_WIDTH - TimesWidth) + 1,10))

                #when time is 5 seconds, goes to level 2
                if(TheTime == 10):
                        Level = 2
                        
                #Level1
                if (Level == 1):
                        Level1Word = Font.render("Level 1",True,WHITE)
                        Level1WordRect = Level1Word.get_rect()
                        Level1WordRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                        Display.blit(Level1Word,Level1WordRect)
                        Level1()
                        
                        #check if the items fall out of the screen
                        #use 1 rect to check if it fall out the screen as all falling items has same speed
                        if (Rect[0].y > usery):
                                for check in range(fallingnum):
                                        #remove the previous coordinates
                                        RandomNums.remove(Rect[check].x)
                                        RandomNums.remove(Rect[check].x + INTERVAL)
                                        RandomNums.remove(Rect[check].x - INTERVAL)
                                        
                                        randomx = random.randint(0,SCREEN_WIDTH - IMAGE_WIDTH)
                                        while True:
                                                if (randomx % INTERVAL == 0 and randomx not in RandomNums):
                                                        #previous position
                                                        RandomNums.append(randomx)
                                                        #positions beside previous position
                                                        RandomNums.append(randomx + IMAGE_WIDTH)
                                                        RandomNums.append(randomx - IMAGE_WIDTH)

                                                        #Set the new x for the items
                                                        Rect[check].x = randomx

                                                        break;

                                                else:
                                                        randomx = random.randint(0,SCREEN_WIDTH - IMAGE_WIDTH)

                                        Rect[check].y = 0
                elif (Level == 2):
                        Level2Word = Font.render("Level 2",True,WHITE)
                        Level2WordRect = Level2Word.get_rect()
                        Level2WordRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                        Display.blit(Level2Word,Level2WordRect)
                        Level2()
                        Level2ItemsCheck()
                        
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

