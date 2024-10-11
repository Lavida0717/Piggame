import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load Background
try:
    background = pygame.image.load(r'C:\xampp\htdocs\space-adventure\background.png')
    print("Background loaded successfully!")
except Exception as e:
    print(e)

screen.fill((0, 0, 0))
screen.blit(background, (0, 0))
pygame.display.update()

# Wait for a few seconds to display the window
pygame.time.wait(5000)
pygame.quit()
