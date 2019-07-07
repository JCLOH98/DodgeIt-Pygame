
import pygame,sys
from pygame.locals import*

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 550
IMAGE_WIDTH = 50
IMAGE_HEIGHT = 50

pygame.init()
Display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Background generator")
Font = pygame.font.Font('Fonts/victorycomics.ttf',32)


def background():
        #floor
        lastfloorend = 0
        
        floor = pygame.image.load("./Sprites/DungeonTilesII (Using)/Floors/floor_1.png")
        floorRect = floor.get_rect()
        #print("First one: ",floorRect.x + IMAGE_WIDTH)
        while(floorRect.x + IMAGE_WIDTH < SCREEN_WIDTH):
                for i in range(8):
                        floor = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Floors/" + "floor_" + str(i+1) + ".png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        floorRect = floor.get_rect()
                        floorRect.center = (((IMAGE_WIDTH/2)*(i+1))+lastfloorend,SCREEN_HEIGHT-IMAGE_HEIGHT/2)
                        Display.blit(floor,floorRect)
                lastfloorend = floorRect.x

        #wall
        #starting wall
        lastwallend = 0
        wallcondition = 0
        wall = pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_top_left.png")
        wallRect = wall.get_rect()
        while(wallRect.x + IMAGE_WIDTH < SCREEN_WIDTH):
                wallcondition += 1
                if (wallcondition == 1):
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_top_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+lastwallend,IMAGE_HEIGHT/2)
                        Display.blit(wall,wallRect)
                elif (wallcondition == 20):
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_top_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+lastwallend,IMAGE_HEIGHT/2)
                        Display.blit(wall,wallRect)
                else:
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_top_mid.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+lastwallend,IMAGE_HEIGHT/2)
                        Display.blit(wall,wallRect)
                lastwallend = wallRect.x + IMAGE_WIDTH

        #mid walls
        midwallline1end = 0
        midwallline2end = 0
        midwallline3end = 0
        midwallline4end = 0
        midwallline5end = 0
        midwallline6end = 0
        midwallline7end = 0
        midwallline8end = 0

        
        #Line1
        midwallcondition = 0
        wall = pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_top_left.png")
        wallRect = wall.get_rect()
        while(wallRect.x + IMAGE_WIDTH < SCREEN_WIDTH):
                midwallcondition += 1
                #print(midwallcondition)
                if (midwallcondition == 1):
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline1end,(IMAGE_HEIGHT/2) + IMAGE_HEIGHT)
                        Display.blit(wall,wallRect)
                elif (midwallcondition == 2):
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline1end,(IMAGE_HEIGHT/2) + IMAGE_HEIGHT)
                        Display.blit(wall,wallRect)
                elif (midwallcondition == 19):
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline1end,(IMAGE_HEIGHT/2) + IMAGE_HEIGHT)
                        Display.blit(wall,wallRect)
                elif (midwallcondition == 20):
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline1end,(IMAGE_HEIGHT/2) + IMAGE_HEIGHT)
                        Display.blit(wall,wallRect)
                #wall hole 2
                elif (midwallcondition == 16 or midwallcondition == 3):
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_hole_2.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline1end,(IMAGE_HEIGHT/2) + IMAGE_HEIGHT)
                        Display.blit(wall,wallRect)
                else:
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_mid.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline1end,(IMAGE_HEIGHT/2) + IMAGE_HEIGHT)
                        Display.blit(wall,wallRect)
                midwallline1end = wallRect.x + IMAGE_WIDTH

        #Line2
        midwallcondition = 0
        wall = pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_top_left.png")
        wallRect = wall.get_rect()
        while(wallRect.x + IMAGE_WIDTH < SCREEN_WIDTH):
                midwallcondition += 1
                #print(midwallcondition)
                if (midwallcondition == 1):
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline2end,(IMAGE_HEIGHT/2) + 2*IMAGE_HEIGHT)
                        Display.blit(wall,wallRect)
                elif (midwallcondition == 2):
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline2end,(IMAGE_HEIGHT/2) + 2*IMAGE_HEIGHT)
                        Display.blit(wall,wallRect)
                elif (midwallcondition == 19):
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline2end,(IMAGE_HEIGHT/2) + 2*IMAGE_HEIGHT)
                        Display.blit(wall,wallRect)
                elif (midwallcondition == 20):
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline2end,(IMAGE_HEIGHT/2) + 2*IMAGE_HEIGHT)
                        Display.blit(wall,wallRect)
                #wall hole 1 
                elif (midwallcondition == 8 or midwallcondition == 18):
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_hole_1.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline2end,(IMAGE_HEIGHT/2) + 2*IMAGE_HEIGHT)
                        Display.blit(wall,wallRect)
                else:
                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_mid.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                        wallRect = wall.get_rect()
                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline2end,(IMAGE_HEIGHT/2) + 2*IMAGE_HEIGHT)
                        Display.blit(wall,wallRect)
                midwallline2end = wallRect.x + IMAGE_WIDTH
        #Line 3 to 5
        midwallcondition = 0
        wall = pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_top_left.png")
        wallRect = wall.get_rect()
        for i in range(3):
                if (i == 0):
                        while(wallRect.x + IMAGE_WIDTH < SCREEN_WIDTH):
                                midwallcondition += 1
                                if (midwallcondition == 1):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 2):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 19):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 20):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 15):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_goo.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                else:
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_mid.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                        
                                midwallline3end = wallRect.x + IMAGE_WIDTH

                elif (i == 1):
                        while(wallRect.x + IMAGE_WIDTH < SCREEN_WIDTH):
                                midwallcondition += 1
                                if (midwallcondition == 1):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 2):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 19):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 20):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 4):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_goo.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                else:
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_mid.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                        
                                midwallline3end = wallRect.x + IMAGE_WIDTH

                elif (i == 2):
                        while(wallRect.x + IMAGE_WIDTH < SCREEN_WIDTH):
                                midwallcondition += 1
                                if (midwallcondition == 1):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 2):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 19):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 20):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 17 or midwallcondition == 7):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_hole_2.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                else:
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_mid.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline3end,(IMAGE_HEIGHT/2) + (i+3)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                        
                                midwallline3end = wallRect.x + IMAGE_WIDTH
                
                        
                midwallcondition = 0
                midwallline3end = 0
                wallRect.x = 0
                
        #Line6to9
        midwallcondition = 0
        wall = pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_top_left.png")
        wallRect = wall.get_rect()
        for i in range(4):
                if (i == 3):
                        while(wallRect.x + IMAGE_WIDTH < SCREEN_WIDTH):
                                midwallcondition += 1
                                #print(midwallcondition)
                                if (midwallcondition == 1):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 2):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 19):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 20):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                #goo
                                elif (midwallcondition == 15):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_goo.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                else:
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_mid.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                midwallline6end = wallRect.x + IMAGE_WIDTH
                elif (i == 1):
                        while(wallRect.x + IMAGE_WIDTH < SCREEN_WIDTH):
                                midwallcondition += 1
                                #print(midwallcondition)
                                if (midwallcondition == 1):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 2):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 19):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 20):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                #goo
                                elif (midwallcondition == 11):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_hole_2.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                else:
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_mid.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                midwallline6end = wallRect.x + IMAGE_WIDTH
                else:
                        while(wallRect.x + IMAGE_WIDTH < SCREEN_WIDTH):
                                midwallcondition += 1
                                #print(midwallcondition)
                                if (midwallcondition == 1):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 2):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_left.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 19):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                elif (midwallcondition == 20):
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_inner_corner_mid_right.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                else:
                                        wall = pygame.transform.scale(pygame.image.load("./Sprites/DungeonTilesII (Using)/Walls/wall_mid.png"),(IMAGE_WIDTH,IMAGE_HEIGHT))
                                        wallRect = wall.get_rect()
                                        wallRect.center = ((IMAGE_WIDTH/2)+midwallline6end,(IMAGE_HEIGHT/2) + (i+6)*IMAGE_HEIGHT)
                                        Display.blit(wall,wallRect)
                                midwallline6end = wallRect.x + IMAGE_WIDTH

                        
                midwallcondition = 0
                midwallline6end = 0
                wallRect.x = 0
        
        
        
def main():
    while True:
        Display.fill((255,255,255))
        background()

        for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
        pygame.display.update()
        
main()
