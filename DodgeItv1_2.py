import re
import time
import random
import pygame,sys
from pygame.locals import*

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 550
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

INTERVAL = 50

pygame.init()
Display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Dodge It.v1.2")
#Font = pygame.font.Font('Fonts/victorycomics.ttf',32)
Font = pygame.font.Font('Fonts/pricedown bl.ttf',32)

#FontSmall = pygame.font.Font('Fonts/victorycomics.ttf',15)
FontSmall = pygame.font.Font('Fonts/pricedown bl.ttf',15)

#images
#background
background = pygame.image.load("./Sprites/Background.png").convert()
backgroundRect = background.get_rect()
backgroundRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

#sprites scale factor
#big zombie
#scale = (IMAGE_WIDTH*2,IMAGE_HEIGHT*2)
#masked orc 
#scale = (IMAGE_WIDTH+10,IMAGE_HEIGHT+15)
#ice zombie
scale = (IMAGE_WIDTH+10,IMAGE_HEIGHT)

#idle
#big zombie
#idle1 = pygame.image.load("./Sprites/DungeonTilesII (Using)/BigZombies/big_zombie_idle_anim_f0.png").convert_alpha()
#idle2 = pygame.image.load("./Sprites/DungeonTilesII (Using)/BigZombies/big_zombie_idle_anim_f1.png").convert_alpha()
#idle3 = pygame.image.load("./Sprites/DungeonTilesII (Using)/BigZombies/big_zombie_idle_anim_f2.png").convert_alpha()
#idle4 = pygame.image.load("./Sprites/DungeonTilesII (Using)/BigZombies/big_zombie_idle_anim_f3.png").convert_alpha()
#masked ogre
#idle1 = pygame.image.load("./Sprites/DungeonTilesII (Using)/MaskedOrcs/masked_orc_idle_anim_f0.png").convert_alpha()
#idle2 = pygame.image.load("./Sprites/DungeonTilesII (Using)/MaskedOrcs/masked_orc_idle_anim_f1.png").convert_alpha()
#idle3 = pygame.image.load("./Sprites/DungeonTilesII (Using)/MaskedOrcs/masked_orc_idle_anim_f2.png").convert_alpha()
#idle4 = pygame.image.load("./Sprites/DungeonTilesII (Using)/MaskedOrcs/masked_orc_idle_anim_f3.png").convert_alpha()
#ice zombie
idle1 = pygame.image.load("./Sprites/DungeonTilesII (Using)/IceZombies/ice_zombie_idle_anim_f0.png").convert_alpha()
idle2 = pygame.image.load("./Sprites/DungeonTilesII (Using)/IceZombies/ice_zombie_idle_anim_f1.png").convert_alpha()
idle3 = pygame.image.load("./Sprites/DungeonTilesII (Using)/IceZombies/ice_zombie_idle_anim_f2.png").convert_alpha()
idle4 = pygame.image.load("./Sprites/DungeonTilesII (Using)/IceZombies/ice_zombie_idle_anim_f3.png").convert_alpha()

#runleft
#big zombie
#runleft1 = pygame.image.load("./Sprites/DungeonTilesII (Using)/BigZombies/big_zombie_run_left_anim_f0.png").convert_alpha()
#runleft2 = pygame.image.load("./Sprites/DungeonTilesII (Using)/BigZombies/big_zombie_run_left_anim_f1.png").convert_alpha()
#runleft3 = pygame.image.load("./Sprites/DungeonTilesII (Using)/BigZombies/big_zombie_run_left_anim_f2.png").convert_alpha()
#runleft4 = pygame.image.load("./Sprites/DungeonTilesII (Using)/BigZombies/big_zombie_run_left_anim_f3.png").convert_alpha()
#masked ogre
#runleft1 = pygame.image.load("./Sprites/DungeonTilesII (Using)/MaskedOrcs/masked_orc_run_left_anim_f0.png").convert_alpha()
#runleft2 = pygame.image.load("./Sprites/DungeonTilesII (Using)/MaskedOrcs/masked_orc_run_left_anim_f1.png").convert_alpha()
#runleft3 = pygame.image.load("./Sprites/DungeonTilesII (Using)/MaskedOrcs/masked_orc_run_left_anim_f2.png").convert_alpha()
#runleft4 = pygame.image.load("./Sprites/DungeonTilesII (Using)/MaskedOrcs/masked_orc_run_left_anim_f3.png").convert_alpha()
#ice zombie
runleft1 = pygame.image.load("./Sprites/DungeonTilesII (Using)/IceZombies/ice_zombie_run_left_anim_f0.png").convert_alpha()
runleft2 = pygame.image.load("./Sprites/DungeonTilesII (Using)/IceZombies/ice_zombie_run_left_anim_f1.png").convert_alpha()
runleft3 = pygame.image.load("./Sprites/DungeonTilesII (Using)/IceZombies/ice_zombie_run_left_anim_f2.png").convert_alpha()
runleft4 = pygame.image.load("./Sprites/DungeonTilesII (Using)/IceZombies/ice_zombie_run_left_anim_f3.png").convert_alpha()

#runright
#big zombie
#runright1 = pygame.image.load("./Sprites/DungeonTilesII (Using)/BigZombies/big_zombie_run_right_anim_f0.png").convert_alpha()
#runright2 = pygame.image.load("./Sprites/DungeonTilesII (Using)/BigZombies/big_zombie_run_right_anim_f1.png").convert_alpha()
#runright3 = pygame.image.load("./Sprites/DungeonTilesII (Using)/BigZombies/big_zombie_run_right_anim_f2.png").convert_alpha()
#runright4 = pygame.image.load("./Sprites/DungeonTilesII (Using)/BigZombies/big_zombie_run_right_anim_f3.png").convert_alpha()
#masked ogre
#runright1 = pygame.image.load("./Sprites/DungeonTilesII (Using)/MaskedOrcs/masked_orc_run_right_anim_f0.png").convert_alpha()
#runright2 = pygame.image.load("./Sprites/DungeonTilesII (Using)/MaskedOrcs/masked_orc_run_right_anim_f1.png").convert_alpha()
#runright3 = pygame.image.load("./Sprites/DungeonTilesII (Using)/MaskedOrcs/masked_orc_run_right_anim_f2.png").convert_alpha()
#runright4 = pygame.image.load("./Sprites/DungeonTilesII (Using)/MaskedOrcs/masked_orc_run_right_anim_f3.png").convert_alpha()
#ice zombie
runright1 = pygame.image.load("./Sprites/DungeonTilesII (Using)/IceZombies/ice_zombie_run_right_anim_f0.png").convert_alpha()
runright2 = pygame.image.load("./Sprites/DungeonTilesII (Using)/IceZombies/ice_zombie_run_right_anim_f1.png").convert_alpha()
runright3 = pygame.image.load("./Sprites/DungeonTilesII (Using)/IceZombies/ice_zombie_run_right_anim_f2.png").convert_alpha()
runright4 = pygame.image.load("./Sprites/DungeonTilesII (Using)/IceZombies/ice_zombie_run_right_anim_f3.png").convert_alpha()

#chests
chest1 = pygame.image.load("./Sprites/DungeonTilesII (Using)/Chests/chest_mimic_open_anim_f0.png").convert_alpha()
chest2 = pygame.image.load("./Sprites/DungeonTilesII (Using)/Chests/chest_mimic_open_anim_f1.png").convert_alpha()
chest3 = pygame.image.load("./Sprites/DungeonTilesII (Using)/Chests/chest_mimic_open_anim_f2.png").convert_alpha()
chest4 = pygame.image.load("./Sprites/DungeonTilesII (Using)/Chests/chest_mimic_open_anim_f3.png").convert_alpha()
chestscale =(IMAGE_WIDTH,IMAGE_HEIGHT)

#logo
Logo = pygame.transform.scale(pygame.image.load("./Sprites/Logo_Transparent.png").convert_alpha(),(32,32))
pygame.display.set_icon(Logo)


def Background():
        #Display.fill(BLACK)
        Display.blit(background,backgroundRect)

def InitialRect(fallingnum,RandomNums,Rect,randomx):
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
                #print(Rect)

def Level1(frame,fallingnum,Rect):
        #draw falling items
        for draw in range(fallingnum):
                #pygame.draw.rect(Display,WHITE,Rect[draw],3)
                yspeed = 5
                Rect[draw].y = Rect[draw].y + yspeed
                if (frame <= 3 or (frame > 12 and frame <= 15)):
                        chest = pygame.transform.scale(chest1,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[draw].center
                        Display.blit(chest,chestRect)
                elif (frame <= 6 or (frame > 15 and frame <= 18)):
                        chest = pygame.transform.scale(chest2,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[draw].center
                        Display.blit(chest,chestRect)
                elif (frame <= 9 or (frame > 18 and frame <= 21)):
                        chest = pygame.transform.scale(chest3,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[draw].center
                        Display.blit(chest,chestRect)
                elif (frame <= 12 or frame > 21):
                        chest = pygame.transform.scale(chest4,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[draw].center
                        Display.blit(chest,chestRect)

def Level2(frame,fallingnum,Rect,RandomSpeed):
        for num in range(fallingnum):
                #pygame.draw.rect(Display,WHITE,Rect[num],3)
                yspeed = RandomSpeed[num]
                Rect[num].y = Rect[num].y + yspeed
        
                if (frame <= 3 or (frame > 12 and frame <= 15)):
                        chest = pygame.transform.scale(chest1,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[num].center
                        Display.blit(chest,chestRect)
                elif (frame <= 6 or (frame > 15 and frame <= 18)):
                        chest = pygame.transform.scale(chest2,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[num].center
                        Display.blit(chest,chestRect)
                elif (frame <= 9 or (frame > 18 and frame <= 21)):
                        chest = pygame.transform.scale(chest3,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[num].center
                        Display.blit(chest,chestRect)
                elif (frame <= 12 or frame > 21):
                        chest = pygame.transform.scale(chest4,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[num].center
                        Display.blit(chest,chestRect)

def Level3(frame,fallingnum,Rect):
        for draw in range(fallingnum):
                #pygame.draw.rect(Display,WHITE,Rect[draw],3)
                yspeed = 5
                Rect[draw].y = Rect[draw].y + yspeed + 4
                if (frame <= 3 or (frame > 12 and frame <= 15)):
                        chest = pygame.transform.scale(chest1,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[draw].center
                        Display.blit(chest,chestRect)
                elif (frame <= 6 or (frame > 15 and frame <= 18)):
                        chest = pygame.transform.scale(chest2,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[draw].center
                        Display.blit(chest,chestRect)
                elif (frame <= 9 or (frame > 18 and frame <= 21)):
                        chest = pygame.transform.scale(chest3,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[draw].center
                        Display.blit(chest,chestRect)
                elif (frame <= 12 or frame > 21):
                        chest = pygame.transform.scale(chest4,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[draw].center
                        Display.blit(chest,chestRect)

def Level4(frame,fallingnum,Rect,RandomSpeed):
        for num in range(fallingnum):
                #pygame.draw.rect(Display,WHITE,Rect[num],3)
                yspeed = RandomSpeed[num]
                Rect[num].y = Rect[num].y + yspeed + 5
        
                if (frame <= 3 or (frame > 12 and frame <= 15)):
                        chest = pygame.transform.scale(chest1,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[num].center
                        Display.blit(chest,chestRect)
                elif (frame <= 6 or (frame > 15 and frame <= 18)):
                        chest = pygame.transform.scale(chest2,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[num].center
                        Display.blit(chest,chestRect)
                elif (frame <= 9 or (frame > 18 and frame <= 21)):
                        chest = pygame.transform.scale(chest3,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[num].center
                        Display.blit(chest,chestRect)
                elif (frame <= 12 or frame > 21):
                        chest = pygame.transform.scale(chest4,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[num].center
                        Display.blit(chest,chestRect)

def Level5(frame,fallingnum,Rect):
        for draw in range(fallingnum):
                #pygame.draw.rect(Display,WHITE,Rect[draw],3)
                yspeed = 5
                Rect[draw].y = Rect[draw].y + yspeed + 5
                if (frame <= 3 or (frame > 12 and frame <= 15)):
                        chest = pygame.transform.scale(chest1,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[draw].center
                        Display.blit(chest,chestRect)
                elif (frame <= 6 or (frame > 15 and frame <= 18)):
                        chest = pygame.transform.scale(chest2,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[draw].center
                        Display.blit(chest,chestRect)
                elif (frame <= 9 or (frame > 18 and frame <= 21)):
                        chest = pygame.transform.scale(chest3,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[draw].center
                        Display.blit(chest,chestRect)
                elif (frame <= 12 or frame > 21):
                        chest = pygame.transform.scale(chest4,chestscale)
                        chestRect = chest.get_rect()
                        chestRect.center = Rect[draw].center
                        Display.blit(chest,chestRect)

def LevelItemsCheck(fallingnum,Rect,RandomNums):
    for num in range(fallingnum):
        if (Rect[num].y + IMAGE_HEIGHT >= SCREEN_HEIGHT - IMAGE_HEIGHT/2):
            RandomNums.remove(Rect[num].x)
            RandomNums.remove(Rect[num].x + INTERVAL)
            RandomNums.remove(Rect[num].x - INTERVAL)

            Rect[num].x = random.randint(0,SCREEN_WIDTH - IMAGE_WIDTH)
        
            while True:
                if (Rect[num].x % INTERVAL == 0 and Rect[num].x not in RandomNums):
                    RandomNums.append(Rect[num].x)
                    RandomNums.append(Rect[num].x + INTERVAL)
                    RandomNums.append(Rect[num].x - INTERVAL)
                    break;
            
                else:
                    Rect[num].x = random.randint(0,SCREEN_WIDTH - IMAGE_WIDTH)
                    
            Rect[num].y = 0
            
def TheSpeed(fallingnum,RandomSpeed):
    thespeed = 0
    for num in range(fallingnum):
        thespeed = random.randint(4,9)

        while True:
            if (thespeed not in RandomSpeed):
                RandomSpeed.append(thespeed)
                break
            else:
                thespeed = random.randint(3,9)        

def RecordScreen():        
        Display.fill(BLACK)

        LevelName = Font.render("Level(s)",True,WHITE)
        LevelNameRect = LevelName.get_rect()
        LevelNameRect.center = ((SCREEN_WIDTH) - (SCREEN_WIDTH/4) - (SCREEN_WIDTH/10),(LevelNameRect.height)*2)
        Display.blit(LevelName,LevelNameRect)
        #Display.blit(LevelName,((SCREEN_WIDTH/2) + TimeNameRect.width,(TimeNameRect.height)*1.5))

        TimeName = Font.render("Time(s)",True,WHITE)
        TimeNameRect = TimeName.get_rect()
        TimeNameRect.center = (SCREEN_WIDTH - LevelNameRect.width,(TimeNameRect.height)*2)
        Display.blit(TimeName,TimeNameRect)

        PlayerName = Font.render("Player Name",True,WHITE)
        PlayerNameRect = PlayerName.get_rect()
        PlayerNameRect.center = (TimeNameRect.width*2,(PlayerNameRect.height)*2)
        Display.blit(PlayerName,PlayerNameRect)
        #Display.blit(PlayerName,((SCREEN_WIDTH/2) - PlayerNameRect.width - TimeNameRect.width,(TimeNameRect.height)*1.5))

        
        Escape = FontSmall.render("Press \'backspace\' to go back to main menu",True,WHITE)
        EscapeRect = Escape.get_rect()
        EscapeRect.center = (SCREEN_WIDTH - EscapeRect.width/2 - 20,SCREEN_HEIGHT - EscapeRect.height*2)
        Display.blit(Escape,EscapeRect)
        
        #Read the data
        try:
                File = open('Data.dat','r')
                Read = File.read()
                #print(File)
                #print("trying")
        except:
                File = open('Data.dat','w')
                File.close()
                File = open('Data.dat','r')
                Read = File.read()
                #print("catch some error")
        else:
                File = open('Data.dat','r')
                Read = File.read()
                #print("success")
                
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
        if (ScreenShowing > SetOfData):
                for i in range (SetOfData):
                        for j in range(3):
                                if (j == 0):
                                        TheName = Font.render(NewData[i][j],True,GREY)
                                        TheNameRect = TheName.get_rect()
                                        TheNameRect.center = (PlayerNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                        Display.blit(TheName,TheNameRect)
                                        
                                elif (j == 1):
                                        TheLevel = Font.render(NewData[i][j],True,GREY)
                                        TheLevelRect = TheLevel.get_rect()
                                        TheLevelRect.center = (LevelNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                        Display.blit(TheLevel,TheLevelRect)

                                elif (j == 2):
                                        TheTime = Font.render(NewData[i][j],True,GREY)
                                        TheTimeRect = TheTime.get_rect()
                                        TheTimeRect.center = (TimeNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                        Display.blit(TheTime,TheTimeRect)
                                        
                        
        else:
                for i in range(ScreenShowing):
                        for j in range(3):
                                if (j == 0):
                                        TheName = Font.render(NewData[i][j],True,GREY)
                                        TheNameRect = TheName.get_rect()
                                        TheNameRect.center = (PlayerNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                        Display.blit(TheName,TheNameRect)
                                        
                                elif (j == 1):
                                        TheLevel = Font.render(NewData[i][j],True,GREY)
                                        TheLevelRect = TheLevel.get_rect()
                                        TheLevelRect.center = (LevelNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                        Display.blit(TheLevel,TheLevelRect)

                                elif (j == 2):
                                        TheTime = Font.render(NewData[i][j],True,GREY)
                                        TheTimeRect = TheTime.get_rect()
                                        TheTimeRect.center = (TimeNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                        Display.blit(TheTime,TheTimeRect)

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
                                        #print("scrolling up")
                                        #if NextData = 0, do nothing
                                        if (NextData != 0):
                                            NextData -=1

                                        #clean prevois screen
                                        Display.fill(BLACK)
                                        
                                        #add record title
                                        Display.blit(PlayerName,PlayerNameRect)
                                        Display.blit(TimeName,TimeNameRect)
                                        Display.blit(LevelName,LevelNameRect)

                                        if (ScreenShowing < SetOfData):
                                                for i in range(ScreenShowing):
                                                        for j in range(3):
                                                                if (j == 0):
                                                                        TheName = Font.render(NewData[i+NextData][j],True,GREY)
                                                                        TheNameRect = TheName.get_rect()
                                                                        TheNameRect.center = (PlayerNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                        Display.blit(TheName,TheNameRect)
                                                                        
                                                                elif (j == 1):
                                                                        TheLevel = Font.render(NewData[i+NextData][j],True,GREY)
                                                                        TheLevelRect = TheLevel.get_rect()
                                                                        TheLevelRect.center = (LevelNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                        Display.blit(TheLevel,TheLevelRect)

                                                                elif (j == 2):
                                                                        TheTime = Font.render(NewData[i+NextData][j],True,GREY)
                                                                        TheTimeRect = TheTime.get_rect()
                                                                        TheTimeRect.center = (TimeNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                        Display.blit(TheTime,TheTimeRect)
                                                Display.blit(Escape,EscapeRect)
                                                pygame.display.update()

                                #scrolldown
                                elif (event.button == 5):
                                        #print("scrolling down")
                                        #if NextData = SetOfData - ScreenShowing, which means reach the end of file, then do nothing
                                        if (NextData != (SetOfData - ScreenShowing)):
                                                NextData += 1

                                        #clean previous screen
                                        Display.fill(BLACK)
                                        
                                        #add record title
                                        Display.blit(PlayerName,PlayerNameRect)
                                        Display.blit(TimeName,TimeNameRect)
                                        Display.blit(LevelName,LevelNameRect)

                                        if (ScreenShowing < SetOfData):
                                                for i in range(ScreenShowing):
                                                        for j in range(3):
                                                                if (j == 0):
                                                                        TheName = Font.render(NewData[i+NextData][j],True,GREY)
                                                                        TheNameRect = TheName.get_rect()
                                                                        TheNameRect.center = (PlayerNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                        Display.blit(TheName,TheNameRect)
                                                                        
                                                                elif (j == 1):
                                                                        TheLevel = Font.render(NewData[i+NextData][j],True,GREY)
                                                                        TheLevelRect = TheLevel.get_rect()
                                                                        TheLevelRect.center = (LevelNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                        Display.blit(TheLevel,TheLevelRect)

                                                                elif (j == 2):
                                                                        TheTime = Font.render(NewData[i+NextData][j],True,GREY)
                                                                        TheTimeRect = TheTime.get_rect()
                                                                        TheTimeRect.center = (TimeNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                        Display.blit(TheTime,TheTimeRect)

                                                Display.blit(Escape,EscapeRect)
                                                pygame.display.update()
                                
                                
                        elif event.type == KEYDOWN:
                                if (event.key == K_w or event.key == K_UP):
                                        #print("up")
                                        #if NextData = 0, do nothing
                                        if (NextData != 0):
                                            NextData -=1

                                        #clean prevois screen
                                        Display.fill(BLACK)
                                        
                                        #add record title
                                        Display.blit(PlayerName,PlayerNameRect)
                                        Display.blit(TimeName,TimeNameRect)
                                        Display.blit(LevelName,LevelNameRect)

                                        if (ScreenShowing < SetOfData):
                                                for i in range(ScreenShowing):
                                                        for j in range(3):
                                                                if (j == 0):
                                                                        TheName = Font.render(NewData[i+NextData][j],True,GREY)
                                                                        TheNameRect = TheName.get_rect()
                                                                        TheNameRect.center = (PlayerNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                        Display.blit(TheName,TheNameRect)
                                                                        
                                                                elif (j == 1):
                                                                        TheLevel = Font.render(NewData[i+NextData][j],True,GREY)
                                                                        TheLevelRect = TheLevel.get_rect()
                                                                        TheLevelRect.center = (LevelNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                        Display.blit(TheLevel,TheLevelRect)

                                                                elif (j == 2):
                                                                        TheTime = Font.render(NewData[i+NextData][j],True,GREY)
                                                                        TheTimeRect = TheTime.get_rect()
                                                                        TheTimeRect.center = (TimeNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                        Display.blit(TheTime,TheTimeRect)

                                                Display.blit(Escape,EscapeRect)
                                                pygame.display.update()

                                elif (event.key == K_s or event.key == K_DOWN):
                                        #print("down")
                                        #if NextData = SetOfData - ScreenShowing, which means reach the end of file, then do nothing
                                        if (NextData != (SetOfData - ScreenShowing)):
                                                NextData += 1

                                        #clean previous screen
                                        Display.fill(BLACK)
                                        
                                        #add record title
                                        Display.blit(PlayerName,PlayerNameRect)
                                        Display.blit(TimeName,TimeNameRect)
                                        Display.blit(LevelName,LevelNameRect)

                                        if (ScreenShowing < SetOfData):
                                                for i in range(ScreenShowing):
                                                        for j in range(3):
                                                                if (j == 0):
                                                                        TheName = Font.render(NewData[i+NextData][j],True,GREY)
                                                                        TheNameRect = TheName.get_rect()
                                                                        TheNameRect.center = (PlayerNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                        Display.blit(TheName,TheNameRect)
                                                                        
                                                                elif (j == 1):
                                                                        TheLevel = Font.render(NewData[i+NextData][j],True,GREY)
                                                                        TheLevelRect = TheLevel.get_rect()
                                                                        TheLevelRect.center = (LevelNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                        Display.blit(TheLevel,TheLevelRect)

                                                                elif (j == 2):
                                                                        TheTime = Font.render(NewData[i+NextData][j],True,GREY)
                                                                        TheTimeRect = TheTime.get_rect()
                                                                        TheTimeRect.center = (TimeNameRect.center[0],(PlayerNameRect.height*2) + ((i+1)*PlayerNameRect.height))
                                                                        Display.blit(TheTime,TheTimeRect)

                                                Display.blit(Escape,EscapeRect)
                                                pygame.display.update()
                                        
                                elif (event.key == K_BACKSPACE):
                                        #print("backspace is pressed")
                                        #close file
                                        File.close()
                                        #Clear the screen
                                        Display.fill(BLACK)
                                        pygame.display.update()
                                        PreviousRun = False
        
def StartScreen():
        
        Display.fill(BLACK)

        Title = Font.render("Dodge it_v1.2",True,WHITE)
        TitleRect = Title.get_rect()
        TitleRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/4)

        LogoRect = Logo.get_rect();
        LogoRect.center = (TitleRect.center[0] - TitleRect.width/2 - LogoRect.width/2 ,TitleRect.center[1])

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

        
        pygame.mixer.music.load('./Musics/Prologue.mp3')
        pygame.mixer.music.play(-1,0.0)
        
        while Start:
                #print(Condition)
                #if (Condition == 0 or Condition < 0):
                        #Condition = 0
                        #Display.fill(BLACK)
                        
                if (Condition == 1):
                        #cover up the previous one
                        pygame.draw.rect(Display,BLACK,TitleRect)
                        pygame.draw.rect(Display,BLACK,LogoRect)
                        pygame.draw.rect(Display,BLACK,CoderRect)
                        pygame.draw.rect(Display,BLACK,StartRect)
                        pygame.draw.rect(Display,BLACK,RecordRect)
                        pygame.draw.rect(Display,BLACK,ExitRect)

                        #new one
                        Display.blit(Title,TitleRect)
                        
                        Display.blit(Logo,LogoRect)

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
                        pygame.draw.rect(Display,BLACK,ExitRect)

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
                        pygame.draw.rect(Display,BLACK,ExitRect)

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
        
                

def main(replay):
        pygame.mixer.init()
        
        #user rectangle
        userRect = pygame.Rect(userx,usery,IMAGE_WIDTH,IMAGE_HEIGHT)
        userspeed = 9

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
        
        #use to check the FPS
        FPS = 0;
        realtimeFPS = 0
        FPScal = 0
        previousFPS = 0
        
        #Level
        Level = 1
        
        #Initial position of falling items
        InitialRect(fallingnum,RandomNums,Rect,randomx)

        #Game Loop
        running = True

        left = False
        right = False

        #THE START SCREEN LOOP
        if replay == 0:
                StartScreen()

        TheTime = 0 #time counter
        Start = time.time() #current time

        #random falling speed
        TheSpeed(fallingnum,RandomSpeed)

        #level condition
        level2condition = 0
        level3condition = 0
        level4condition = 0
        level5condition = 0

        pygame.mixer.music.stop()
        #THE GAME LOOP
        pygame.mixer.music.load('./Musics/Chibi Ninja.mp3')
        pygame.mixer.music.play(-1,0.0)
        while running:
                FPS += 1

                #background color
                #Display.fill(BLACK)
                Background()
                        

                End = time.time()#end time

                if (int(End) - int(Start) == 1):
                        TheTime = TheTime + 1
                        Start = time.time()
                        #To check the FPS
                        #print("Avg FPS: ", FPS/TheTime)
                        #print("RealTimeFPS:", (FPS - previousFPS)/(TheTime - FPScal),"\n")
                        previousFPS = FPS
                        FPScal += 1
                        
                        
                #player square
                #Robot = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII/big_zombie_idle_anim_f0.png"),(IMAGE_WIDTH*2,IMAGE_HEIGHT*2))#pygame.image.load("./Sprites/robotfree/png/Idle (1).png")
                #RobotRect = Robot.get_rect()
                #RobotRect.center = userRect.center
                #Display.blit(Robot,(RobotRect.x,RobotRect.y))
                #pygame.draw.rect(Display,GREY,userRect,3)
                #-------------------------------------------
                #-------------------------------------------
                #-------------------------------------------
                #-------------------------------------------
                #-------------------------------------------
                #-------------------------------------------
                #WORK ON THE PLAYER SPRITES HERE
                #-------------------------------------------
                #-------------------------------------------
                #-------------------------------------------
                #-------------------------------------------
                #-------------------------------------------
                #-------------------------------------------

                #show time
                TimesWidth = Font.render("Time(s):",True,WHITE).get_rect().width
                Display.blit(Font.render("Time(s):",True,WHITE),(SCREEN_WIDTH - TimesWidth*2,0))
                Timer = Font.render(str(TheTime),True,WHITE)
                Display.blit(Timer, ((SCREEN_WIDTH - TimesWidth) + 1,0))
                
                #when time is 10 seconds, goes to level 2
                if(TheTime == 10):
                        if (level2condition == 0):
                                userspeed += 1
                                level2condition = 1
                        Level = 2
                elif(TheTime == 25):
                        if (level3condition == 0):
                                userspeed += 1
                                level3condition = 1
                        Level = 3
                elif(TheTime == 40):
                        Level = 4
                elif (TheTime == 60):
                        if (level5condition == 0):
                                fallingnum += 1
                                RandomNums = []
                                Rect = []
                                userspeed += 1
                                InitialRect(fallingnum,RandomNums,Rect,randomx)
                                level5condition = 1
                        Level = 5
                        
                        
                #Level1
                if (Level == 1):
                        Level1Word = Font.render("Level 1",True,WHITE)
                        Level1WordRect = Level1Word.get_rect()
                        Level1WordRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                        Display.blit(Level1Word,Level1WordRect)
                        Level1((FPS - previousFPS),fallingnum,Rect)
                        LevelItemsCheck(fallingnum,Rect,RandomNums)
                        
                elif (Level == 2):
                        Level2Word = Font.render("Level 2",True,WHITE)
                        Level2WordRect = Level2Word.get_rect()
                        Level2WordRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                        Display.blit(Level2Word,Level2WordRect)
                        Level2((FPS - previousFPS),fallingnum,Rect,RandomSpeed)
                        LevelItemsCheck(fallingnum,Rect,RandomNums)
                        
                elif (Level == 3):
                        Level3Word = Font.render("Level 3",True,WHITE)
                        Level3WordRect = Level3Word.get_rect()
                        Level3WordRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                        Display.blit(Level3Word,Level3WordRect)
                        Level3((FPS - previousFPS),fallingnum,Rect)
                        LevelItemsCheck(fallingnum,Rect,RandomNums)

                elif (Level == 4):
                        Level4Word = Font.render("Level 4",True,WHITE)
                        Level4WordRect = Level4Word.get_rect()
                        Level4WordRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                        Display.blit(Level4Word,Level3WordRect)
                        Level4((FPS - previousFPS),fallingnum,Rect,RandomSpeed)
                        LevelItemsCheck(fallingnum,Rect,RandomNums)

                elif (Level == 5):
                        Level5Word = Font.render("Level 5",True,WHITE)
                        Level5WordRect = Level5Word.get_rect()
                        Level5WordRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                        Display.blit(Level5Word,Level3WordRect)
                        Level5((FPS - previousFPS),fallingnum,Rect)
                        LevelItemsCheck(fallingnum,Rect,RandomNums)
                        
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

                if (left == False and right == False):
                        if ( (FPS - previousFPS) <= 3 or ( (FPS - previousFPS) > 12 and (FPS - previousFPS) <= 15)):
                                Robot = pygame.transform.scale(idle1,scale)
                                RobotRect = Robot.get_rect()
                                RobotRect.center = userRect.center
                                Display.blit(Robot,RobotRect)
                                #pygame.draw.rect(Display,GREY,userRect,3)

                        elif ( (FPS - previousFPS) <= 6 or ( (FPS - previousFPS) > 15 and (FPS - previousFPS) <= 18)):
                                Robot = pygame.transform.scale(idle2,scale)
                                RobotRect = Robot.get_rect()
                                RobotRect.center = userRect.center
                                Display.blit(Robot,RobotRect)
                                #pygame.draw.rect(Display,GREY,userRect,3)

                        elif ( (FPS - previousFPS) <= 9 or ( (FPS - previousFPS) > 18 and (FPS - previousFPS) <= 21)):
                                Robot = pygame.transform.scale(idle3,scale)
                                RobotRect = Robot.get_rect()
                                RobotRect.center = userRect.center
                                Display.blit(Robot,RobotRect)
                                #pygame.draw.rect(Display,GREY,userRect,3)

                        elif ( (FPS - previousFPS) <= 12 or (FPS - previousFPS) > 21):
                                Robot = pygame.transform.scale(idle4,scale)
                                RobotRect = Robot.get_rect()
                                RobotRect.center = userRect.center
                                Display.blit(Robot,RobotRect)
                                #pygame.draw.rect(Display,GREY,userRect,3)

                elif (left == True and right == False):
                        if ( (FPS - previousFPS) <= 3 or ( (FPS - previousFPS) > 12 and (FPS - previousFPS) <= 15)):
                                Robot = pygame.transform.scale(runleft1,scale)
                                RobotRect = Robot.get_rect()
                                RobotRect.center = userRect.center
                                Display.blit(Robot,RobotRect)
                                #pygame.draw.rect(Display,GREY,userRect,3)

                        elif ( (FPS - previousFPS) <= 6 or ( (FPS - previousFPS) > 15 and (FPS - previousFPS) <= 18)):
                                Robot = pygame.transform.scale(runleft2,scale)
                                RobotRect = Robot.get_rect()
                                RobotRect.center = userRect.center
                                Display.blit(Robot,RobotRect)
                                #pygame.draw.rect(Display,GREY,userRect,3)

                        elif ( (FPS - previousFPS) <= 9 or ( (FPS - previousFPS) > 18 and (FPS - previousFPS) <= 21)):
                                Robot = pygame.transform.scale(runleft3,scale)
                                RobotRect = Robot.get_rect()
                                RobotRect.center = userRect.center
                                Display.blit(Robot,RobotRect)
                                #pygame.draw.rect(Display,GREY,userRect,3)

                        elif ( (FPS - previousFPS) <= 12 or (FPS - previousFPS) > 21):
                                Robot = pygame.transform.scale(runleft4,scale)
                                RobotRect = Robot.get_rect()
                                RobotRect.center = userRect.center
                                Display.blit(Robot,RobotRect)
                                #pygame.draw.rect(Display,GREY,userRect,3)

                        userRect.x = userRect.x - userspeed
                                

                elif (right == True and left == False):                        
                        if ( (FPS - previousFPS) <= 3 or ( (FPS - previousFPS) > 12 and (FPS - previousFPS) <= 15)):
                                Robot = pygame.transform.scale(runright1,scale)
                                RobotRect = Robot.get_rect()
                                RobotRect.center = userRect.center
                                Display.blit(Robot,RobotRect)
                                #pygame.draw.rect(Display,GREY,userRect,3)

                        elif ( (FPS - previousFPS) <= 6 or ( (FPS - previousFPS) > 15 and (FPS - previousFPS) <= 18)):
                                Robot = pygame.transform.scale(runright2,scale)
                                RobotRect = Robot.get_rect()
                                RobotRect.center = userRect.center
                                Display.blit(Robot,RobotRect)
                                #pygame.draw.rect(Display,GREY,userRect,3)

                        elif ( (FPS - previousFPS) <= 9 or ( (FPS - previousFPS) > 18 and (FPS - previousFPS) <= 21)):
                                Robot = pygame.transform.scale(runright3,scale)
                                RobotRect = Robot.get_rect()
                                RobotRect.center = userRect.center
                                Display.blit(Robot,RobotRect)
                                #pygame.draw.rect(Display,GREY,userRect,3)

                        elif ( (FPS - previousFPS) <= 12 or (FPS - previousFPS) > 21):
                                Robot = pygame.transform.scale(runright4,scale)
                                RobotRect = Robot.get_rect()
                                RobotRect.center = userRect.center
                                Display.blit(Robot,RobotRect)
                                #pygame.draw.rect(Display,GREY,userRect,3)
                        
                        userRect.x = userRect.x + userspeed

                if (userRect.x < 0):
                        userRect.x = 0
                
                elif (userRect.x > SCREEN_WIDTH - IMAGE_WIDTH):
                        userRect.x = SCREEN_WIDTH - IMAGE_WIDTH

                #collision check
                for collision in range(fallingnum):
                        if (userRect.colliderect(Rect[collision]) == True):
                                running = False

                pygame.display.update()
                pygame.time.Clock().tick(30) #30fps
        
        #Game ending
        Ending = True
        RecordName = []
        MaxChar = 0
        
        pygame.mixer.music.stop()
        #Clear the game over screen
        Display.fill(BLACK)

        gameover = Font.render("GAME OVER!!!",True,WHITE)
        gameoverRect = gameover.get_rect()
        gameoverRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - gameoverRect.height*2)
        Display.blit(gameover,gameoverRect)

        LogoRect = Logo.get_rect()
        LogoRect.center = (gameoverRect.center[0] - gameoverRect.width/2 - LogoRect.width/2,gameoverRect.center[1])
        Display.blit(Logo,LogoRect)

        #Please Enter your name
        EnterName = Font.render("Please Enter your name (Max 20 characters)",True,WHITE)
        EnterNameRect = EnterName.get_rect()
        EnterNameRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - EnterNameRect.height)
        Display.blit(EnterName,EnterNameRect)
        
        Exit = FontSmall.render("Press \'/\' to replay",True,WHITE)
        ExitRect = Exit.get_rect()
        ExitRect.center = (SCREEN_WIDTH - ExitRect.width/2 - 20,SCREEN_HEIGHT - ExitRect.height*2)
        Display.blit(Exit,ExitRect)

        pygame.mixer.music.load('./Musics/Jumpshot.mp3')
        pygame.mixer.music.play(-1,0.0)

        while Ending:
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()

                        elif event.type == pygame.KEYDOWN:
                                #print("Entering name")
                                #print("event ket: ",event.key)
                                if event.key == K_BACKSPACE:
                                        #print("backspace")
                                        #print(RecordName)
                                        
                                        if (RecordName == [] and MaxChar != 0):
                                                pygame.draw.rect(Display,BLACK,TheNameRect)
                                                
                                        if (RecordName != []):
                                                MaxChar -= 1
                                                #remove the last element of the name
                                                del(RecordName[-1])
                                                #print(RecordName)
                                                Name = "".join(RecordName)
                                                #print(Name)
                                                pygame.draw.rect(Display,BLACK,TheNameRect)
                                                TheName = Font.render(Name,True,GREY)
                                                TheNameRect = TheName.get_rect()
                                                TheNameRect.center = (EnterNameRect.center[0], EnterNameRect.center[1] + TheNameRect.height)
                                                Display.blit(TheName,TheNameRect)
                                                
                                        
                                
                                        
                                elif event.key == K_RETURN:
                                        #print("enter")
                                        if (RecordName != []):
                                                File = open('Data.dat','a')
                                                File.write(Name)
                                                File.write(",")
                                                File.write(str(Level))
                                                File.write(",")
                                                File.write(str(TheTime))
                                                File.write("\n")
                                                File.close()
                                                pygame.quit()
                                                sys.exit()
                                        else:
                                                pygame.quit()
                                                sys.exit()
                                        
                                elif event.key in range(256):
                                        if re.search("[a-z]",chr(event.key)) or (chr(event.key) in ['1','2','3','4','5','6','7','8','9','0']) or event.key == K_SPACE:
                                                MaxChar += 1

                                                if MaxChar <= 20:
                                                        RecordName.append(chr(event.key))
                                                        #print("RecordName")
                                                        Name = "".join(RecordName)
                                                        #print(Name)
                                                        TheName = Font.render(Name,True,GREY)
                                                        TheNameRect = TheName.get_rect()
                                                        TheNameRect.center = (EnterNameRect.center[0], EnterNameRect.center[1] + TheNameRect.height)
                                                        pygame.draw.rect(Display,BLACK,TheNameRect)
                                                        Display.blit(TheName,TheNameRect)
                                                else:
                                                        MaxChar = 20

                                        elif chr(event.key) == "/":
                                                #print("/ is pressed for replay, tempo setting")
                                                pygame.mixer.music.stop()
                                                return main(1)
                                        
                pygame.display.update()
                
    
main(0)

