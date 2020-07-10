import pygame
import numpy as np
pygame.init()


screenWidth = 500
win = pygame.display.set_mode([screenWidth, screenWidth])
pygame.display.set_caption("Frog Game")

# Frog
velFrog = 5
wFrog = 20
hFrog = 20
xFrog = screenWidth / 2 - wFrog
yFrog = screenWidth - hFrog
isJump = False
jumpCount = -5

# Car Features
wCar = np.array([30, 30, 30, 40, 50])
hCar = np.array(len(wCar)*[10])
xCar = np.array([0, 100, 200, 300, 500])
yCar = np.array([80, 150, 200, 310, 420])
velCars = np.array([5, 3, 2, 1, 3])

# Images
image = pygame.image.load("./frog.png")
background = pygame.image.load("./background.png")
# image = pygame.transform.scale(image, (100, 100))


run = True
while run:
    # print(yFrog)
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
        # If it is jumping
        yFrog -= (jumpCount ** 2)
        hFrog += (jumpCount ** 2) * 0.3
        jumpCount += 1
        if yFrog < 0:
            yFrog = 0
        if (jumpCount ** 2) == 0:
            # end jump
            hFrog = 20
            isJump = False
            jumpCount = -5

    # Update background
    win.blit(background, (0, 0))

    # Cars update
    for index_car in range(len(wCar)):
        xCar[index_car] -= 5
        if xCar[index_car] + wCar[index_car] < 0:
            xCar[index_car] = screenWidth
        pygame.draw.rect(win, [255, 255, 255], [xCar[index_car], yCar[index_car], wCar[index_car], hCar[index_car]])

    # Update the frog
    win.blit(image, (xFrog, yFrog))

    # Update the game
    pygame.display.update()

pygame.quit()
