from random import randint
import pygame


def draw_random_line(screen: pygame.Surface):
    color = tuple([randint(0, 255) for _ in range(3)])
    start_pos = (randint(0, screen.get_width()),
                 randint(0, screen.get_width()))
    end_pos = (randint(0, screen.get_width()),
               randint(0, screen.get_height()))
    pygame.draw.line(screen, color, start_pos, end_pos, 1)


def draw_random_rect(screen: pygame.Surface):
    color = tuple([randint(0, 255) for _ in range(3)])
    start_pos = (randint(0, screen.get_width()),
                 randint(0, screen.get_height()))
    size = (randint(0, screen.get_width() - start_pos[0]),
            randint(0, screen.get_height() - start_pos[1]))
    pygame.draw.rect(screen, color, (*start_pos, *size), 1)


def draw_pixels(screen: pygame.Surface):
    color = pygame.Color(0, 0, 0)
    for i in range(10000):
        start_pos = (randint(0, screen.get_width()),
                     randint(0, screen.get_height()))
        pygame.draw.rect(screen, color, (*start_pos, 1, 1))
        # pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 500))

    screen.fill((255, 255, 255))
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        # draw_random_rect(screen)
        # draw_random_line(screen)
        draw_pixels(screen)
        pygame.display.flip()
    pygame.quit()
