import pygame
pygame.init()

screen = pygame.display.set_mode([300]*2)

fps = 120
running = True
square = {"x": 0, "y": 0, "w": 100}
click = False
difference = (0, 0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            if click:
                difference = event.rel
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if (square["x"] + 100 > pos[0] > square["x"] and
                    square["y"] + 100 > pos[1] > square["y"]):
                click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            click = False

    screen.fill([0]*3)
    print(square["x"], square["y"])
    square["x"] += difference[0]
    square["y"] += difference[1]
    difference = (0, 0)
    pygame.draw.rect(
        screen, "green",
        (square["x"], square["y"],
         square["w"], square["w"]))

    pygame.display.flip()

pygame.quit()
