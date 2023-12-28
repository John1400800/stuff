import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))

running = True
color = pygame.Color(255, 255, 255)
screen.fill([255]*3)
pos = (0, 0)
fps = 50
cnt = 0
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            pos = event.pos

    screen.fill(color)
    pygame.draw.circle(screen, [255]*3, pos, 20)
    pygame.display.flip()
    if cnt % fps < 60: 
        if color.hsva[0] < 359:
            color.hsva = (color.hsva[0] + 1, 100, 100)
        else:
            color.hsva = (0, 100, 100)
    cnt += 1
    clock.tick(fps)
