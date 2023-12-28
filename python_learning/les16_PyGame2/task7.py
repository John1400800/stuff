# ctrl+z шаг назад ctrl+z шаг вперёд ctrl+c стереть
# всё попробуйте стереть всё а потом сделать шаг назад
import pygame
pygame.init()

screen = pygame.display.set_mode([500]*2)

rects = []
hide_rects = []
idx = 0

all_clear = False

running = True
drowing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not drowing:
                start_pos = list(event.pos).copy()
                rects.append([start_pos, start_pos.copy()])
                drowing = True
                hide_rects.clear()
        elif event.type == pygame.MOUSEMOTION:
            if drowing:
                now_pos = list(event.pos).copy()
                rects[idx][1][0], rects[idx][1][1] = now_pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if drowing:
                drowing = False
                idx += 1

        elif event.type == pygame.KEYDOWN:
            print(event.key, event.mod)
            if event.key == 122 and event.mod == 64 and len(rects):
                idx -= 1
                hide_rects.append(rects.pop(-1))
            elif event.key == 121 and event.mod == 64 and len(hide_rects):
                if not all_clear:
                    idx += 1
                    rects.append(hide_rects.pop(-1))
                else:
                    idx = len(hide_rects)
                    rects.extend(hide_rects.copy())
                    hide_rects.clear()
                    all_clear = False
            elif event.key == 99 and event.mod == 64 and len(rects):
                hide_rects.clear()
                hide_rects.extend(rects)
                rects.clear()
                idx = 0
                all_clear = True

    screen.fill([0]*3)

    if len(rects):
        for rect in rects:
            start_x, end_x = sorted([rect[0][0], rect[1][0]])
            start_y, end_y = sorted([rect[0][1], rect[1][1]])
            width, high = end_x - start_x, end_y - start_y
            pygame.draw.rect(
                screen, 'white', (start_x, start_y, width, high), 4)
        # pygame.draw.line(screen, "white", rect[0], rect[1], 3)

    pygame.display.flip()

pygame.quit()
