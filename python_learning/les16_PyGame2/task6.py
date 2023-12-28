import pygame
import math
pygame.init()

w = 401
center = [401/2]*2
r = 160

speed = 10
k = 1

degrees = a, b, c = [0, 120, 240]

screen = pygame.display.set_mode([w]*2)

running = True
fps = 120
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mous_btn = event.button
            k += 1 if mous_btn == 1 else -1

    screen.fill([0]*3)

    pygame.draw.circle(screen, "white", center, 20)

    for i, d in enumerate(degrees):
        pygame.draw.polygon(screen, "white",
                            (center,

                             (center[0] + r*math.cos((math.pi/180)*d),
                              center[1] + r*math.sin((math.pi/180)*d)),

                             (center[0] + r*math.cos((math.pi/180)*(d+30)),
                              center[1] + r*math.sin((math.pi/180)*(d+30)))))
        degrees[i] += (speed*k)/fps % 360

    clock.tick(fps)
    pygame.display.update()
pygame.quit()
