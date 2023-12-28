import pygame
pygame.init()

screen = pygame.display.set_mode([200]*2)
font = pygame.font.Font(None, 50)


running = True
cnt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == 770:
            cnt += 1

    screen.fill([255]*3)
    text = font.render(f"{cnt}", True, "red")
    screen.blit(
        text, ((200 - text.get_width()) / 2,
               (200 - text.get_height()) / 2))
    pygame.display.update()

pygame.quit()
