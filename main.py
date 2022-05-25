from enum import auto
import pygame
import graphics
from random import randint
from controls import *
from texts import *

pygame.init()

WIDTH, HEIGHT = 900, 600

S_WIDTH = 10
TOP_MARGE = 130
SIDE_MARGE = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (105, 105, 105)


M_TITLE = H0.render("SNAKE", True, WHITE)
M_TITLE_RECT = M_TITLE.get_rect()
M_TITLE_RECT.center = (WIDTH // 2, (HEIGHT // 2) - 20)

G_TITLE = H1.render("SNAKE", True, WHITE)
G_TITLE_RECT = G_TITLE.get_rect()
G_TITLE_RECT.center = (WIDTH // 2, TOP_MARGE // 2)

G_POINTS = H2.render("POINTS : ", True, WHITE)
G_POINTS_RECT = G_POINTS.get_rect()
G_POINTS_RECT.center = ((WIDTH // 2) + (G_TITLE_RECT.width // 2) + (G_POINTS_RECT.width // 2) + 10, TOP_MARGE // 2 + 15)

WIN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

SPEEDS = [30, 25, 20, 15, 10, 5, 4, 3, 2, 1]

def moveSnake(snake, xVel, yVel):
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = [j for j in snake[i - 1]]
    
    snake[0][0] += S_WIDTH * xVel
    snake[0][1] += S_WIDTH * yVel

    if(snake[0][0] < SIDE_MARGE):
        snake[0][0] = WIDTH - SIDE_MARGE - S_WIDTH
    elif(snake[0][1] < TOP_MARGE):
        snake[0][1] = HEIGHT - SIDE_MARGE - S_WIDTH
    elif(snake[0][0] == WIDTH - SIDE_MARGE):
        snake[0][0] = SIDE_MARGE
    elif(snake[0][1] == HEIGHT - SIDE_MARGE):
        snake[0][1] = TOP_MARGE

def setBait(bait, snake):
    bait[0] = randint(SIDE_MARGE / 10, ((WIDTH - SIDE_MARGE) / 10) - 1) * 10
    bait[1] = randint(TOP_MARGE / 10, ((HEIGHT - SIDE_MARGE) / 10) - 1) * 10

    while(bait in snake[:-1]):
        bait[0] = randint(SIDE_MARGE / 10, (WIDTH - SIDE_MARGE) / 10) * 10
        bait[1] = randint(TOP_MARGE / 10, (HEIGHT - SIDE_MARGE) / 10) * 10

def isAlive(snake):
    if(snake[0] in snake[1 : -2]):
        return 3
    return 2

def menuToGame():
    y = M_TITLE_RECT.center[1]
    x = M_TITLE_RECT.center[0]
    tarY = G_TITLE_RECT.center[1]
    currSize = M_TITLE.get_size()[1]
    tarSize = G_TITLE.get_size()[1]

    ch = (currSize - tarSize) / (y - tarY)

    while(y > tarY):
        clock.tick(170)
        WIN.fill(BLACK)
        tempFont = pygame.font.Font('freesansbold.ttf', int(currSize))
        tempTitle = tempFont.render("SNAKE", True, WHITE)
        tempTitleRect = tempTitle.get_rect()
        tempTitleRect.center = (x, y)
        WIN.blit(tempTitle, tempTitleRect)

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return 0
            if(event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN):
                return 2

        pygame.display.update()
        y -= 1
        currSize -= ch
    return 2

def closeTrans():
    pos = []

    for i in range(int(HEIGHT / 10)):
        pos.append([0, WIDTH])

    run = 7

    while(run):
        clock.tick(10)
        graphics.drawRects(WIN, pos, WIDTH, 10, WHITE)

        run = 0

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return 0
        
        for i in range(len(pos)):
            if(pos[i][0] < pos[i][1]):
                run = 7
                pos[i][0] += randint(1, 3) * 10
                pos[i][1] -= randint(1, 3) * 10


        pygame.display.update()

    return 2

def openTrans(points, bait, bigBait, snake, pauseB):
    pos = []

    for i in range(int(HEIGHT / 10)):
        pos.append([int(WIDTH / 2), int(WIDTH / 2)])

    run = 7

    while(run):
        clock.tick(10)

        graphics.drawUI(WIN, str(points), G_TITLE, G_TITLE_RECT, G_POINTS, G_POINTS_RECT)
        graphics.drawBorder(WIN, SIDE_MARGE, TOP_MARGE, WIDTH, HEIGHT)
        graphics.drawBait(WIN, bait, S_WIDTH, bigBait)
        graphics.drawSnake(WIN, snake, S_WIDTH)
        pauseB.show()
        graphics.drawRects(WIN, pos, WIDTH, 10, WHITE)

        run = 0

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return 0
        
        for i in range(len(pos)):
            if(pos[i][0] > 0):
                run = 7
                pos[i][0] -= randint(1, 3) * 10
            if(pos[i][1] < WIDTH):
                eun = 7
                pos[i][1] += randint(1, 3) * 10


        pygame.display.update()

    return 2

def pauseMenu(pButton):
    run = 5

    while(run == 5):
        pButton.show()

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = 0

        pButton.update()

        if(pButton.clicked()):
            run = 2

        pygame.display.update()

    return run

def game(diff, autoInr):
    run = 2
    points = 0
    snake = [[450, 350], [440, 350], [430, 350], [420, 350]]
    bait = [0, 0]
    setBait(bait, snake)
    xVel = 1
    yVel = 0
    ticks = 0
    pauseB = pauseButton(WIN, [WHITE, BLACK], [50, 50, 50, 50])
    turn = False
    bigBait = False
    if(not autoInr):
        diff = SPEEDS[diff - 1]
    else:
        diff = 10

    run = closeTrans()

    run = openTrans(points, bait, bigBait, snake, pauseB)



    while(run == 2):
        clock.tick(160)

        graphics.drawUI(WIN, str(points), G_TITLE, G_TITLE_RECT, G_POINTS, G_POINTS_RECT)
        graphics.drawBorder(WIN, SIDE_MARGE, TOP_MARGE, WIDTH, HEIGHT)
        graphics.drawBait(WIN, bait, S_WIDTH, bigBait)
        graphics.drawSnake(WIN, snake, S_WIDTH)
        pauseB.show()
        
        pygame.display.update()

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return [0, points]
            if(event.type == pygame.KEYDOWN and not turn):
                if((event.key == pygame.K_a or event.key == pygame.K_LEFT) and not xVel):
                    xVel, yVel = -1, 0
                    turn = True
                elif((event.key == pygame.K_d or event.key == pygame.K_RIGHT) and not xVel):
                    xVel, yVel = 1, 0
                    turn = True
                elif((event.key == pygame.K_w or event.key == pygame.K_UP) and not yVel):
                    xVel, yVel = 0, -1
                    turn = True
                elif((event.key == pygame.K_s or event.key == pygame.K_DOWN) and not yVel):
                    xVel, yVel = 0, 1
                    turn = True

        if(ticks == 0):
            moveSnake(snake, xVel, yVel)
            bigBait = not bigBait
            turn = False
        
        ticks = (ticks + 1) % diff
        pauseB.update()

        if(snake[0] == bait):
            snake.append(snake[-1])
            setBait(bait, snake)
            points += 5

            if(diff > 1 and points % 2 == 0):
                diff -= 1

        run = isAlive(snake)

        if(pauseB.clicked()):
            run = pauseMenu(pauseB)

    return [run, points]

def gameOver(points):
    run = 3
    restartButton = button(WIN, [BLACK, WHITE], [260, 400, 170, 50], "RESTART")
    menuButton = button(WIN, [BLACK, WHITE], [460, 400, 170, 50], "MENU")

    text = H1.render("GAME OVER", True, WHITE)
    textRect = text.get_rect()
    textRect.center = [WIDTH / 2, (HEIGHT / 2) - 50]

    pText = H2.render("POINTS : " + str(points), True, WHITE)
    pTextRect = pText.get_rect()
    pTextRect.center = [WIDTH / 2, (HEIGHT / 2) + 25]

    graphics.drawDoubleRect(WIN, WIDTH / 2, HEIGHT / 2, 550, 400, BLACK, WHITE)
    WIN.blit(text, textRect)
    WIN.blit(pText, pTextRect)

    while(run == 3):
        pygame.display.update()
        restartButton.show()
        menuButton.show()

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return 0
        restartButton.update()
        menuButton.update()

        if(restartButton.clicked()):
            run = 2
        elif(menuButton.clicked()):
            run = 1

        pygame.display.update()
    return run

def options(diff, autoInr):
    run = 4
    playButton = button(WIN, [WHITE, BLACK], [260, 350, 170, 60], "PLAY")
    menuButton = button(WIN, [WHITE, BLACK], [470, 350, 170, 60], "MENU")
    diffSlider = slider(WIN, [WHITE, BLACK], [250, 100], 400, [1, 10], diff, "SET SPEED")
    autoTick = tickBox(WIN, [WHITE, BLACK, GREY], [WIDTH / 2, 200], "Auto Increase", autoInr)
    

    while(run == 4):
        WIN.fill(BLACK)
        
        menuButton.show()
        playButton.show()
        diffSlider.show()
        autoTick.show()

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = 0

        
        menuButton.update()
        playButton.update()
        diffSlider.update()
        autoTick.update()

        diff = diffSlider.getVal()

        if(autoTick.val):
            diffSlider.set_color([GREY, BLACK])
        else:
            diffSlider.set_color([WHITE, BLACK])


        if(menuButton.clicked()):
            run = 1
        elif(playButton.clicked()):
            run = 2

        pygame.display.update()
    
    return [run, diff, autoTick.val]

def menu():
    run = 1
    points = 0
    diff = 5
    autoInr = False

    playButton = button(WIN, [WHITE, BLACK], [260, 350, 170, 60], "PLAY")
    optionsButton = button(WIN, [WHITE, BLACK], [470, 350, 170, 60], "OPTIONS")

    while(run):        
        graphics.drawMenu(WIN, playButton, optionsButton, M_TITLE, M_TITLE_RECT)

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
            
        
        playButton.update()
        optionsButton.update()

        if(playButton.clicked()):
            run = 2
            while(run > 1):
                if(run == 2):
                    run, points = game(diff, autoInr)
                else:
                    run = gameOver(points)
        elif(optionsButton.clicked()):
            run, diff, autoInr = options(diff, autoInr)
            
            while(run > 1):
                if(run == 2):
                    run, points = game(diff, autoInr)
                else:
                    run = gameOver(points)
        
        pygame.display.update()
    
    pygame.quit()

if(__name__ == "__main__"):
    menu()