# 2048

import random
import colorsys
import pygame

# Initialize pygame
pygame.init()

screenSize = 600
# Create a display surface
screen = pygame.display.set_mode((screenSize, screenSize))

width = screen.get_width()
height = screen.get_height()


clock = pygame.time.Clock()

# ad any sounds you might need here


# fonts
smallfont = pygame.font.SysFont('Corbel',35)

bigfont = pygame.font.SysFont('Corbel',70)

biggerfont = pygame.font.SysFont('Corbel',100)


# images


# game states
running = True
pressed = False


# game stats
dt = 0



colors = []

for i in range(2048):
    # Generate a distinct color using HSV color space
    hue = i / 10.0  # Ensure distinct hues
    saturation = 1.0  # Full saturation
    value = 1.0  # Full brightness
    rgb_color = colorsys.hsv_to_rgb(hue, saturation, value)
    
    # Convert RGB values to hexadecimal format
    hex_color = '#%02X%02X%02X' % (
        int(rgb_color[0] * 255),
        int(rgb_color[1] * 255),
        int(rgb_color[2] * 255)
    )
    
    colors.append(hex_color)

start = 2

# game grid values
girdArray = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]


gridWith = screenSize / 4

# functions

#draw the lines of the grid
def drawGrid():
    for x in range(4):
        for y in range(4):
            rect = pygame.Rect(x * gridWith, y * gridWith, gridWith, gridWith)
            pygame.draw.rect(screen, (255,255,255), rect, 1)

# place the numbers/blocks inside the grid
def drawGridNumbers():
    for x in range(4):
        for y in range(4):
            if girdArray[y][x] != 0:
                text = bigfont.render(str(girdArray[y][x]), True, (255,255,255))
                textRect = text.get_rect()
                textRect.center = (x * gridWith + gridWith/2, y * gridWith + gridWith/2)
                
                
                pygame.draw.rect(screen, colors[girdArray[y][x]], ((x * gridWith + 20 , y * gridWith + 20), (gridWith - 40 , gridWith - 40  )), 100)
                
                screen.blit(text, textRect)


#spawn a block on a random empty spot
def addBlock():
   spawn = True
   while spawn:
       x = random.randint(0,3)
       y = random.randint(0,3)
       n = random.randrange(start,start*2 + 1,2)

       if girdArray[y][x] == 0:
           girdArray[y][x] = n
           spawn = False


# spawn the first block
addBlock()



# game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill("black")

    drawGrid()

    drawGridNumbers()

    # controlls
    def left():
        for y in range(4):
            for x in range(1, 4):  
                if girdArray[y][x] != 0:
                    i = x
                    while i > 0:
                        if girdArray[y][i - 1] == 0:
                            girdArray[y][i - 1] = girdArray[y][i]
                            girdArray[y][i] = 0
                        elif girdArray[y][i - 1] == girdArray[y][i]:
                            girdArray[y][i - 1] *= 2
                            girdArray[y][i] = 0
                        else:
                            break
                        i -= 1

                            
                        
                        
#
    def right():
        for y in range(4):
            for x in range(4):  
                if girdArray[y][x] != 0:
                    i = x
                    while i < 3:
                        if girdArray[y][i + 1] == 0:
                            girdArray[y][i + 1] = girdArray[y][x]
                            girdArray[y][x] = 0
                        elif girdArray[y][i + 1] == girdArray[y][x]:
                            girdArray[y][i + 1] *= 2
                            girdArray[y][x] = 0
                        else:
                            break
                        i += 1
                        
                            
                        

    def up():
        for x in range(4):
            for y in range(1, 4):  
                if girdArray[y][x] != 0:
                    i = y
                    while i > 0:
                        if girdArray[i - 1][x] == 0:
                            girdArray[i - 1][x] = girdArray[i][x]
                            girdArray[i][x] = 0
                        elif girdArray[i - 1][x] == girdArray[i][x]:
                            girdArray[i - 1][x] *= 2
                            girdArray[i][x] = 0
                        else:
                            break
                        i -= 1


    def down():
        for x in range(4):
            for y in range(2, -1, -1):  
                if girdArray[y][x] != 0:
                    i = y
                    while i < 3:
                        if girdArray[i + 1][x] == 0:
                            girdArray[i + 1][x] = girdArray[i][x]
                            girdArray[i][x] = 0
                        elif girdArray[i + 1][x] == girdArray[i][x]:
                            girdArray[i + 1][x] *= 2
                            girdArray[i][x] = 0
                        else:
                            break
                        i += 1

                        


    if pressed == False:
        if event.type == pygame.KEYDOWN:
            pressed = True
            if event.key == pygame.K_LEFT:
                left()
            if event.key == pygame.K_RIGHT:
                right()
            if event.key == pygame.K_UP:
                up()
            if event.key == pygame.K_DOWN:
                down()
            addBlock()
        



    if event.type == pygame.KEYUP:
        pressed = False
    


    pygame.display.flip()
    
    dt = clock.tick(60)

   

