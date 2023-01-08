import pygame
pygame.font.init()

WIDTH, HEIGHT = 1400, 800 #DIMENSIONS OF SCREEN (x,y)

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
ball_dim = 25 #diameter of ball
BACK = pygame.transform.scale(pygame.image.load('img_4.png'),(WIDTH, HEIGHT))
def draw_window(b1, b2, pixel_list): #what we are doing 60 times a second
    WIN.blit(BACK, (0, 0)) #color of background (R,G,B)
    for pixel in pixel_list:
        pygame.draw.rect(WIN, BLUE, pixel)
    pygame.draw.rect(WIN, RED, b1)

    pygame.display.update()#adding changes


def main():
    pixel_list = []
    for w in range(int(WIDTH/25)):
     for h in range(int(HEIGHT/25)):
        pixel = pygame.Rect(w*25,h*25,25,25)
        pixel_list.append(pixel)

    b1 = pygame.Rect(0,0, ball_dim, ball_dim)#setting rectangle for ball1
    b2 = pygame.Rect(700, 100, ball_dim, ball_dim)#above for ball2
    run = True
    while run:
        for event in pygame.event.get():#checking if user quit
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT:
                    b1.x += 25
                if event.key == pygame.K_LEFT:
                    b1.x += -25
                if event.key == pygame.K_UP:
                    b1.y -= 25
                if event.key == pygame.K_DOWN:
                    b1.y += 25
        for pixel in pixel_list:
            if pixel.colliderect(b1):
                pixel_list.remove(pixel)

        draw_window(b1, b2, pixel_list)
    pygame.quit()
if __name__ == "__main__":
    main()