import pygame
pygame.font.init()
WIDTH, HEIGHT = 1400, 844 #DIMENSIONS OF SCREEN (x,y)
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #setting window to the correct size
GOALS_FONT = pygame.font.SysFont('impact', 100)#font of goals
RED = (255, 0, 0) # blue in RGB
BLUE = (0,0,255) #red in RGB
WHITE = (255, 255, 255)  #white
BLACK = (0,0,0)#I think you can guess
ball_dim = 55 #diameter of ball
BACK = pygame.transform.scale(pygame.image.load('img_4.png'),(WIDTH, HEIGHT)) #background image and size
BALL = pygame.transform.scale(pygame.image.load('ball.png'),(ball_dim, ball_dim)) #ball image and size
def draw_window(b1, b2, red, redGoal, blueGoal, goalsForBlue, goalsForRed , blueRec, redRec): #what we are painting
    WIN.blit(BACK, (0, 0)) #background on 0,0 (so it covers the screen)
    pygame.draw.rect(WIN, BLUE, blueRec) #square on blue side
    pygame.draw.rect(WIN, RED, redRec) #square on red side
    goals = GOALS_FONT.render(str(goalsForRed)+" : "+str(goalsForBlue), 1, WHITE) #typing the score
    WIN.blit(goals, (WIDTH/2 - 100, 100)) #painting the score
    pygame.draw.rect(WIN, WHITE, b1) #ball
    WIN.blit(BALL, (b1.x, b1.y)) #ball position (image)
    pygame.draw.rect(WIN, (200, 0, 0), redGoal)#color of red goal
    pygame.draw.rect(WIN, (0, 0 , 200), blueGoal)#color of blue goal
    pygame.draw.rect(WIN, BLUE, b2) #blue character
    pygame.draw.rect(WIN, RED, red) #red character
    pygame.display.update()#adding changes
def main(): #whats going on
    AI =1 #MAKE THIS 1 FOR 1 PLAYER AND 0 FOR TWO PLAYER
    gravity = 0 #gravity of blue player
    gravityBall = 0 #gravity of red player
    b1 = pygame.Rect(WIDTH/2-55/2, 100, ball_dim, ball_dim)#setting rectangle for ball
    b2 = pygame.Rect(1345, HEIGHT - b1.width-10, ball_dim, ball_dim)#above for blue
    red = pygame.Rect(0, HEIGHT - b1.width -10, ball_dim, ball_dim)#above for red
    redRec = pygame.Rect(400, 130, ball_dim, ball_dim)
    blueRec = pygame.Rect(900, 130, ball_dim, ball_dim)
    redGoal = pygame.Rect(0, HEIGHT - 300, ball_dim, 300)
    blueGoal = pygame.Rect(WIDTH - ball_dim, HEIGHT - 300, ball_dim, 300)
    VELOCITY = 0 #x movement for blue
    run = True
    velocityBall = 0 #x movement for ball
    velocityRed = 0 #red x movement
    gravityRed = 0 #u probably know
    goalsForRed = 0
    goalsForBlue = 0
    while run:
        for event in pygame.event.get():#checking if user quit
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN: #if key pressed
                if event.key == pygame.K_UP and gravity == 0: #if up arrow pressed
                    b2.y -= 2  #move off ground(slightly) for blue
                    gravity = -25 #setting movement to an upwards acceleration for blue
                if (event.key == pygame.K_w and gravityRed == 0)  or (b1.x - red.x > -500 and b1.x - red.x < 500 and b1.y+50< red.y and gravityRed == 0 and red.y > 750 and AI == 1): #same for red
                    red.y -= 2
                    gravityRed = -25
        keys_pressed = pygame.key.get_pressed()#setting keys
        if b1.colliderect(redGoal) or b1.colliderect(blueGoal): #if ball touch a goal
            if b1.colliderect(redGoal):
                goalsForBlue += 1
            else:
                goalsForRed += 1
            #everything underneath 'if' is setting up when goal happens
            b1.x = WIDTH/2-55/2
            b1.y =100
            b2.x = 1345
            b2.y = HEIGHT - b1.width-10
            red.x = 0
            red.y = HEIGHT - b1.width-10
            gravity = 0
            gravityRed = 0
            gravityBall = 0
            velocityRed = 0
            VELOCITY = 0
            velocityBall = 0
        if b2.colliderect(b1): #if blue hit ball
            velocityBall = VELOCITY * 2 / 1 #setting ball velocity to double of blue speed
            if VELOCITY > 0: #if blue movement was towards right:
             b1.y -= 1.5
             gravityBall = (gravity - VELOCITY) / 1 #making ball accerlate upwards according to velocity and upward accerleration
            if VELOCITY < 0: #if blue movement was towards lefr:
                b1.y -= 1.5
                gravityBall = (gravity + VELOCITY) / 1
        if red.colliderect(b1): #same as above but for red player
            velocityBall = velocityRed * 2
            if velocityRed > 0:
                b1.y -= 1.5
                gravityBall = (gravityRed - velocityRed) / 1
            if velocityRed < 0:
                b1.y -= 1.5
                gravityBall = (gravityRed + velocityRed) / 1
        if b2.x < 0 or b2.x + b2.width > WIDTH: #if blu player touching left or right wall
            b2.x -= VELOCITY #stop from escaping area
        if red.x < 0 or red.x + red.width > WIDTH: #same except for red
            red.x -= velocityRed
        if b2.y+b2.height<HEIGHT: #if  blu player in air
            gravity = gravity + 1 #make down movement accelerate
        else: #if blu plauer touching floor
            gravity = 0 #stay i=on floor
            b2.y = HEIGHT - b2.height
        if red.y+red.height<HEIGHT: #for red player
            gravityRed = gravityRed + 1
        else:
            gravityRed = 0
            red.y = HEIGHT - red.height
        if b1.y+b1.height<HEIGHT: #ball in air
            gravityBall = gravityBall + 1 #fall
        elif gravityBall < 3 : #if bounce too small
            gravityBall = 0 #no bounce
        else:
            b1.y -= 5
            gravityBall = -gravityBall +6 #making bounce, but weaj=ker from last one
        if b1.y < 0:
            gravityBall = -gravityBall #if touching ceiling reverse direction of falling
        velocityBall += -velocityBall/60 #slide
        velocityRed += -velocityRed/60
        VELOCITY += -VELOCITY/60
        if (VELOCITY <  0.4 and VELOCITY > 0) or (VELOCITY > -0.4 and VELOCITY < 0): #stop slide if slide too small
            VELOCITY = 0
        if (velocityBall <  0.4 and velocityBall > 0) or (velocityBall > -0.4 and velocityBall < 0):
            velocityBall = 0
        if (velocityRed <  0.4 and velocityRed > 0) or (velocityRed > -0.4 and velocityRed < 0):
            velocityRed = 0
        b2.y += gravity #always change y by gravity
        b2.x += VELOCITY #always change x by velocity
        b1.x += velocityBall
        b1.y += gravityBall
        red.x += velocityRed
        red.y += gravityRed
        print(velocityBall)
        if b1.x < 0 or b1.x + b1.width > WIDTH: #if ball hitting sides
            velocityBall = -velocityBall
        if keys_pressed[pygame.K_a] or (red.x + 150 > b1.x and AI == 1):
            velocityRed -= 1 #when a pressed reduce velocity (accelerate to left)
        if keys_pressed[pygame.K_d] or (red.x < (VELOCITY + b1.y/100) * 20 + b1.x or (red.x < b1.x and b1.y > 700)) and AI ==1: #when d pressed increase velocity (accelerate to right)
            velocityRed += 1
        if keys_pressed[pygame.K_LEFT]: #same for arrow keys
            VELOCITY = VELOCITY -1
        if keys_pressed[pygame.K_RIGHT]:
            VELOCITY = VELOCITY +1
        draw_window(b1, b2,  red, redGoal, blueGoal, goalsForBlue, goalsForRed, blueRec, redRec) #drawing
    pygame.quit()
if __name__ == "__main__":
    main()