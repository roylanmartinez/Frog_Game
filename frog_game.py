import pygame
import numpy as np
pygame.init()


screenWidth = 500
win = pygame.display.set_mode([screenWidth, screenWidth])
pygame.display.set_caption("Frog Game")

# Frog
velFrog = 10
wFrog = 20
hFrog = 20
xFrog = screenWidth / 2 - wFrog
yFrog = screenWidth - hFrog

# Car Features
wCar = np.array([30, 30, 30, 40, 50])
hCar = np.array(len(wCar)*[5])
xCar = np.array([0])
yCar = screenWidth - hCar - wCar
velCars = np.array([5, 3, 2, 1, 3])

isJump = False
jumpCount = -5

run = True
passedHalf = False

while run:
    pygame.time.delay(50)

    # Close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Frog controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        xFrog -= velFrog
        if xFrog <= 0:
            xFrog = 0
    if keys[pygame.K_RIGHT]:
        xFrog += velFrog
        if screenWidth <= xFrog + wFrog:
            xFrog = screenWidth - wFrog
    if not isJump:
        if keys[pygame.K_UP]:
            yFrog -= velFrog * 0.2
            if yFrog <= 0:
                yFrog = 0
        if keys[pygame.K_DOWN]:
            yFrog += velFrog
            if screenWidth <= yFrog + hFrog:
                yFrog = screenWidth - hFrog
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        yFrog -= (jumpCount ** 2)
        if yFrog < 0:
            yFrog = 0
        jumpCount += 1
        if (jumpCount ** 2) == 0:
            isJump = False
            jumpCount = -5

    # Update black color
    win.fill([0, 0, 0])

    # Cars update
    xCar += 5
    if xCar > screenWidth:
        xCar = -wCar
    # Update the board
    pygame.draw.rect(win, [255, 0, 0], [xFrog, yFrog, wFrog, hFrog])
    pygame.draw.rect(win, [255, 255, 255], [xCar, yCar, wCar, hCar])
    pygame.display.update()
pygame.quit()
