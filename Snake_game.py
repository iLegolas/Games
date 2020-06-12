import pygame
import sys , os
import time
from pygame.locals import *
import random

pygame.init()

red  = (255,0,0)
white = (255,255,255)
black = (100,0,0)
cyan = (0,255,255)
window_width = 1024
window_height = 720

gameDisplay  = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('The Snake Game')
font = pygame.font.SysFont(None,25,bold = True)

direction = "none"

def myquit():
    pygame.quit()
    sys.exit(0)

clock = pygame.time.Clock()
FPS = 17
blockSize = 10
noPixel = 0

def snake(blockSize, snakelist):
    for size in snakelist:
        pygame.draw.rect(gameDisplay, black,[size[0],size[1],blockSize,blockSize])

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [window_width/2, window_height/2])

def gameLoop():
    gameExit = False
    gameOver = False
    global direction
    lead_x = window_width/2
    lead_y = window_height/2

    change_pixels_of_x = 0
    change_pixels_of_y = 0

    snakelist = []
    snakeLength = 1

    randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10
    randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press c to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()

                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN

                if leftArrow and direction != "right":
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel
                    direction = "left"
                elif rightArrow and direction != "left":
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel
                    direction = "right"
                elif upArrow and direction != "down":
                    change_pixels_of_y = -blockSize
                    change_pixels_of_x = noPixel
                    direction = "up"
                elif downArrow and direction != "up":
                    change_pixels_of_y = blockSize
                    change_pixels_of_x = noPixel
                    direction = "down"

            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                gameOver = True

        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y

        gameDisplay.fill(white)
        AppleThickness = blockSize

        pygame.draw.rect(gameDisplay,red, [randomAppleX,randomAppleY,AppleThickness,AppleThickness])

        allspriteslist = []
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)

        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSegment in snakelist [:-1]:
            if eachSegment == allspriteslist:
                gameOver = True

        score = snakeLength - 1
        show = font.render("Score: " + str(score), True,cyan)
        gameDisplay.blit(show, (10, 10))

        snake(blockSize, snakelist)
        pygame.display.update()

        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
                randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10
                randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10
                snakeLength += 1

        clock.tick(FPS)
    pygame.quit()
    quit()
gameLoop()
