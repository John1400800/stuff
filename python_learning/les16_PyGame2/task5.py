import pygame
pygame.init()

screen = pygame.display.set_mode([501]*2)
font = pygame.font.Font(None, 16)


circle = {"x": 501*0.5, "y": 501*0.5, "r": 20}

fps = 120
spped = 1
running = True
clock = pygame.time.Clock()
pos = [circle["x"]]*2
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            pos = event.pos

    screen.fill([0]*3)
    pygame.draw.circle(screen, "red",
                       (circle["x"], circle["y"]), circle["r"])
    text_cord = font.render(
        f"[ x:{circle['x']}; y:{circle['y']} ]", True, "white")
    screen.blit(text_cord, (10, 10))
    pygame.display.update()

    if pos[0] > circle["x"]:
        circle["x"] += spped
    elif pos[0] < circle["x"]:
        circle["x"] -= spped
    if pos[1] > circle["y"]:
        circle["y"] += spped
    elif pos[1] < circle["y"]:
        circle["y"] -= spped

    clock.tick(fps)
pygame.quit()
