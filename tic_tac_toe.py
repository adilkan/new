import pygame
from collections import defaultdict

pygame.init()
width = 800
height = 800
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
is_x = True

dis = pygame.display.set_mode([width, height], pygame.RESIZABLE)
dis.fill(white)
horizont = height // 3
vertical = width // 3
pygame.draw.line(dis, black, (0, horizont), (width, horizont), 4)
pygame.draw.line(dis, black, (0, horizont * 2), (width, horizont * 2), 4)
pygame.draw.line(dis, black, (vertical, 0), (vertical, height), 4)
pygame.draw.line(dis, black, (vertical * 2, 0), (vertical * 2, height), 4)
pygame.draw.line(dis, black, (0, 0), (0, height), 4)
pygame.draw.line(dis, black, (width - 3, 0), (width - 3, height), 4)
pygame.draw.line(dis, black, (width, 0), (0, 0), 4)
pygame.draw.line(dis, black, (0, height - 3), (width, height - 3), 4)
pygame.display.flip()

grid = [[0, 0, 0] for i in range(3)]


def win(grid):
    count_horizont = {}
    count_vertical = {}

    for i in range(3):
        for j in range(3):
            if grid[i][j]:
                if i not in count_vertical:
                    count_vertical[i] = {}
                count_vertical[i][grid[i][j]] = count_vertical[i].get(grid[i][j], 0) + 1
                if j not in count_horizont:
                    count_horizont[j] = {}
                count_horizont[j][grid[i][j]] = count_horizont[j].get(grid[i][j], 0) + 1
    count = {1: {}, 2: {}}

    for i in range(1, 4):
        count[1][grid[i - 1][i - 1]] = count[1].get(grid[i - 1][i - 1], 0) + 1
        count[2][grid[-i][i - 1]] = count[2].get(grid[-i][i - 1],0) + 1

    for i in count_vertical:
        for j in count_vertical[i]:
            if count_vertical[i][j] == 3:
                return j

    for i in count_horizont:
        for j in count_horizont[i]:
            if count_horizont[i][j] == 3:
                return j

    for i in (1, 2):
        for j in count[i]:
            if j and count[i][j] == 3:
                return j
    return 0
imut = True


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and imut:
            x, y = pygame.mouse.get_pos()
            x //= vertical
            y //= horizont
            if not grid[y][x]:
                if is_x:
                    pygame.draw.line(dis, black, (x * vertical, y * horizont), ((x + 1) * vertical, (y + 1) * horizont),
                                     6)
                    pygame.draw.line(dis, black, ((x + 1) * vertical, y * horizont), (x * vertical, (y + 1) * horizont),
                                     6)
                    grid[y][x] = 1

                else:
                    pygame.draw.circle(dis, black, (x * vertical + vertical // 2, y * horizont + horizont // 2),
                                       min(vertical // 2, horizont // 2), 6)
                    grid[y][x] = 2
                pygame.display.update()
                is_x = not is_x
    check = win(grid)
    if check:
        f_sys = pygame.font.SysFont('arial', 50)
        text = f_sys.render(f'{check}  win', black, green)
        pos = text.get_rect(center = (width // 2, height // 2))
        dis.blit(text, pos)
        pygame.display.update()

        imut = False