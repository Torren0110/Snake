import pygame
from texts import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def drawMenu(WIN, playButton, optionsButton, M_TITLE, M_TITLE_RECT):
    WIN.fill(BLACK)
    WIN.blit(M_TITLE, M_TITLE_RECT)
    playButton.show()
    optionsButton.show()

def drawSnake(WIN, snake, S_WIDTH):
    if(snake[0][0] + S_WIDTH == snake[1][0]):
        pygame.draw.rect(WIN, WHITE, [snake[0][0] + 1, snake[0][1] + 1, S_WIDTH - 1, S_WIDTH - 2])
    elif(snake[0][0] - S_WIDTH == snake[1][0]):
        pygame.draw.rect(WIN, WHITE, [snake[0][0], snake[0][1] + 1, S_WIDTH - 1, S_WIDTH - 2])
    elif(snake[0][1] + S_WIDTH == snake[1][1]):
        pygame.draw.rect(WIN, WHITE, [snake[0][0] + 1, snake[0][1] + 1, S_WIDTH - 2, S_WIDTH - 1])
    elif(snake[0][1] - S_WIDTH == snake[1][1]):
        pygame.draw.rect(WIN, WHITE, [snake[0][0] + 1, snake[0][1], S_WIDTH - 2, S_WIDTH - 1])
    else:
        pygame.draw.rect(WIN, WHITE, [snake[0][0] + 1, snake[0][1] + 1, S_WIDTH - 2, S_WIDTH - 2])

    for i in range(1, len(snake) - 2):
        xCh = 1
        yCh = 1
        widthCh = 2
        heightCh = 2

        if(snake[i][0] + S_WIDTH == snake[i - 1][0] or snake[i][0] + S_WIDTH == snake[i + 1][0]):
            widthCh -= 1
        if(snake[i][0] - S_WIDTH == snake[i - 1][0] or snake[i][0] - S_WIDTH == snake[i + 1][0]):
            widthCh -= 1
            xCh -= 1
        if(snake[i][1] + S_WIDTH == snake[i - 1][1] or snake[i][1] + S_WIDTH == snake[i + 1][1]):
            heightCh -= 1
        if(snake[i][1] - S_WIDTH == snake[i - 1][1] or snake[i][1] - S_WIDTH == snake[i + 1][1]):
            heightCh -= 1
            yCh -= 1
        
        pygame.draw.rect(WIN, WHITE, [snake[i][0] + xCh, snake[i][1] + yCh, S_WIDTH - widthCh, S_WIDTH - heightCh])
    
    if(snake[-2][0] + S_WIDTH == snake[-3][0]):
        pygame.draw.rect(WIN, WHITE, [snake[-2][0] + 1, snake[-2][1] + 1, S_WIDTH - 1, S_WIDTH - 2])
    elif(snake[-2][0] - S_WIDTH == snake[-3][0]):
        pygame.draw.rect(WIN, WHITE, [snake[-2][0], snake[-2][1] + 1, S_WIDTH - 1, S_WIDTH - 2])
    elif(snake[-2][1] + S_WIDTH == snake[-3][1]):
        pygame.draw.rect(WIN, WHITE, [snake[-2][0] + 1, snake[-2][1] + 1, S_WIDTH - 2, S_WIDTH - 1])
    elif(snake[-2][1] - S_WIDTH == snake[-3][1]):
        pygame.draw.rect(WIN, WHITE, [snake[-2][0] + 1, snake[-2][1], S_WIDTH - 2, S_WIDTH - 1])
    else:
        pygame.draw.rect(WIN, WHITE, [snake[-2][0] + 1, snake[-2][1] + 1, S_WIDTH - 2, S_WIDTH - 2])

def drawUI(WIN, points, G_TITLE, G_TITLE_RECT, G_POINTS, G_POINTS_RECT):
    WIN.fill(BLACK)
    WIN.blit(G_TITLE, G_TITLE_RECT)
    WIN.blit(G_POINTS, G_POINTS_RECT)
    pointsNum = H2.render(points, True, WHITE)
    pointsNumRect = pointsNum.get_rect()
    pointsNumRect.center = (G_POINTS_RECT.center[0] + G_POINTS_RECT.width // 2 + pointsNumRect.width // 2, G_POINTS_RECT.center[1])
    WIN.blit(pointsNum, pointsNumRect)

def drawBorder(WIN, SIDE_MARGE, TOP_MARGE, WIDTH, HEIGHT):
    pygame.draw.rect(WIN, WHITE, [SIDE_MARGE - 5, TOP_MARGE - 5, WIDTH - (2 * (SIDE_MARGE - 5)), HEIGHT - TOP_MARGE - SIDE_MARGE + 10])
    pygame.draw.rect(WIN, BLACK, [SIDE_MARGE, TOP_MARGE, WIDTH - (2 * SIDE_MARGE), HEIGHT - TOP_MARGE - SIDE_MARGE])

def drawBait(WIN, bait, S_WIDTH, bigBait):
    if(bigBait):
        pygame.draw.rect(WIN, RED, [bait[0], bait[1], S_WIDTH, S_WIDTH])
    else:
        pygame.draw.rect(WIN, RED, [bait[0] + 1, bait[1] + 1, S_WIDTH - 2, S_WIDTH - 2])

def drawDoubleRect(WIN, x, y, l, b, pColor, sColor):
    pygame.draw.rect(WIN, sColor, [x - (l / 2), y - (b / 2), l, b])
    pygame.draw.rect(WIN, pColor, [x - (l / 2) + 2, y - (b / 2) + 2, l - 4, b - 4])

def drawPauseMenu(WIN):
    pass
