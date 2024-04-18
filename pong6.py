# Créé par delorme, le 17/04/2024 en Python 3.7
import pygame
from random import randint, random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

screen.fill(BLACK)
pygame.display.update()

myfont = pygame.font.SysFont('monospace', 50)

print("pong6")
screen.fill(BLACK)
title = myfont.render("Single Player Pong:", False, GREEN)
screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
pygame.display.update()
pygame.time.delay(1000)
screen.fill(BLACK)
# countdown before start game
# loop from 3 to 0 and write the number in the middle of the screen
import time
for i in range(3, 0, -1):
    count = myfont.render(str(i), False, GREEN)
    screen.blit(count, (WIDTH // 2 - count.get_width() // 2, HEIGHT // 2 - count.get_height() * 2))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.fill(BLACK)

#???

radius = 10
x = WIDTH//2
y = radius + 10
pygame.draw.circle(screen, WHITE, (x, y), radius)  # Position is the center of the circle.


paddle = { "width" : 200,
           "height": 20,
           "color" : BLUE,
           "x"     : 0,
           "y"     : 0}
paddle["x"] = WIDTH//2-paddle["width"]//2
paddle["y"] = HEIGHT-paddle["height"]
pygame.draw.rect(screen, paddle["color"], (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

speed = 5
sens_x = sens_y = 1
pause = False
score = 0


end = False
while not end:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        pause = True

    if key[pygame.K_RETURN]:
        pause = False

    if key[pygame.K_l]:
        auto = False

    if not pause:

        if key[pygame.K_LEFT]:
            print("Key LEFT pressed")
            paddle["x"]-=speed
            if paddle["x"]<0 :
                paddle["x"]=0

        if key[pygame.K_RIGHT]:
            print("Key RIGHT pressed")
            paddle["x"]+=speed
            if paddle["x"]>WIDTH-paddle["width"]:
                paddle["x"]=WIDTH-paddle["width"]

        # change x direction if the ball hits the left or right edge
        if x<radius or x>WIDTH-radius :
            sens_x=-sens_x

        # change y direction if the ball hits the top edge
        if y<radius  :
            sens_y=-sens_y


         # if the ball hits the paddle top
        if y>=paddle["y"]-radius :

            # if the ball is between the x paddle begin and the x paddle end
            if x>paddle["x"] and x<paddle["x"]+paddle["width"] :
                # change y direction
                sens_y=-sens_y
                score +=1

        # if the ball comes out of the screen from below, end the game
        if y>HEIGHT :
            end = True

        # compute the new ball coordinates
        x = x + sens_x * speed
        y = y + sens_y * speed

    # redraw ball and paddle
    point = myfont.render(str(score)+" pts", False, GREEN)
    screen.blit(point, (0, 0))
    pygame.draw.circle(screen, WHITE, (x, y), radius)
    pygame.draw.rect(screen, paddle["color"], (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

        # Display the score in position (10, 0) (top left on the screen)

    # update screen
    pygame.display.update()
    pygame.time.delay(10)

# Wait a bit to be sure the player knows his score
pygame.time.delay(2000)
pygame.quit()

pygame.quit()
