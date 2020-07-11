import pygame
import numpy as np

pygame.init()

# INITIALIZE THE GAME
screenWidth = 500
win = pygame.display.set_mode([screenWidth, screenWidth])
pygame.display.set_caption("Frog Game")
pygame.font.init()

# Text
myfont = pygame.font.SysFont('Comic Sans MS', 20)
myfont1 = pygame.font.SysFont('Comic Sans MS', 30)
scores = [0, 0]
won = False

# Someone Won
someone_won = [False, 3]

# Frog
velFrog = [5, 5]
wFrog = [24, 24]
hFrog = [24, 24]
xFrog = [375, 125]
yFrog = [screenWidth - hFrog[0], screenWidth - hFrog[1]]
isJump = [False, False]
jumpCount = [-5, -5]

# Car Features
difficulty = 1
wCar = np.array([32, 32, 64, 32, 32, 32, 64, 32, 32, 32, 32, 64, 32, 32, 32, 64, 32, 32, 32, 32, 64])
hCar = np.array(wCar.copy())
xCar = np.array([62, 124, 186, 250, 310, 372, 100, 450, 0, 262, 324, 386, 450, 110, 172, 0, 150, 100, 400, 0, 220])
yCar = np.array([80, 182, 215, 335, 30, 290, 425, 400, 130, 80, 182, 215, 335, 30, 290, 425, 400, 130, 30, 30, -10])
velCars = np.array([12, 8, 9, 11, 9, 8, 7, 11, 8, 8, 6, 6, 7, 8, 9, 10, 9, 12, 9, 10, 2]) * difficulty

# Images
image = pygame.image.load("./frog.png")
image1 = pygame.image.load("./frog1.png")
background = pygame.image.load("./background.png")
# Cars
car0 = pygame.image.load("./car0.png")
car1 = pygame.image.load("./car1.png")
car2 = pygame.image.load("./car2.png")
car3 = pygame.image.load("./car3.png")
car4 = pygame.image.load("./car4.png")
car5 = pygame.image.load("./car0.png")
car6 = pygame.image.load("./car2.png")
car7 = pygame.image.load("./car1.png")
car8 = pygame.image.load("./car3.png")
car9 = pygame.image.load("./car0.png")
car10 = pygame.image.load("./car1.png")
car11 = pygame.image.load("./car2.png")
car12 = pygame.image.load("./car3.png")
car13 = pygame.image.load("./car4.png")
car14 = pygame.image.load("./car0.png")
car15 = pygame.image.load("./car2.png")
car16 = pygame.image.load("./car1.png")
car17 = pygame.image.load("./car3.png")
car18 = pygame.image.load("./shark1.png")
car19 = pygame.image.load("./shark1.png")
car20 = pygame.image.load("./goal.png")

run = True
while run:
    # print(yFrog)
    pygame.time.delay(25)

    # Close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Frog controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        xFrog[0] -= velFrog[0] - 2
        if xFrog[0] <= 0:
            xFrog[0] = 0
    if keys[pygame.K_RIGHT]:
        xFrog[0] += velFrog[0] - 2
        if screenWidth <= xFrog[0] + wFrog[0]:
            xFrog[0] = screenWidth - wFrog[0]
    if not isJump[0]:
        if keys[pygame.K_UP]:
            yFrog[0] -= velFrog[0] - 3
            if yFrog[0] <= 0:
                yFrog[0] = 0
        if keys[pygame.K_DOWN]:
            yFrog[0] += velFrog[0] - 2
            if screenWidth <= yFrog[0] + hFrog[0]:
                yFrog[0] = screenWidth - hFrog[0]
        if keys[pygame.K_SPACE]:
            isJump[0] = True
    else:
        # If it is jumping
        yFrog[0] -= (jumpCount[0] ** 2)
        hFrog[0] += (jumpCount[0] ** 2) * 0.3
        jumpCount[0] += 1
        if yFrog[0] < 0:
            yFrog[0] = 0
        if (jumpCount[0] ** 2) == 0:
            # end jump
            hFrog[0] = 20
            isJump[0] = False
            jumpCount[0] = -5

    if keys[pygame.K_a]:
        xFrog[1] -= velFrog[1] - 2
        if xFrog[1] <= 0:
            xFrog[1] = 0
    if keys[pygame.K_d]:
        xFrog[1] += velFrog[1] - 2
        if screenWidth <= xFrog[1] + wFrog[1]:
            xFrog[1] = screenWidth - wFrog[1]
    if not isJump[1]:
        if keys[pygame.K_w]:
            yFrog[1] -= velFrog[1] - 3
            if yFrog[1] <= 0:
                yFrog[1] = 0
        if keys[pygame.K_s]:
            yFrog[1] += velFrog[1] - 2
            if screenWidth <= yFrog[1] + hFrog[1]:
                yFrog[1] = screenWidth - hFrog[1]
        if keys[pygame.K_l]:
            isJump[1] = True
    else:
        # If it is jumping
        yFrog[1] -= (jumpCount[1] ** 2)
        hFrog[1] += (jumpCount[1] ** 2) * 0.3
        jumpCount[1] += 1
        if yFrog[1] < 0:
            yFrog[1] = 0
        if (jumpCount[1] ** 2) == 0:
            # end jump
            hFrog[1] = 20
            isJump[1] = False
            jumpCount[1] = -5

    # Update background
    win.blit(background, (0, 0))

    # Cars update

    for index_car in range(len(wCar)):

        # Go left
        if index_car not in [2, 3, 4, 6, 8, 12, 17, 13, 11, 15, 20]:
            xCar[index_car] -= velCars[index_car]
            # IF COLLISION
            for i in range(2):
                if (xFrog[i] <= xCar[index_car] + 20) \
                        and (yFrog[i] <= yCar[index_car] + 20) \
                        and (yFrog[i] >= yCar[index_car] - 10) \
                        and (xFrog[i] >= xCar[index_car] - 20):
                    yFrog[i] = 500 - 24
                    xFrog[i] = 375 if not i else 125

        if xCar[index_car] + 32 + wCar[index_car] < 0 and index_car != 2 and index_car != 4:
            xCar[index_car] = screenWidth

        # GO right
        # 64 pixels
        if index_car in [2, 6, 11, 15]:
            xCar[index_car] += velCars[index_car]
            if xCar[index_car] - 64 > screenWidth:
                xCar[index_car] = 0 - 64
            # IF COLLISION
            for i in range(2):
                if (xFrog[i] <= xCar[index_car] + 60) \
                        and (yFrog[i] <= yCar[index_car] + 35) \
                        and (yFrog[i] >= yCar[index_car] + 5) \
                        and (xFrog[i] >= xCar[index_car] - 10):
                    yFrog[i] = 500 - 24
                    xFrog[i] = 375 if not i else 125
        if index_car in [3, 8, 12, 17, 4, 13]:
            xCar[index_car] += velCars[index_car]
            if xCar[index_car] - 32 > screenWidth:
                xCar[index_car] = 0 - 32

            # If collision score
            for i in range(2):
                if (xFrog[i] <= xCar[index_car] + 22) \
                        and (yFrog[i] <= yCar[index_car] + 35) \
                        and (yFrog[i] >= yCar[index_car] + 5) \
                        and (xFrog[i] >= xCar[index_car] - 10):
                    yFrog[i] = 500 - 24
                    xFrog[i] = 375 if not i else 125

        # Repeat the cars
        win.blit(eval(f"car{index_car}"), (xCar[index_car], yCar[index_car]))

    # Update the frog

    win.blit(image, (xFrog[0], yFrog[0]))
    win.blit(image1, (xFrog[1], yFrog[1]))

    # Text
    # IF COLLISION

    for i in range(2):
        if (xFrog[i] <= xCar[20] + 35) \
                and (yFrog[i] <= yCar[20] + 27) \
                and (xFrog[i] >= xCar[20] - 12):
            if i:
                scores[1] += 1
                if scores[1] == 3:
                    scores = [0, 0]
                    someone_won = [True, 'Left']
            else:
                scores[0] += 1
                if scores[0] == 3:
                    scores = [0, 0]
                    someone_won = [True, 'Right']

            yFrog[i] = 500 - 24
            xFrog[i] = 375 if not i else 125

    textsurface = myfont.render(f'Score left player: {scores[1]}', False, (0, 0, 0))
    textsurface1 = myfont.render(f'Score player right: {scores[0]}', False, (0, 0, 0))
    win.blit(textsurface, (0, 0))
    win.blit(textsurface1, (300, 0))

    if someone_won[0]:
        pygame.draw.rect(win, (255, 255, 255), [50, 50, 400, 300])
        textwon = myfont1.render(f'Player {someone_won[1]} Won!', False, (0, 0, 0))
        textwon1 = myfont1.render(f'Press Enter to start again', False, (0, 0, 0))
        win.blit(textwon, (140, 100))
        win.blit(textwon1, (70, 200))
        if keys[pygame.K_RETURN]:
            someone_won[0] = False

    # Update the game
    pygame.display.update()

pygame.quit()
