
import pygame

class coin(object): #COIN CLASS
    coin_frames = [pygame.image.load(f'assets/coins/coins{i}.png') for i in range(1, 7)] # Load all coin frames
    coin_frames = [pygame.transform.smoothscale(frame, (50, 50)) for frame in coin_frames] # Resize all frames

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame_index = 0 
        self.frame_count = 0
        self.hitbox = pygame.Rect(self.x, self.y, 50, 50)

    def draw(self, win): 
        self.frame_count += 1

        if self.frame_count >= 0:
            win.blit(self.coin_frames[self.frame_index], (self.x, self.y))
            self.frame_index = (self.frame_index + 1) % len(self.coin_frames)
            self.frame_count = 0
        self.hitbox = pygame.Rect(self.x, self.y, 50, 50)

    def hit(self): 
        self.x = -99999
        self.y = -99999
        pygame.display.update()
