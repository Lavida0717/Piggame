import pygame
from pygame import mixer
from player import Player
from enemy import Enemy
from bullet import Bullet

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load Background and Sound
background = pygame.image.load(r'C:\xampp\htdocs\space-adventure\background.png')
# Comment out sound for now
# mixer.music.load(r'C:\xampp\htdocs\space-adventure\background.wav')
# mixer.music.play(-1)

# Create game objects
player = Player()
enemies = Enemy(num_of_enemies=6)
bullet = Bullet()

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Function to show score
def show_score(x, y):
    score = font.render(f"Score : {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))

# Function to detect collision
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)**0.5
    return distance < 27

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

        # Collision detection
        collision = is_collision(enemies.x[i], enemies.y[i], bullet.x, bullet.y)
        if collision:
            bullet.y = 480
            bullet.state = "ready"
            score_value += 1
            enemies.x[i] = random.randint(0, 736)
            enemies.y[i] = random.randint(50, 150)
            
        enemies.draw(screen)
        
        if enemies.y[i] > 440:
            running = False

    player.draw(screen)
    if bullet.state == "fire":
        bullet.fire(bullet.x)
    
    show_score(textX, textY)
    
    pygame.display.update()
