
import pygame

class coin(object): #COIN CLASS
    coin_frames = [pygame.image.load(f'coins/coins{i}.png') for i in range(1, 7)] # Load all coin frames
    coin_frames = [pygame.transform.smoothscale(frame, (50, 50)) for frame in coin_frames] # Resize all frames

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame_index = 0 # Index to keep track of which frame to display
        self.frame_delay = 2 # Delay between frame changes
        self.frame_count = 0 # Counter to keep track of frames
        self.speed = 0.5
        self.hitbox = pygame.Rect(self.x, self.y, 50, 50)

    def draw(self, win): #COIN APPEARANCE
        # Increment frame count
        self.frame_count += 1

        # Draw the current frame if enough frames have passed
        if self.frame_count >= self.frame_delay:
            # Draw the current frame
            win.blit(self.coin_frames[self.frame_index], (self.x, self.y))

            # Increment frame index to cycle through frames
            self.frame_index = (self.frame_index + 1) % len(self.coin_frames)

            # Reset frame count
            self.frame_count = 0

        # Update hitbox position
        self.hitbox = pygame.Rect(self.x, self.y, 50, 50)

    def hit(self): #CODE TO MAKE COIN DISAPPEAR AFTER IT IS COLLECTED
        self.x = -47474
        self.y = -38830
        pygame.display.update()
