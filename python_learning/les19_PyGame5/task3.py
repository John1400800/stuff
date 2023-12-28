import os
import pygame
pygame.init()


def load_img(name: str) -> pygame.Surface:
    fullpath = f"data\\{name}"
    if os.path.isfile(fullpath) and fullpath[-4:] in ('.png', '.jpg'):
        image = pygame.image.load(fullpath)
        # image.set_colorkey(image.get_at((0, 0)))
        return image
    else:
        raise Exception('no file or wrong extension')


car_img = load_img('car2.png')
car_img_pos = [0, 0]
car_img_size = car_img.get_size()
car_speed = 180

screen_size = car_img_size[0]*3, car_img_size[1]
screen = pygame.display.set_mode(screen_size)

running = True
fps = 144
clock = pygame.time.Clock()
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
    car_img_pos[0] += car_speed/fps
    if car_img_pos[0] > screen_size[0]-car_img_size[0] or car_img_pos[0] < 0:
        car_speed = -car_speed
        car_img = pygame.transform.flip(car_img, True, False)
    screen.fill("white")
    screen.blit(car_img, car_img_pos)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
