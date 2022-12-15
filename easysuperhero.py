import pygame
import random
import math
from pygame import mixer

# initializing pygame
pygame.init()

# creating screen
screen_width = 533
screen_height = 830
screen = pygame.display.set_mode((screen_width, screen_height))

# set the background
background = pygame.image.load('superheroassets/bg1.jpg')

pygame.display.set_caption('Diablo')

romanBrawler = pygame.image.load('superheroassets/spaceviking.png')
bossimg = pygame.image.load('superheroassets/spaceship.png')

# Score
score = 0
next_boss = 20
HP = 10
bossHP = 10
scoreX = 5
scoreY = 5
HPX = 430
HPY = 5
win = False

def show_score(x, y):
    score_val = font.render("Score: " + str(score),
                        True, (255,255,255))
    screen.blit(score_val, (x , y ))

def show_boss():
    if win:
       screen.blit(bossimg, (bossX, bossY))

def show_HP(x, y):
    HP_val = font.render("HP: " + str(HP),
                        True, (255,255,255))
    screen.blit(HP_val, (x , y ))

font = pygame.font.SysFont('Verdana', 24, 'bold')
font_gameover = pygame.font.SysFont('Verdana', 64, 'bold')

soldierimg = []
soldierX = []
soldierY = []
soldierspeedX = []
soldierspeedY = []

no_of_soldiers = 2

for i in range(no_of_soldiers):
    soldierimg.append(pygame.image.load('superheroassets/alien.png'))
    soldierimg.append(pygame.image.load('superheroassets/spaceinvader.png'))
    soldierX.append(random.randint(50, 460))
    soldierY.append(random.randint(30, 40))
    soldierspeedY.append(-1)

bulletimg = pygame.image.load('superheroassets/spaceray.png')
check = False
bulletX = 260
bulletY = 740

romanBrawlerX = 240
romanBrawlerY = 640

bossX = random.randint(50, 300)
bossY = random.randint(50, 70)
bossspeedX = 5

changeX = 0
running = True

def gameover():
    img_gameover = font_gameover.render('GAME OVER', True, 'white')
    screen.blit(img_gameover, (50, 250))
    check = False

while running:

    screen.blit(background, (0, 0))
    for event in pygame.event.get():

        if bossX <= 0:
            bossspeedX = 5
        if bossX>=300:
            bossspeedX = -5
        bossX += bossspeedX

        if next_boss == 0:
            win = True
            no_of_soldiers = 0
           # score=0

            #collision = isCollision(bulletX, bossX, bulletY, bossY)
            distance = math.sqrt((math.pow(bulletX - bossX, 2)) + (math.pow(bulletY - bossY, 2)))
            if distance < 500:
                explosion = mixer.Sound('superheroassets/explosion.wav')
                explosion.play()
                bulletY = 730
                check = False
                bossX = random.randint(50, 300)
                bossY = random.randint(50, 70)
                bossHP -= 1

        if bossHP == 0:
            win = False
            no_of_soldiers = 2
            bossHP =  5
            score += 20
            next_boss = 20

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if check is False:
                    bulletSound = mixer.Sound('superheroassets/laser.wav')
                    bulletSound.play()
                    DEFAULT_IMAGE_SIZE = (200, 180)
                    romanBrawler = pygame.image.load('superheroassets/spaceviking2.png')
                    romanBrawler = pygame.transform.scale(romanBrawler, DEFAULT_IMAGE_SIZE)
                    check = True
                    bulletX = romanBrawlerX + 70
            if event.key == pygame.K_LEFT:
                changeX = -1
            if event.key == pygame.K_RIGHT:
                changeX = 1
        if event.type == pygame.KEYUP:
            changeX = 0
            romanBrawler = pygame.image.load('superheroassets/spaceviking.png')

    romanBrawlerX=romanBrawlerX+changeX
    if romanBrawlerX <= -40:
        romanBrawlerX = -40
    elif romanBrawlerX >= 400:
        romanBrawlerX = 400

    for i in range(no_of_soldiers):
        if soldierY[i] < 0:
            for j in range(no_of_soldiers):
                soldierY[j] = 1
            gameover()
            break
        soldierY[i] += soldierspeedY[i]

        if soldierY[i] <= 0:
            soldierspeedY[i] = 0.5
            soldierY[i] += soldierspeedY[i]

        if soldierY[i] == 840:
            HP -= 1
            soldierX[i] = random.randint(50, 490)
            soldierY[i] = random.randint(30, 40)

        if HP <= 0:
            gameover()
            HP = 0


        def isCollision(x1, x2, y1, y2):
            distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
            if distance <= 50:
                return True
            else:
                return False

        collision = isCollision(bulletX, soldierX[i], bulletY, soldierY[i])

        if collision:
            explosion = mixer.Sound('superheroassets    /explosion.wav')
            explosion.play()
            bulletY = 730
            check = False
            soldierX[i] = random.randint(50, 490)
            soldierY[i] = random.randint(30, 40)
            score += 1
            next_boss -= 1
        screen.blit(soldierimg[i], (soldierX[i], soldierY[i]))

        #distance = math.sqrt(math.pow(bulletX - bossX, 2) + math.pow(bulletY - bossY, 2))


    if bulletY <= 0:
        bulletY = 730
        check = False
    if check:
        screen.blit(bulletimg, (bulletX, bulletY))
        bulletY -= 3

    #screen.blit(bossimg, (bossX, bossY))
    screen.blit(romanBrawler, (romanBrawlerX, romanBrawlerY))
    show_score(scoreX, scoreY)
    show_HP(HPX, HPY)
    show_boss()
    pygame.display.update()
