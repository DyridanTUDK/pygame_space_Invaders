import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

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
enemyX = 370
enemyY = 50
enemyX_change = 0


#draws the player
def player(x, y):
    screen.blit(playerIMG, (x, y))

#draws the enemy
def enemy(x, y):
    screen.blit(enemyIMG, (x, y))

#Game Loop
running = True
while running:


    screen.fill((145, 169, 194))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Movement using keystrokes
        if event.type == pygame.KEYDOWN:
            print("key pressed")
            if event.key == pygame.K_LEFT:
                print("left key pressed")
                playerX_change = -0.3
            if event.key ==  pygame.K_RIGHT:
                print("right key pressed")
                playerX_change = +0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or  event.key == pygame.K_LEFT:
                print("key is released")
                playerX_change = 0
    #add movement to the player
    playerX += playerX_change
    #code for checking border
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    #creating player
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
