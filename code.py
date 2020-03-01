import pygame
import time
import random


pygame.init()


eat = pygame.mixer.Sound("eat_apple.ogg")
pygame.mixer.music.load("background1.mp3")


white = (255, 255, 255)
black = (0,0,0)
red = (255, 0, 0)
green = (57, 255, 20)
blue = (0, 0, 255)


display_width = 800
display_height = 600


gameDisplay = pygame.display.set_mode((display_width,display_height))


pygame.display.set_caption('Shaap')


icon = pygame.image.load('snakeHead.png')
pygame.display.set_icon(icon)


img = pygame.image.load('snakeHead.png')
appleimg = pygame.image.load('apple.png')


clock = pygame.time.Clock()
block_size = 20
AppleThickness = 30

FPS = 15

direction = "up"

smallfont = pygame.font.SysFont("comicsansms", 20)
mediumfont = pygame.font.SysFont("comicsansms", 35)
largefont = pygame.font.SysFont("comicsansms", 50)

    
def pause():
    paused = True

    message_to_screen("Paused", red, -50, size = "large")

    # message_to_screen("Press C to Continue or Q to Quit", white, 250, size = "small")

    pygame.display.update()
    clock.tick(5)

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.Quit()
                quit() 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

##                elif event.key == pygame.K_q:
##                    pygame.quit()
##                    quit()
                    
        # gameDisplay.fill(black)
        message_to_screen("Paused", red, -50, size = "large")

        # message_to_screen("Press C to Continue or Q to Quit", white, 250, size = "small")

        pygame.display.update()
        clock.tick(5)

    
def score(score):
    text = smallfont.render("Score: " + str(score), True, white)
    gameDisplay.blit(text, [0,0])


def randAppleGen():
    
    randAppleX = round(random.randrange(0, display_width - AppleThickness - 15))                    
    randAppleY = round(random.randrange(0, display_height - AppleThickness - 15))

    return randAppleX, randAppleY


def game_intro():
    intro = True

    pygame.mixer.music.play(-1)
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

     
        gameDisplay.fill(black)
        message_to_screen("Welcome to Shaap",
                          green,
                          -150,
                          "large")

        message_to_screen("The objective of the snake is to eat red apples",
                          white,
                          10,
                          "small")
        message_to_screen("The more apples you eat, the longer you get",
                          white,
                          50,
                          "small")
        message_to_screen("If you run into yourself or the edges, you die!",
                          white,
                          70,
                          "small")
        message_to_screen("Press C to play, P to Pause or Q to Quit",
                          red,
                          150,
                          "small")
        

        pygame.display.update()
        clock.tick(5)
        

def snake(block_size, snakelist):


    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    

    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]) )

    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

        
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = mediumfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)

    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

    
def gameLoop():

    global direction
    
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = -10

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()
    
    

    while not gameExit:

        if gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("Game Over", red, -50, "large")
            message_to_screen("Press C to play again or press Q to Quit", white, 150, "small")
            pygame.display.update()

        while gameOver == True:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                    
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                        
                    if event.key == pygame.K_c:
                        
                        direction = "up"
                        gameLoop()
                
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True;
            
        
        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(black)

        
        # pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        gameDisplay.blit(appleimg, (randAppleX, randAppleY))
        
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)

        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        
        
        snake(block_size, snakeList)
        score(snakeLength-1)
        pygame.display.update()

##        previous version
##                       
##        if lead_x == randAppleX and lead_y == randAppleY:
##            randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
##            randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0
##            snakeLength += 1

                
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                pygame.mixer.Sound.play(eat)
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1  
                       
        if snakeLength >= 10:
            clock.tick(FPS+2)
        elif snakeLength >= 20:
            clock.tick(FPS+5)
        elif snakeLength >= 30:
            clock.tick(FPS+10)
        elif snakeLength >= 70:
            clock.tick(FPS+40)
        
        else:
            clock.tick(FPS)
        

    

    pygame.quit()
    quit()

game_intro()
gameLoop()
