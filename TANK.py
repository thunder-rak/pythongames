import pygame
pygame.font.init()

WIDTH, HEIGHT = 1400, 800 #DIMENSIONS OF SCREEN (x,y)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
degree_FONT = pygame.font.SysFont('comic sans', 50)
pygame.display.set_caption('hello')#name
BULLET_VEL = 5
MAX = 1
RED = (255, 0, 0)
BLUE = (0,0,255)
GREEN = (0,120,0)
BLACK = (0,0,0)
FPS = 60 #frames per second
VELOCITY = 2
ball_dim = 50 #diameter of ball
BACK = pygame.transform.scale(pygame.image.load('img_9.png'),(WIDTH, HEIGHT))
def draw_window(b1, cannon, pixel_list, ball_list,degrees, bullet, b2, degreesBlue, bullet2): #what we are doing 60 times a second
    for ball in ball_list:
        pygame.draw.rect(WIN, (255,0, 0), ball)
    WIN.blit(BACK, (0, 0)) #color of background (R,G,B)
    degrees_text = degree_FONT.render("DIRECION: "  + str(degrees), 1, BLACK)
    degrees_text2 = degree_FONT.render("DIRECION: "  + str(degreesBlue), 1, BLACK)
    WIN.blit(degrees_text, (20, 20))
    WIN.blit(degrees_text2, (1000, 20))
    for pixel in pixel_list:
        pygame.draw.rect(WIN, GREEN, pixel)
    pygame.draw.rect(WIN, RED, b1)
    pygame.draw.rect(WIN, (255,255,0), b2)
    pygame.draw.rect(WIN, RED, bullet)
    pygame.draw.rect(WIN, (255,255,0), bullet2)
    pygame.display.update()#adding changes


def main():
    ballEdge = [2,5,7,8,9,8,7,5,2]
    pixel_list = []
    ball_list = []
    gravityRed = 0
    gravityBlue = 0
    gravityBull = 0
    gravityBull2 = 0
    for w in range(int(WIDTH/10)):
        for h in range(int(HEIGHT/10)):
            if h*10 > 600 or w*10>WIDTH/2-100 and w*10<WIDTH/2+100:
                pixel = pygame.Rect(w*10,h*10,10,10)
                pixel_list.append(pixel)
    for w in range(0,9):
        for h in range(ballEdge[w]):
            ball = pygame.Rect(0+((h/2) * 10),w*10,10,10)
            ball_list.append(ball)
    for w in range(0,9):
            for h in range(ballEdge[w]):
                ball = pygame.Rect(0-((h/2) * 10),w*10,10,10)
                ball_list.append(ball)
    b1 = pygame.Rect(100,0, ball_dim, ball_dim)
    b2 = pygame.Rect(1300,0, ball_dim, ball_dim)#setting rectangle for ball1
    bullet = pygame.Rect(5685,0, 10, 10)
    bullet2 = pygame.Rect(5685,0, 10, 10)
    cannon = pygame.Rect(b1.x, b1.y, 10, ball_dim)#above for ball2
    run = True
    degrees = 0
    degreesBlue = 0
    velocityRed = 4
    velocityBlue = 4
    velocityBull2 = 0
    velocityBull = 0
    while run:
        for event in pygame.event.get():#checking if user quit
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SLASH:
                    bullet2.x = b2.x
                    bullet2.y = b2.y
                    gravityBull2 = -(90 - degreesBlue)/2.5
                    velocityBull2 = -(degreesBlue)/2.5
                if event.key == pygame.K_c:
                    bullet.x = b1.x
                    bullet.y = b1.y
                    gravityBull = -(90 - degrees)/2.5
                    velocityBull = (degrees)/2.5
        keys_pressed = pygame.key.get_pressed()#setting keys
        if keys_pressed[pygame.K_DOWN]:
            degreesBlue = degreesBlue + -1
        if keys_pressed[pygame.K_UP]:
            degreesBlue = degreesBlue + 1
        if keys_pressed[pygame.K_RIGHT]:
            b2.x -= -velocityBlue
        if keys_pressed[pygame.K_LEFT]:
            b2.x += -velocityBlue
        if keys_pressed[pygame.K_s]:
            degrees = degrees + -1
        if keys_pressed[pygame.K_w]:
            degrees= degrees + 1
        if keys_pressed[pygame.K_d]:
            b1.x -= -velocityRed
        if keys_pressed[pygame.K_a]:
            b1.x += -velocityRed

        gravityBull += 0.5
        gravityBull2 += 0.5
        bullet.x += velocityBull
        bullet.y += gravityBull
        bullet2.x += velocityBull2
        bullet2.y += gravityBull2
        gravityRed += 1
        gravityBlue += 1
        b1.y += gravityRed
        b2.y += gravityBlue
        if b1.y > 545 + 50 or b1.x>WIDTH/2 - 100 - 50:
            b1.x += -10
        else:
            velocityRed = 4
        if b2.y > 545 + 50 or b2.x<WIDTH/2 + 100:
            b2.x += 10
        else:
            velocityBlue = 4
        for pixel in pixel_list:
            if pixel.colliderect(b1):
                gravityRed = -1
        for pixel in pixel_list:
            if pixel.colliderect(b2):
                gravityBlue = -1
        for pixel in pixel_list:
            if pixel.colliderect(bullet):
                for t in ball_list:
                    t.x += bullet.x
                    t.y += bullet.y
                for g in ball_list:
                    for q in pixel_list:
                     if g.colliderect(q):
                         pixel_list.remove(q)
                for a in ball_list:
                    a.x -= bullet.x
                    a.y -= bullet.y
                bullet.x = 78699
                bullet.y = 68898
        for pixel in pixel_list:
            if pixel.colliderect(bullet2):
                for t in ball_list:
                    t.x += bullet2.x
                    t.y += bullet2.y
                for g in ball_list:
                    for q in pixel_list:
                        if g.colliderect(q):
                            pixel_list.remove(q)
                for a in ball_list:
                    a.x -= bullet2.x
                    a.y -= bullet2.y
                bullet2.x = 78699
                bullet2.y = 68898


        draw_window(b1, cannon, pixel_list, ball_list,degrees, bullet, b2,degreesBlue,bullet2)
    pygame.quit()
if __name__ == "__main__":
    main()