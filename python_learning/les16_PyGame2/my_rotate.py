import pygame
pygame.init()

screen = pygame.display.set_mode([600]*2)
surf_rot = pygame.Surface([400]*2)
# surf_rot.set_colorkey((0, 0, 0))
pygame.draw.rect(surf_rot, (255, 0, 0), (180, 0, 40, 300))

center_outer = [600 / 2]*2
center_inner = [400 / 2]*2


running = True
degree = 0
speed = 10
fps = 120
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill([255]*3)

    spin = pygame.transform.rotate(surf_rot, degree)
    screen.blit(spin, (0, 0))

    pygame.display.update()

    degree += speed / fps
    degree %= 360

    clock.tick(fps)

pygame.quit()
