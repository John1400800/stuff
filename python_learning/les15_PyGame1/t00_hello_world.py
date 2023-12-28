import pygame


def draw_text(screen: pygame.Surface, color: tuple[int]):
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Pygame!", True, color)
    text_x = screen.get_width() // 2 - text.get_width() // 2
    text_y = screen.get_height() // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    # нарисовали текст
    screen.blit(text, (text_x, text_y))
    # рамка вокруг текста
    pygame.draw.rect(
        screen, color,
        (text_x - 10, text_y - 10,
         text_w + 20, text_h + 20), 3)


if __name__ == "__main__":
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    draw_text(screen, (0, 255, 0))
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
