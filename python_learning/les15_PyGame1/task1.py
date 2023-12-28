import pygame

if __name__ == "__main__":
    pygame.init()
    size_window = tuple(map(int, input().split()))
    pygame.display.set_caption("Крест")
    screen = pygame.display.set_mode(size_window)

    screen.fill((0, 0, 0))
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pygame.draw.line(screen, (255, 255, 255), (0, 0), size_window, 5)
        pygame.draw.line(screen, (255, 255, 255),
                         (0, size_window[1]), (size_window[0], 0), 5)
        pygame.display.flip()
    pygame.quit()
