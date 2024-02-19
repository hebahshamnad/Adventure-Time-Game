        
import pygame

class enemy(object): #ENEMY CLASS
    enemyimg = pygame.image.load('assets/enemies/enemy.png') #LOADS ENEMY IMG
    enemyimg = pygame.transform.smoothscale(enemyimg, (80, 60)) #RESIZES ENEMY IMG

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
