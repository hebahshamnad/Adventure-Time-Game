import pygame
from player import player
from coin import coin
from enemy import enemy
pygame.init()

win = pygame.display.set_mode((700,660))
pygame.display.set_caption("Adventure Time Game")

#------------------------------------
#ALL IMAGES USED IN GAME

bg = pygame.image.load('assets/bg-elements/BG1.jpg')
bg2 = pygame.image.load('assets/bg-elements/START.jpeg')
bg3 = pygame.image.load('assets/bg-elements/LEVEL2.png')
bg4 = pygame.image.load('assets/bg-elements/LEVEL2SCREEN.png')
bg5 = pygame.image.load('assets/bg-elements/GAMEWIN.jpg')
bg6 = pygame.image.load('assets/bg-elements/GAMEOVER.jpg')

scoreboard= pygame.image.load('assets/bg-elements/scoreboard.png')
heartboard=pygame.image.load('assets/bg-elements/heartboard.png')

#---------------------------------------------

clock = pygame.time.Clock()

score = pygame.font.SysFont('fixedsys', 40)
heart= pygame.font.SysFont('fixedsys', 40)
scorecount = 0 #SCORE COUNTER

def Level1GameWindow(): #FUNCTION TO DISPLAY LEVEL 1 GAME WINDOW
    win.blit(bg, (0,0))
    man.draw(win)

    for c in coinlist:
        c.draw(win)

    for h in henchmenlist:
        h.draw(win)
       
    
    
    win.blit(scoreboard, (5, 10))  # Adjust position as needed
    finalscore = score.render(("{0}".format(scorecount)), True,(0, 0, 0))
    win.blit(finalscore, (75,22))

    
    win.blit(heartboard, (255, 10))  # Adjust position as needed
    heartscore= heart.render(("{0}".format(3-EnemyCollisionCount)), True,(0, 0, 0)) 
    win.blit(heartscore,(330,22))
    pygame.display.update()


def Level2GameWindow(): #FUNCTION TO DISPLAY LEVEL 2 GAME WINDOW
    win.blit(bg4, (0,0))
    man.draw(win)

    for c in newcoinlist:
        c.draw(win)

    for h in newhenchmenlist:
        h.draw(win)

    win.blit(scoreboard, (5, 10))  # Adjust position as needed
    finalscore = score.render(("{0}".format(scorecount)), True,(0, 0, 0))
    win.blit(finalscore, (75,22))

    
    win.blit(heartboard, (255, 10))  # Adjust position as needed
    heartscore= heart.render(("{0}".format(3-EnemyCollisionCount)), True,(0, 0, 0)) 
    win.blit(heartscore,(330,22))
    pygame.display.update()

#---------------------------------------------------------

#SPRITE LOCATIONS

man = player(10, 500, 64,64)
henchmenlist = [enemy(260, 230, 64, 64, 460),
                enemy(590, 350, 64, 64, 610),
                enemy(260, 450, 64, 64, 460),
                enemy(195, 155, 64, 64, 215)]
newhenchmenlist = [enemy(330, 175, 64, 64, 460),
                   enemy(210, 270, 64, 64, 360),
                   enemy(150, 500, 64, 64, 350),
                   enemy(330, 335, 64, 64, 590),
                   enemy(210, 270, 64, 64, 360)]

coinlist = [coin(300,350), coin(200,240), coin(550,460), coin(300,570), 
            coin(100,350), coin(550,240), coin(450,155), coin(450,350), 
            coin(200,460), coin(550,570)]
newcoinlist = [coin(40,335), coin(40,420), coin(440,420), coin(140,270), 
               coin(240,420), coin(340,570), coin(275,175), coin(590,175), 
               coin(590,270), coin(590,420), coin(295,335), coin(440,500), 
               coin(170,570), coin(570,570)]

#-------------------------------------------------
#BOOL EXPRESSION FOR SCREEN TRANSTIONS

CoinCount = 0 #COIN COLLECTION COUNTER
EnemyCollisionCount = 0 #ENEMY COLLISION COUNTER
gamestart = True #FOR DISPLAYING GAME LOADING SCREEN
newscreen = False #FOR DISPLAYING LVL 2 LOADING SCREEN
Level2 = False #FOR DISPALYING LVL 2 PLAYER SCREEN
GAMEWIN = False
GAMEOVER = False
run = True
#-----------------------------------
#BACKSTORY
# print('\n\n\nFinn, a young boy from a poor family, hears that the ruler of Ooo,  Princess Bubblegum is trapped in a tower after being kidnapped by the Ice King, an evil wizard. Saving her would grant his family enough money to bring them out of poverty and lead a comfortable life. Wanting to help his family, he volunteers to rescue the princess. However, the path to the tower is rigged with traps and surrounded by the Ice King’s henchmen. Finn must now bravely fight the henchmen and avoid the traps to make it out alive! Help him save the princess!\n\nKEYS TO USE:\nUP/DOWN/LEFT/RIGHT\nSPACEBAR\nESCAPE\n\nThe left/right/up/down/ keys  are directional keys that will allow you to move your character through the game\nThe spacebar will allow you to begin the game!\nPressing the little x in the corner will allow you to quit the game')

#------------------------------------
#MAIN LOOP

while run:
    clock.tick(27)

    if gamestart: #GAME LOADING SCREEN
        win.blit(bg2,(0,0))
        info= pygame.font.Font(None, 40)
        instruction= info.render(('PRESS SPACEBAR TO CONTINUE'), True,(255, 255, 255),(0, 0, 0))
        win.blit(instruction, (150,620))
        pygame.display.update()

    elif newscreen: #LVL 2 LOADING SCREEN
        win.blit(bg3,(0,0))
        pygame.display.update()
        pygame.time.delay(3000)

        #RESET EVERYTHING BUT SCORECOUNT
        CoinCount = 0
        EnemyCollisionCount = 0
        for h in henchmenlist:
            h.hit()
        coinlist.clear()
        henchmenlist.clear() 
        coinlist += newcoinlist
        henchmenlist += newhenchmenlist
        Level2 = True
        newscreen = False

    elif Level2: #LVL 2 SCREEN
        Level2GameWindow()
        pygame.display.update()
        if CoinCount == 14: #IF ALL LVL 2 COINS ARE COLLECTED
            GAMEWIN = True
            run = False
        else:
            pass

        if EnemyCollisionCount >= 2: #IF MORE THAN 1 COLLISION OCCURS
            GAMEOVER = True
            run = False
        else:
            pass

    else: #LEVEL 1 SCREEN
        Level1GameWindow()
        pygame.display.update()

        if CoinCount == 10: #IF ALL LVL 1 COINS ARE COLLECTED
            man.hit()
            pygame.display.update()
            newscreen = True #LVL 2 LOADING SCREEN APPEARS
        else:
            pass

        if EnemyCollisionCount >= 4: #IF MORE THAN 3 COLLISIONS OCCUR
            GAMEOVER = True
            run = False
        else:
            pass

    # FOR ENEMY COLLISIONS
    for h in henchmenlist:
        if man.hitbox[1] < h.hitbox[1] + h.hitbox[3] and man.hitbox[1] + man.hitbox[3] > h.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > h.hitbox[0] and man.hitbox[0] < h.hitbox[0] + h.hitbox[2]:
                if Level2:
                    scorecount -= 4 #4 POINT DEDUCTION  IN LVL 2
                else:
                    scorecount -= 2  #2 POINT DEDUCTION IN LVL 1
                EnemyCollisionCount += 1
                man.hit()
        
    # FOR COIN
    for c in coinlist:
        if man.hitbox[1] < c.hitbox[1] + c.hitbox[3] and man.hitbox[1] + man.hitbox[3] > c.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > c.hitbox[0] and man.hitbox[0] < c.hitbox[0] + c.hitbox[2]:
                if Level2:
                    scorecount += 4   #4 POINTS ADDED  IN LVL 2
                else:
                    scorecount += 2   #2 POINTS ADDED  IN LVL 1
                CoinCount += 1
                c.hit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > 2: #CODE FOR MOVING LEFT
        man.x -= man.speed
        man.left = True
        man.right = False
        man.standing = False
        man.up = False
        man.down = False

    elif keys[pygame.K_RIGHT] and man.x < 600: #CODE FOR MOVING RIGHT
        man.x += man.speed
        man.right = True
        man.left = False
        man.standing = False
        man.up = False
        man.down = False

    elif keys[pygame.K_UP] and man.y >10: #CODE FOR MOVING UP
        man.y -= man.speed
        man.right = False
        man.left = False
        man.standing = False
        man.up = True
        man.down = False
  
    elif keys[pygame.K_DOWN] and man.y <530:#CODE FOR MOVING DOWN
        man.y += man.speed
        man.right = False
        man.left = False
        man.standing = False
        man.up = False
        man.down = True

    elif keys[pygame.K_SPACE]: #SPACE BAR KEY NEEDED TO PROCEED TO LVL 1
        gamestart = False #IF GAME START = FALSE, LVL 1 PROCEEDS

    else: #IF NO KEY IS PRESSED, FINN WILL BE IN A STANDING POSITION
        man.standing = True
        man.walkCount = 0

#IF USER WINS
while GAMEWIN:
    win.blit(bg5, (0,0))
    score = pygame.font.Font(None, 60)
    finalscore = score.render(("FINAL SCORE: {0}".format(scorecount)), True,(255, 255, 255),(0, 0, 0))
    win.blit(finalscore, (190,520))   #DISPLAYS FINAL SCORE
    pygame.display.update()

#IF USER LOSES
while GAMEOVER:
    win.blit(bg6, (0,0))
    score = pygame.font.Font(None, 60)
    finalscore = score.render(("FINAL SCORE: {0}".format(scorecount)), True,(255, 255, 255),(0, 0, 0))
    win.blit(finalscore, (190,520)) #DISPLAYS FINAL SCORE  
    pygame.display.update()

pygame.quit()
