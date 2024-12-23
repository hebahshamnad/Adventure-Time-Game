        
import pygame

class enemy(object): #ENEMY CLASS
    enemyimg = pygame.image.load('assets/enemies/enemy.png') 
    enemyimg = pygame.transform.smoothscale(enemyimg, (80, 60)) 

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.speed = 5
        
        self.hitbox = (self.x, self.y, 80, 60)

    def draw(self, win): 
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        win.blit(self.enemyimg, (self.x,self.y))
        self.walkCount += 1
        
        self.hitbox = (self.x, self.y, 80, 60)

    def move(self): 
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

    def hit(self): 
        self.x =-99999
        self.y =-99999
        self.walkCount = 0
        pygame.display.update()
