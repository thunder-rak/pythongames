import pygame
from random import randint
pygame.font.init()

WIDTH, HEIGHT = 1400, 844 #DIMENSIONS OF SCREEN (x,y)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
HEALTH_FONT = pygame.font.SysFont('comic sans', 30)
WIN_FONT = pygame.font.SysFont('impact', 200)
pygame.display.set_caption('hello')#name
BULLET_VEL = 5
MAX = 1
RED = (255, 0, 0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
FPS = 60 #frames per second
VELOCITY = 0
ball_dim = 50 #diameter of ball
BALL = pygame.image.load('img.png') #first ball
BALL=pygame.transform.scale(BALL, (ball_dim, ball_dim)) #scaling b1 down
BALL2 = pygame.image.load('img.png') #second ball
BALL2=pygame.transform.scale(BALL2, (ball_dim, ball_dim))#scaling down
BACK = pygame.transform.scale(pygame.image.load('forest.png'),(WIDTH*8, HEIGHT*8))
B1_HIT = pygame.USEREVENT + 1
B2_HIT = pygame.USEREVENT + 2
def draw_window(b1, platform, b1_bullets, b2_bullets, b1_health, b2_health, back): #what we are doing 60 times a second
    WIN.blit(BACK, (back.x, back.y)) #color of background (R,G,B)
    pygame.draw.rect(WIN, RED, b1)
    b1_health_text = HEALTH_FONT.render("HEALTH: "  + str(b1_health), 1, BLACK)
    b2_health_text = HEALTH_FONT.render("HEALTH: "  + str(b2_health), 1, BLACK)
    for plat in platform:
        pygame.draw.rect(WIN, (0, 100, 0) , plat)
    pygame.display.update()#adding changes


def main():
    VELOCITY = 0
    MAX =1
    b1 = pygame.Rect(WIDTH/2 - 25, HEIGHT/2 - 25, ball_dim, ball_dim)#setting rectangle for ball1
    platformPlaces = [(600, HEIGHT * 8 - 400, 200,200),(100, HEIGHT*8-600, 200,200),(0, HEIGHT * 8, WIDTH*10, 1000), (0, 0, 100, HEIGHT*10)]#above for ball2
    platform = []
    for plat in platformPlaces:
        platform.append(pygame.Rect(plat))
    back = pygame.Rect(0, 0, WIDTH * 8, HEIGHT * 8)
    b1_bullets = []
    b2_bullets = []
    b1_health = 10
    b2_health = 10
    gravity = 0
    clock = pygame.time.Clock()#dont know
    run = True
    while run:
        for event in pygame.event.get():#checking if user quit
            if event.type == pygame.QUIT:
                run = False
            if event.type == B1_HIT:
                b1_health -= 1
            if event.type == B2_HIT:
                b2_health -= 1
        gravity -= 1
        back.x += VELOCITY
        back.y += gravity
        for t in platform:
            t.y += gravity
            t.x += VELOCITY
        keys_pressed = pygame.key.get_pressed()#setting keys
        if keys_pressed[pygame.K_UP]:#up key for WASD
         for plat in platform:
          if b1.colliderect(plat):
            back.y += 11
            gravity = 30
            for rt in platform:
             rt.y += 11
        if keys_pressed[pygame.K_LEFT]:#up key for W
            VELOCITY = 15
        elif keys_pressed[pygame.K_RIGHT]:#down key for WASD
            VELOCITY = -15
        else:
            VELOCITY = 0
        for a in platform:
         if b1.colliderect(a):
          if b1.y + 50 >  a.y and b1.y + 20 < a.y:
            check1 = a.y
            a.y = b1.y + 50
            check2 = a.y
            checkFin = check2-check1
            back.y += checkFin
            for q in platform:
                if q!=a:
                    q.y +=checkFin
            gravity = 1
          else:
              back.x += -VELOCITY
              for q in platform:
                        q.x += -VELOCITY
        if platform[3].x+100>b1.x:
            back.x -= 10
            for q in platform:
                q.x -= 10
        draw_window(b1, platform, b1_bullets, b2_bullets, b1_health, b2_health, back)


    pygame.quit()
if __name__ == "__main__":
    main()