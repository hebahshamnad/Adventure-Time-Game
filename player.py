import pygame

char = pygame.image.load('FINN.png')

walkRight = [pygame.image.load(f'move-sideways/R{i}.png') for i in range(1, 10)]
walkLeft = [pygame.transform.flip(img, True, False) for img in walkRight]

walkUp = [pygame.image.load(f'move-up/U{i}.png') for i in range(1, 10)]
walkDown = [pygame.image.load(f'move-down/D{i}.png') for i in range(1, 10)]

class player(object): #PLAYER CLASS
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 15
        self.isJump = False
        self.up = False
        self.down = False
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
