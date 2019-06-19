import pygame
import time
import random

pygame.init()

display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("EvilDimansion")
clock=pygame.time.Clock()

heroImage = pygame.image.load("D:\\PythonSoft\\Lv-416.PythonCore\\myGame\\hero.png")
bgImage = pygame.image.load("D:\\PythonSoft\\Lv-416.PythonCore\\myGame\\StoneRoad.png")
heroImage = pygame.transform.scale(heroImage, (50,50))
hero_size=50

enemyImage = pygame.image.load("D:\\PythonSoft\\Lv-416.PythonCore\\myGame\\enemy.png")
enemyImage = pygame.transform.scale(enemyImage, (50,50))
enemy_size = 50

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(176,224,230)

def things(thingsX,thingsY,thingsW,thingsH,color):
    pygame.draw.rect(gameDisplay,color, [thingsX, thingsY,thingsW,thingsH])

def hero(x,y):
    gameDisplay.blit(heroImage,(x,y)) # Drawing our image in propriate coordinates!

def enemy(enemyX,enemyY):
    gameDisplay.blit(enemyImage,(enemyX,enemyY))
    

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def you_died():
    message_display("You died!!!")


def game_loop():
    x=(display_width*0.45)
    y=(display_height*0.45)
    enemyX=(display_width*0.1)
    enemyY=(display_height*0.1)

    deltaX=0
    deltaY=0

    # things_startX=random.randrange(0,display_width)
    # things_startY=-600
    # things_speed=7
    # thingsW=50
    # thingsH=50
    # color=black
    gameExit=False

    while not gameExit:
# create a list of events what happend. list per frame \ sec
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT:
                gameExit=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x>0:
                    deltaX=-5
                elif event.key == pygame.K_RIGHT:
                    deltaX=5
                elif event.key==pygame.K_UP:
                    deltaY=-5
                elif event.key == pygame.K_DOWN:
                    deltaY=5
#stop moving object after release the button    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    deltaX=0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    deltaY=0
        
        x+=deltaX
        y+=deltaY

#set up map border, object bouncing between end of window on x and on y axis
        if x>display_width - hero_size or x<0 :
            deltaX=-deltaX
        if y>display_height-hero_size or y<0:
            deltaY=-deltaY
            
            

        # print(x)
        # screen.blit(bgImage[0,0]) #layer*(order) of painting #1 if hero first and background white second, no car visible
        
        # things(thingsX,thingsY,thingsW,thingsH,color)
        # things(things_startX,things_startY,thingsW,thingsH,color)
        print(x)
        gameDisplay.fill(white)
        enemy(enemyX,enemyY)
        hero(x,y)              #layer(order) of painting #2

        # if x>display_width - hero_size or x<0:
        #     gameExit = True
        #     you_died()
        # if y>display_height-hero_size or y<0:
        #     gameExit = True
        #     you_died()
        pygame.display.update()#update dsiplay after getting all events
        clock.tick(60) #set up frames/sec in arg 
game_loop()
