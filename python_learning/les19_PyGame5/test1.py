import os
import sys
import pygame

pygame.init()
pygame.mouse.set_visible(False)


def load_image(name, colorkey=None):
    fullname = f"data\\{name}"
    if not os.path.isfile(fullname) or fullname[-4:] != ".png":
        print(f"file named {name} not found or file not png")
        w, h = 25, 50
        image = pygame.Surface((50, 100))
        pygame.draw.polygon(image, "white", ((0, h*0.8), (0, 0), (w, h*0.60)))
        pygame.draw.line(image, "white", (w*0.1, h*0.2), (w*0.8, h), 10)
        image.set_colorkey((0, 0, 0))
    else:
        image = pygame.image.load(fullname)
    return image


img2 = load_image("arrow.png")
arrow_pos = -img2.get_width(), -img2.get_height()

image_size = 200, 100
image = pygame.Surface(image_size)
image.fill(pygame.Color("red"))

size_window = width, height = 500, 400
screen = pygame.display.set_mode(size_window)
start_pos_surf_rect = [0, (height - image_size[1])/2]
v = 30

rect_run = True
running = True
clock = pygame.time.Clock()
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.MOUSEMOTION:
            arrow_pos = [-img2.get_width(), -img2.get_height()] if 0 == ev.pos[0] or \
                0 == ev.pos[1] else ev.pos
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if (start_pos_surf_rect[0] <= arrow_pos[0] <= start_pos_surf_rect[0]+image_size[0] and
                    start_pos_surf_rect[1] <= arrow_pos[1] <= start_pos_surf_rect[1]+image_size[1]):
                rect_run = not rect_run

    screen.fill("black"if rect_run else "brown")
    pygame.draw.rect(
        screen, "black", (*[p + 2 for p in start_pos_surf_rect], *image_size))
    screen.blit(image, start_pos_surf_rect)
    screen.blit(img2, arrow_pos)
    pygame.display.update()

    start_pos_surf_rect[0] += v/60 if rect_run else 0
    if start_pos_surf_rect[0]+image_size[0] > width or start_pos_surf_rect[0] < 0:
        v = -v
    clock.tick(144)

pygame.quit()
