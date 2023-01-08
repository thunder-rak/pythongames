import pygame
from random import randint
pygame.font.init()

WIDTH, HEIGHT = 844, 844 #DIMENSIONS OF SCREEN (x,y)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
HEALTH_FONT = pygame.font.SysFont('comic sans', 30)
WIN_FONT = pygame.font.SysFont('impact', 200)
pygame.display.set_caption('hello')#name
BULLET_VEL = 5
MAX = 1
RED = (255, 0, 0)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
FPS = 60 #frames per second
VELOCITY = 2
ball_dim = 35 #diameter of ball
BALL = pygame.image.load('img.png') #first ball
BALL=pygame.transform.scale(BALL, (ball_dim, ball_dim)) #scaling b1 down
BALL2 = pygame.image.load('img.png') #second ball
BALL2=pygame.transform.scale(BALL2, (ball_dim, ball_dim))#scaling down
BACK = pygame.transform.scale(pygame.image.load('img_4.png'),(WIDTH, HEIGHT))
B1_HIT = pygame.USEREVENT + 1
B2_HIT = pygame.USEREVENT + 2
def draw_window(b1, b2, b1_bullets, b2_bullets, b1_health, b2_health, snakeLength): #what we are doing 60 times a second
    WIN.blit(BACK, (0, 0)) #color of background (R,G,B)
    pygame.draw.rect(WIN, GREEN, b1)
    pygame.draw.rect(WIN, RED, b2)
    b1_health_text = HEALTH_FONT.render("HEALTH: "  + str(b1_health), 1, BLACK)
    b2_health_text = HEALTH_FONT.render("HEALTH: "  + str(b2_health), 1, BLACK)
    WIN.blit(b1_health_text, (20, 20))
    WIN.blit(b2_health_text, (800, 20))
    for section in snakeLength:
        pygame.draw.rect(WIN, GREEN, section)
    for bullet in b2_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in b1_bullets:
        pygame.draw.rect(WIN, BLUE, bullet)
    if b1_health < 1:
        win_text = WIN_FONT.render("PLAYER 1 WINS", 1, BLACK)
        WIN.blit(win_text, (0, 0))
    if b2_health < 1:
        win_text = WIN_FONT.render("PLAYER 2 WINS", 1, BLACK)
        WIN.blit(win_text, (0, 0))

    pygame.display.update()#adding changes


def main():
    snakeLength = []
    MAX =1
    b1 = pygame.Rect(WIDTH/2 - ball_dim/2, 100, ball_dim, ball_dim)#setting rectangle for ball1
    b2 = pygame.Rect(700, 100, ball_dim, ball_dim)#above for ball2
    snakeLength.append(b1)
    b1_bullets = []
    b2_bullets = []
    b1_health = 10
    b2_health = 10
    run = True
    xMovement = -5
    yMovement = 0
    while run:
        for event in pygame.event.get():#checking if user quit
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()#setting keys
        if keys_pressed[pygame.K_UP] and yMovement != 5:#up key for WASD
            yMovement = -1
            xMovement = 0
        if keys_pressed[pygame.K_DOWN]  and yMovement != -5:#down key for WASD
            yMovement = 1
            xMovement = 0
        if keys_pressed[pygame.K_LEFT] and xMovement != 5:#up key for WASD
            xMovement = -1
            yMovement = 0
        if keys_pressed[pygame.K_RIGHT] and xMovement != -5:#down key for WASD
            xMovement = 1
            yMovement = 0
        for section in snakeLength:
            section.x+= xMovement
            section.y+= yMovement
        if b1.colliderect(b2):
            b2.x = randint(0, 800)
            b2.y = randint(0, 800)
            section = pygame.Rect(snakeLength[len(snakeLength)-1].x - xMovement*10,snakeLength[len(snakeLength)-1].y-yMovement*9, b1.width, b1.width)
            snakeLength.append(section)
        draw_window(b1, b2, b1_bullets, b2_bullets, b1_health, b2_health, snakeLength)


    pygame.quit()
if __name__ == "__main__":
    main()