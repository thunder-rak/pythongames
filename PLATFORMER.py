import pygame
pygame.font.init()

WIDTH, HEIGHT = 1400, 844 #DIMENSIONS OF SCREEN (x,y)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
HEALTH_FONT = pygame.font.SysFont('comic sans', 30)
WIN_FONT = pygame.font.SysFont('impact', 200)
pygame.display.set_caption('hello')#name
BULLET_VEL = 5
MAX = 1
RED = (255, 0, 0)
BLUE = (0,0,255)
BLACK = (0,0,0)
FPS = 60 #frames per second
VELOCITY = 2
ball_dim = 50 #diameter of ball
BALL = pygame.image.load('img.png') #first ball
BALL=pygame.transform.scale(BALL, (ball_dim, ball_dim)) #scaling b1 down
BALL2 = pygame.image.load('img.png') #second ball
BALL2=pygame.transform.scale(BALL2, (ball_dim, ball_dim))#scaling down
BACK = pygame.transform.scale(pygame.image.load('img_4.png'),(WIDTH, HEIGHT))
B1_HIT = pygame.USEREVENT + 1
B2_HIT = pygame.USEREVENT + 2
def draw_window(b1, b2, b1_bullets, b2_bullets, b1_health, b2_health): #what we are doing 60 times a second
    WIN.blit(BACK, (0, 0)) #color of background (R,G,B)
    pygame.draw.rect(WIN, RED, b1)
    b1_health_text = HEALTH_FONT.render("HEALTH: "  + str(b1_health), 1, BLACK)
    b2_health_text = HEALTH_FONT.render("HEALTH: "  + str(b2_health), 1, BLACK)
    WIN.blit(b1_health_text, (20, 20))
    WIN.blit(b2_health_text, (800, 20))
    WIN.blit(BALL2, (b2.x, b2.y))#Position of ball2(x,y)
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
    MAX =1
    b1 = pygame.Rect(100, 100, ball_dim, ball_dim)#setting rectangle for ball1
    b2 = pygame.Rect(700, 100, ball_dim, ball_dim)#above for ball2
    b1_bullets = []
    b2_bullets = []
    b1_health = 10
    b2_health = 10
    clock = pygame.time.Clock()#dont know
    gravity = 0
    run = True
    while run:
        for event in pygame.event.get():#checking if user quit
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT:
                    b1.x += 50
                if event.key == pygame.K_LEFT:
                    b1.x += -50
                if event.key == pygame.K_m and len(b2_bullets)<MAX:
                    bullet = pygame.Rect(b2.x,b2.y+b1.height//2, 10, 5)
                    b2_bullets.append(bullet)
            if event.type == B1_HIT:
                b1_health -= 1
            if event.type == B2_HIT:
                b2_health -= 1
        keys_pressed = pygame.key.get_pressed()#setting keys
        gravity +=1
        b1.y += gravity
        draw_window(b1, b2, b1_bullets, b2_bullets, b1_health, b2_health)
    pygame.quit()
if __name__ == "__main__":
    main()