import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))

running = True
screen.fill('blue')
fps = 60
v = 10
clock = pygame.time.Clock()
click = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            radius = 0
            click = True
    screen.fill('blue')
    if click:
        pygame.draw.circle(screen, 'yellow', pos, radius)
        radius += v / fps
    pygame.display.flip()
    clock.tick(fps)
