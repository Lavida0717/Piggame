import pygame
import random

class Enemy:
    def __init__(self, num_of_enemies):
        self.images = [pygame.image.load('enemy.png') for _ in range(num_of_enemies)]
        self.x = [random.randint(0, 736) for _ in range(num_of_enemies)]
        self.y = [random.randint(50, 150) for _ in range(num_of_enemies)]
        self.x_change = [4 for _ in range(num_of_enemies)]
        self.y_change = [40 for _ in range(num_of_enemies)]
        self.num_of_enemies = num_of_enemies

    def draw(self, screen):
        for i in range(self.num_of_enemies):
            screen.blit(self.images[i], (self.x[i], self.y[i]))

    def update_position(self, i):
        self.x[i] += self.x_change[i]
        if self.x[i] <= 0:
            self.x_change[i] = 4
            self.y[i] += self.y_change[i]
        elif self.x[i] >= 736:
            self.x_change[i] = -4
            self.y[i] += self.y_change[i]
