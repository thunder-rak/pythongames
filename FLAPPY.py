import pygame
from random import randint
pygame.font.init()
WIDTH, HEIGHT = 1400, 844 #DIMENSIONS OF SCREEwN (x,y)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0,0,0)
score_font = pygame.font.SysFont('comic sans', 30)
FLAP = pygame.transform.scale(pygame.image.load('img_7.png'),(80, 60))
BACK = pygame.transform.scale(pygame.image.load('img_6.png'),(WIDTH, HEIGHT))
def draw_window(b1,score, pipes): #what we are doing 60 times a second
    WIN.blit(BACK, (0, 0)) #color of background (R,G,B)
    WIN.blit(FLAP, (b1.x, b1.y)) #color of background (R,G,B)
    for t in pipes:
        pygame.draw.rect(WIN, (0, 100, 0), t)
    score_text = score_font.render(str(round(score)), 1, BLACK)
    WIN.blit(score_text, (50,50))
    pygame.display.update()#adding changes
def main():
    b1 = pygame.Rect(200, HEIGHT/2 - 100, 80, 60)#setting rectangle for ball1
    p1 = pygame.Rect(WIDTH - 200, HEIGHT-300, 100, 1000)
    p2 = pygame.Rect(WIDTH - 200, -800, 100, 1000)
    p3 = pygame.Rect(WIDTH - -300, HEIGHT-300, 100, 1000)
    p4 = pygame.Rect(WIDTH - -300, -800, 100, 1000)
    p5 = pygame.Rect(WIDTH - -800, HEIGHT-300, 100, 1000)
    p6 = pygame.Rect(WIDTH - -800, -800, 100, 1000)
    run = True
    gravity = 0
    pipes = [p1,p2,p3,p4,p5,p6]
    pipesHalf = [p2,p4,p6]
    acceleration = 0
    score = 0
    while run:
        for event in pygame.event.get():#checking if user quit
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP:
                    gravity = -15
        acceleration += 0.003
        score += 1/35
        p1.x -= 5 +acceleration
        p2.x -= 5 +acceleration
        p3.x -= 5+acceleration
        p4.x -= 5+acceleration
        p5.x -= 5+acceleration
        p6.x -= 5+acceleration
        for p in pipesHalf:
            if p.x < 0:
                p.y= HEIGHT - 300
                pipes[(pipesHalf.index(p)+1)*2-2].y = -800
                p.x = 1400
                pipes[(pipesHalf.index(p)+1)*2-2].x = 1400
                pos = randint(-150, 150)
                p.y += pos
                pipes[(pipesHalf.index(p)+1)*2-2].y += pos
        for a in pipes:
            if a.colliderect(b1):
                run = False
        if b1.y<0 or b1.y > HEIGHT - 60:
            run = False
        b1.y +=gravity
        gravity +=0.5
        draw_window(b1,score, pipes)
    pygame.quit()
    print(round(score))
if __name__ == "__main__":
    main()