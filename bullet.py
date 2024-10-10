import pygame

class Bullet:
    def __init__(self):
        self.image = pygame.image.load('bullet.png')
        self.x = 0
        self.y = 480
        self.y_change = 10
        self.state = "ready"

    def fire(self, x):
        self.state = "fire"
        self.x = x
        screen.blit(self.image, (self.x + 16, self.y + 10))

    def move(self):
        if self.state == "fire":
            self.y -= self.y_change
            if self.y <= 0:
                self.y = 480
                self.state = "ready"
