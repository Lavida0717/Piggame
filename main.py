import pygame
from pygame import mixer
from player import Player
from enemy import Enemy
from bullet import Bullet

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load Background and Sound
background = pygame.image.load('background.png')
mixer.music.load("background.wav")
mixer.music.play(-1)

# Create game objects
player = Player()
enemies = Enemy(num_of_enemies=6)
bullet = Bullet()

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_SPACE and bullet.state == "ready":
                bullet_sound = mixer.Sound("laser.wav")
                bullet_sound.play()
                bullet.fire(player.x)

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player.stop()

    # Update game objects
    player.update_position()
    bullet.move()

    for i in range(enemies.num_of_enemies):
        enemies.update_position(i)

    # Draw everything on the screen
    player.draw(screen)
    bullet.fire(bullet.x)
    enemies.draw(screen)

    pygame.display.update()
