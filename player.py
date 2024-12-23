import pygame

char = pygame.image.load('assets/FINN.png')

walkRight = [pygame.image.load(f'assets/move-sideways/R{i}.png') for i in range(1, 10)]
walkLeft = [pygame.transform.flip(img, True, False) for img in walkRight]
walkUp = [pygame.image.load(f'assets/move-up/U{i}.png') for i in range(1, 10)]
walkDown = [pygame.image.load(f'assets/move-down/D{i}.png') for i in range(1, 10)]

heartbreak = pygame.image.load('assets/bg-elements/loss.png')  
hit_bg= pygame.image.load('assets/bg-elements/HIT.jpg')

class player(object): #PLAYER CLASS
    HITBOX_OFFSET_X = 10
    HITBOX_WIDTH = 80
    HITBOX_HEIGHT = 125
    DEFAULT_X = 10
    DEFAULT_Y = 550
    WALK_COUNT_RESET = 27
    HEARTBREAK_Y_OFFSET = 50
    HIT_ANIMATION_FRAMES = 30
    HIT_ANIMATION_DELAY = 40

    def __init__(self, x, y, width, height):
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
        
        self.update_hitbox()

    def update_hitbox(self):
        self.hitbox = (self.x + self.HITBOX_OFFSET_X, self.y, self.HITBOX_WIDTH, self.HITBOX_HEIGHT)

    def draw(self, win): 
        if self.walkCount + 1 >= self.WALK_COUNT_RESET:
            self.walkCount = 0

        if not self.standing:
            direction = None
            if self.left:
                direction = walkLeft
            elif self.right:
                direction = walkRight
            elif self.up:
                direction = walkUp
            elif self.down:
                direction = walkDown
            
            if direction:
                win.blit(direction[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))
        
        self.update_hitbox()

    def default_position(self):
        self.x = self.DEFAULT_X
        self.y = self.DEFAULT_Y
        self.update_hitbox()

    def hit(self, win): 
        self.default_position()
        self.walkCount = 0
        
        heartbreak_y = self.y - self.HEARTBREAK_Y_OFFSET  
        
        for _ in range(self.HIT_ANIMATION_FRAMES):  
            win.blit(hit_bg, (0, 0))  
            win.blit(char, (self.x, self.y))  
            win.blit(heartbreak, (self.x + 20, heartbreak_y))  
            pygame.display.update()  
            heartbreak_y -= 1 
            pygame.time.delay(self.HIT_ANIMATION_DELAY)  
