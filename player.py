import pygame

class Player:
    def __init__(self):
        self.image = pygame.image.load('player.png')
        self.x = 370
        self.y = 480
        self.x_change = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.x_change = -5

    def move_right(self):
        self.x_change = 5

    def stop(self):
        self.x_change = 0

    def update_position(self):
        self.x += self.x_change
        self.x = max(0, min(self.x, 736))
