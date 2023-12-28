import os
import pygame
pygame.init()

img_game_over = pygame.image.load(f"data\\gameover.png")
screen = pygame.display.set_mode(img_game_over.get_size())

pos = [-img_game_over.get_size()[0], 0]

running = True
fps, clock = 60, pygame.time.Clock()
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
    screen.fill("black")
    screen.blit(img_game_over, pos)
    pygame.display.update()
    clock.tick(fps)
    if pos[0] <= 0:
        pos[0] += 200/fps
pygame.quit()



