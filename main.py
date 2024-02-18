
import pygame
pygame.init()

win = pygame.display.set_mode((700,660))
pygame.display.set_caption("Game")

#------------------------------------
#ALL IMAGES USED IN GAME

# walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

# walkLeft=[]
# for i in range(9):
#   a=pygame.transform.flip(walkRight[i], True, False)
#   walkLeft.append(a)

# walkUp=[pygame.image.load('U1.png'), pygame.image.load('U2.png'), pygame.image.load('U3.png'), pygame.image.load('U4.png'), pygame.image.load('U5.png'), pygame.image.load('U6.png'), pygame.image.load('U7.png'), pygame.image.load('U8.png'), pygame.image.load('U9.png')]

# walkDown=[pygame.image.load('D1.png'), pygame.image.load('D2.png'), pygame.image.load('D3.png'), pygame.image.load('D4.png'), pygame.image.load('D5.png'), pygame.image.load('D6.png'), pygame.image.load('D7.png'), pygame.image.load('D8.png'), pygame.image.load('D9.png')]
walkRight = [pygame.image.load(f'move-sideways/R{i}.png') for i in range(1, 10)]
walkLeft = [pygame.transform.flip(img, True, False) for img in walkRight]

walkUp = [pygame.image.load(f'move-up/U{i}.png') for i in range(1, 10)]
walkDown = [pygame.image.load(f'move-down/D{i}.png') for i in range(1, 10)]

bg = pygame.image.load('BG1.jpg')
bg2= pygame.image.load('START.jpeg')
bg3=pygame.image.load('LEVEL2.png')
bg4=pygame.image.load('LEVEL2SCREEN.png')
bg5=pygame.image.load('GAMEWIN.jpg')
bg6=pygame.image.load('GAMEOVER.jpg')

char = pygame.image.load('FINN.png')

#---------------------------------------------

clock = pygame.time.Clock()

#---------------------------------------
#CLASSES

class player(object): #PLAYER CLASS
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 15
        self.isJump = False
        self.up=False
        self.down=False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        
        self.hitbox = (self.x + 10, self.y , 80, 125)

    def draw(self, win): #ANIMATIONS AND MOVEMENT
      if self.walkCount + 1 >= 27:
          self.walkCount = 0

      if not(self.standing):
          if self.left:
              win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
              self.walkCount += 1
          elif self.right:
              win.blit(walkRight[self.walkCount//3], (self.x,self.y))
              self.walkCount +=1
          elif self.up:
              win.blit(walkUp[self.walkCount//3], (self.x,self.y))
              self.walkCount +=1
          elif self.down:
              win.blit(walkDown[self.walkCount//3], (self.x,self.y))
              self.walkCount +=1
      else:
        win.blit(char, (self.x, self.y))
        
      self.hitbox = (self.x + 10, self.y, 80, 125)
     # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self): #WHEN FINN COLLIDES WITH ENEMY, THIS CODE WILL MAKE HIM RETURN TO HIS OG POSITION
      self.x =10
      self.y =550
      self.walkCount = 0
      pygame.display.update()


    
                
class coin(object): #COIN CLASS
  coinimg=pygame.image.load('coins.png') #LOAD COIN IMG
  coinimg= pygame.transform.smoothscale(coinimg, (50, 50)) #RESIZE COIN IMG
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.walkCount = 0
    self.speed = 1
    self.hitbox = (self.x, self.y, 50, 50)

  def draw(self, win): #COIN APPEARANCE

    if self.walkCount + 1 >= 33:
        self.walkCount = 0
    
    win.blit(self.coinimg, (self.x,self.y))
    self.walkCount += 1
    
    self.hitbox = (self.x, self.y, 50, 50)
    #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

  def hit(self): #CODE TO MAKE COIN DISAPPEAR AFTER IT IS COLLECTED
        self.x = -47474
        self.y = -38830
        self.walkCount = 0
        pygame.display.update()



class enemy(object): #ENEMY CLASS
  enemyimg = pygame.image.load('enemy.png') #LOADS ENEMY IMG
  enemyimg= pygame.transform.smoothscale(enemyimg, (80, 60)) #RESIZES ENEMY IMG

  
  def __init__(self, x, y, width, height, end):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.path = [x, end]
    self.walkCount = 0
    self.speed = 5
    
    self.hitbox = (self.x, self.y, 80, 60)

  def draw(self, win): #APPEARANCE
    self.move()
    if self.walkCount + 1 >= 33:
        self.walkCount = 0
    
    win.blit(self.enemyimg, (self.x,self.y))
    self.walkCount += 1
    
    self.hitbox = (self.x, self.y, 80, 60)
    #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

  def move(self): #MOVEMENT
   if self.speed > 0:
      if self.x + self.speed < self.path[1]:
        self.x += self.speed
      else:
        self.speed = self.speed * -1
        self.walkCount = 0
   else:
      if self.x - self.speed > self.path[0]:
        self.x += self.speed

      else:
        self.speed = self.speed * -1
        self.walkCount = 0

  def hit(self): #MAKE ENEMIES DISAPPEAR AFTER LVL 1 ENDS
    self.x =-99095
    self.y =-898875
    self.walkCount = 0
    pygame.display.update()

#--------------------------------------------------

score= pygame.font.SysFont('comicsans',40,True) 

scorecount=0 #SCORE COUNTER

def Level1GameWindow(): #FUNCTION TO DISPLAY LEVEL 1 GAME WINDOW
  
  win.blit(bg, (0,0))
  man.draw(win)

  coin1.draw(win)
  coin2.draw(win)
  coin3.draw(win)
  coin4.draw(win)
  coin5.draw(win)
  coin6.draw(win)
  coin7.draw(win)  
  coin8.draw(win)
  coin9.draw(win)
  coin10.draw(win)
  henchmen.draw(win)
  henchmen2.draw(win)
  henchmen3.draw(win)
  henchmen4.draw(win)

  finalscore= score.render((" SCORE: {0} ".format(scorecount)), True,(255, 255, 255),(0, 0, 0))
  win.blit(finalscore, (20,0)) 
  pygame.display.update()


def Level2GameWindow(): #FUNCTION TO DISPLAY LEVEL 2 GAME WINDOW
  win.blit(bg4, (0,0))
  man.draw(win)
  henchmen5.draw(win)
  henchmen6.draw(win)
  henchmen7.draw(win)
  henchmen8.draw(win)

  for i in range(len(coinlist)):
    coinlist[i].draw(win)
  
  finalscore= score.render((" SCORE: {0} ".format(scorecount)), True,(255, 255, 255),(0, 0, 0))
  win.blit(finalscore, (20,0)) 
  pygame.display.update()

#---------------------------------------------------------

#SPRITE LOCATIONS

man = player(10, 500, 64,64)
henchmen = enemy(260, 230, 64, 64, 460)
henchmen2=  enemy(590, 350, 64, 64, 610)
henchmen3 = enemy(260, 450, 64, 64, 460)
henchmen4=enemy(195, 155, 64, 64, 215)
henchmen5= enemy(330, 175, 64, 64, 460)
henchmen6= enemy(210, 270, 64, 64, 360)
henchmen7=enemy(150, 500, 64, 64, 350)
henchmen8=enemy(330, 335, 64, 64, 590)
henchmen9=enemy(210, 270, 64, 64, 360)

henchmenlist=[henchmen,henchmen2,henchmen3,henchmen4] #HENCHMEN FOR LVL 1
newhenchmenlist=[henchmen5,henchmen6,henchmen7,henchmen8] #HENCHEMEN FOR LVL2

coin1= coin(300,350)
coin2=coin(200,240)
coin3 =coin(550,460)
coin4=coin(300,570)   
coin5= coin(100,350)
coin6= coin(550,240)
coin7=coin(450,155)
coin8=coin(450,350)
coin9= coin(200,460)
coin10=coin(550,570)
coin11= coin(40,335)
coin12=coin(40,420)
coin13=coin(440,420)  
coin14=coin(140,270)
coin15=coin(240,420)
coin16=coin(340,570)
coin17=coin(275,175)
coin18=coin(590,175)
coin19=coin(590,270)
coin20=coin(590,420)
coin21=coin(295,335)
coin22= coin(440,500)
coin23=coin(170,570)
coin24=coin(570,570)

coinlist=[coin1,coin2,coin3,coin4,coin5,coin6,coin7,coin8,coin9,coin10] #COINS FOR LVL 1
newcoinlist=[coin11,coin12,coin13,coin14,coin15,coin16,coin17,coin18,coin19,coin20,coin21,coin22,coin23,coin24] #COINS FOR LVL 2

#-------------------------------------------------
#BOOL EXPRESSION FOR SCREEN TRANSTIONS

CoinCount=0 #COIN COLLECTION COUNTER
EnemyCollisionCount=0 #ENEMY COLLISION COUNTER
gamestart =True #FOR DISPLAYING GAME LOADING SCREEN
newscreen=False #FOR DISPLAYING LVL 2 LOADING SCREEN
Level2=False #FOR DISPALYING LVL 2 PLAYER SCREEN
GAMEWIN=False
GAMEOVER=False
run = True
#-----------------------------------
#BACKSTORY
print('\n\n\nFinn, a young boy from a poor family, hears that the ruler of Ooo,  Princess Bubblegum is trapped in a tower after being kidnapped by the Ice King, an evil wizard. Saving her would grant his family enough money to bring them out of poverty and lead a comfortable life. Wanting to help his family, he volunteers to rescue the princess. However, the path to the tower is rigged with traps and surrounded by the Ice King’s henchmen. Finn must now bravely fight the henchmen and avoid the traps to make it out alive! Help him save the princess!\n\nKEYS TO USE:\nUP/DOWN/LEFT/RIGHT\nSPACEBAR\nESCAPE\n\nThe left/right/up/down/ keys  are directional keys that will allow you to move your character through the game\nThe spacebar will allow you to begin the game!\nPressing the little x in the corner will allow you to quit the game')

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
    CoinCount=0
    EnemyCollisionCount=0
    henchmen.hit()
    henchmen2.hit()
    henchmen3.hit()
    henchmen4.hit()
    coinlist.clear()
    henchmenlist.clear() 
    coinlist+=newcoinlist
    henchmenlist+= newhenchmenlist
    Level2=True
    newscreen=False

  elif Level2: #LVL 2 SCREEN
    Level2GameWindow()
    pygame.display.update()
    if CoinCount==14: #IF ALL LVL 2 COINS ARE COLLECTED
      GAMEWIN=True
      run=False
    else:
      pass

    if EnemyCollisionCount>=2: #IF MORE THAN 1 COLLISION OCCURS
      GAMEOVER=True
      run=False
    else:
      pass

    

  
  else: #LEVEL 1 SCREEN
    Level1GameWindow()
    pygame.display.update()

    if CoinCount==10: #IF ALL LVL 1 COINS ARE COLLECTED
      man.hit()
      pygame.display.update()
      newscreen=True #LVL 2 LOADING SCREEN APPEARS
    else:
      pass

    if EnemyCollisionCount>=4: #IF MORE THAN 3 COLLISIONS OCCUR
      GAMEOVER=True
      run=False
    else:
      pass

  
  # FOR ENEMY COLLISIONS
  for i in range(len(henchmenlist)):
    if man.hitbox[1] < henchmenlist[i].hitbox[1] + henchmenlist[i].hitbox[3] and man.hitbox[1] + man.hitbox[3] > henchmenlist[i].hitbox[1]:
      if man.hitbox[0] + man.hitbox[2] > henchmenlist[i].hitbox[0] and man.hitbox[0] < henchmenlist[i].hitbox[0] + henchmenlist[i].hitbox[2]:
        if Level2:
          scorecount-=4 #4 POINT DEDUCTION  IN LVL 2
        else:
          scorecount-=2  #2 POINT DEDUCTION IN LVL 1

        EnemyCollisionCount+=1
        man.hit()
            
 #FOR COIN
  for i in range(len(coinlist)):
    if man.hitbox[1] < coinlist[i].hitbox[1] + coinlist[i].hitbox[3] and man.hitbox[1] + man.hitbox[3] > coinlist[i].hitbox[1]:
      if man.hitbox[0] + man.hitbox[2] > coinlist[i].hitbox[0] and man.hitbox[0] < coinlist[i].hitbox[0] + coinlist[i].hitbox[2]:
        if Level2:
          scorecount+=4   #4 POINTS ADDED  IN LVL 2
        else:
          scorecount+=2   #2 POINTS ADDED  IN LVL 1
        CoinCount+=1
        coinlist[i].hit()




  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          run = False
      
  
  keys = pygame.key.get_pressed()

  

  if keys[pygame.K_LEFT] and man.x > 2: #CODE FOR MOVING LEFT
      man.x -= man.speed
      man.left = True
      man.right = False
      man.standing = False
      man.up=False
      man.down=False

  elif keys[pygame.K_RIGHT] and man.x < 600: #CODE FOR MOVING RIGHT
      man.x += man.speed
      man.right = True
      man.left = False
      man.standing = False
      man.up=False
      man.down=False

  elif keys[pygame.K_UP] and man.y >10: #CODE FOR MOVING UP
      man.y -= man.speed
      man.right = False
      man.left = False
      man.standing = False
      man.up=True
      man.down=False
  
  elif keys[pygame.K_DOWN] and man.y <530:#CODE FOR MOVING DOWN
      man.y += man.speed
      man.right = False
      man.left = False
      man.standing = False
      man.up=False
      man.down=True

  elif keys[pygame.K_SPACE]: #SPACE BAR KEY NEEDED TO PROCEED TO LVL 1
    gamestart=False #IF GAME START = FALSE, LVL 1 PROCEEDS

    
  else: #IF NO KEY IS PRESSED, FINN WILL BE IN A STANDING POSITION
      man.standing = True
      man.walkCount = 0
      




#IF USER WINS
while GAMEWIN:
  
  win.blit(bg5, (0,0))
  score= pygame.font.Font(None, 60)
  finalscore= score.render(("FINAL SCORE: {0}".format(scorecount)), True,(255, 255, 255),(0, 0, 0))
  win.blit(finalscore, (190,520))   #DISPLAYS FINAL SCORE
  pygame.display.update()

#IF USER LOSES
while GAMEOVER:
  win.blit(bg6, (0,0))
  score= pygame.font.Font(None, 60)
  finalscore= score.render(("FINAL SCORE: {0}".format(scorecount)), True,(255, 255, 255),(0, 0, 0))
  win.blit(finalscore, (210,520)) #DISPLAYS FINAL SCORE  
  pygame.display.update()


pygame.quit()

