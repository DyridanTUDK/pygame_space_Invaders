import pygame
#importing random
import random

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load("background.png")

#Title and Icon
pygame.display.set_caption("Space Invaders")
Icon = pygame.image.load("ufo.png")
pygame.display.set_icon(Icon)

#player
playerIMG = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyIMG = pygame.image.load("enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 50

#bullet
#ready = you cant see
#fire = you can see
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = -18
bullet_state = "ready"



#draws the player
def player(x, y):
    screen.blit(playerIMG, (x, y))

#draws the enemy
def enemy(x, y):
    screen.blit(enemyIMG, (x, y))

#draw the bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16 , y+10))

#Game Loop
running = True
while running:


    screen.fill((0,0,0))
    #background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Movement using keystrokes
        if event.type == pygame.KEYDOWN:
            print("key pressed")
            if event.key == pygame.K_LEFT:
                print("left key pressed")
                playerX_change = -6
            if event.key ==  pygame.K_RIGHT:
                print("right key pressed")
                playerX_change = +6
            if event.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or  event.key == pygame.K_LEFT:
                print("key is released")
                playerX_change = 0

    #enemy Movement
    #add motion to the sprite
    enemyX += enemyX_change
    #boundary check for the enemy
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    #Player movement
    #add movement to the player
    playerX += playerX_change
    #code for checking border
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY += bulletY_change


    #creating player
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
