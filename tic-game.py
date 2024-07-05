import time

import pygame
import random

DISPLAY_WIDTH = 300
DISPLAY_HEIGHT = 300

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
FPS = 30
clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Крестики-нолики")

field = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]


def draw_grid():
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 3)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 3)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 3)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 3)


def draw_tic_tac_toe():
    for i in range(3):
        for j in range(3):
            if field[i][j] == "x":
                pygame.draw.line(screen, BLACK, (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 3)
                pygame.draw.line(screen, BLACK, (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 3)
            elif field[i][j] == "0":
                pygame.draw.circle(screen, BLACK, (j * 100 + 50, i * 100 + 50), 45, 3)


# noinspection PyGlobalUndefined
def get_win_check(symbol):
    flag_win = False
    global win

    # Проверка горизонтальной линии
    for line in field:
        if line.count(symbol) == 3:
            flag_win = True
            win = [[0, field.index(line)], [1, field.index(line)], [2, field.index(line)]]

    # Проверка вертикальной линии
    for column in range(3):
        if field[0][column] == field[1][column] == field[2][column] == symbol:
            flag_win = True
            win = [[column, 0], [column, 1], [column, 2]]

    # проверка на диагональные линии
    if field[0][0] == field[1][1] == field[2][2] == symbol:
        flag_win = True
        win = [[0, 0], [1, 1], [2, 2]]
    if field[0][2] == field[1][1] == field[2][0] == symbol:
        flag_win = True
        win = [[0, 2], [1, 1], [2, 0]]
    return flag_win


game_over = False
run_game = True
while run_game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run_game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_position = pygame.mouse.get_pos()
            if field[mouse_position[1] // 100][mouse_position[0] // 100] == "":
                field[mouse_position[1] // 100][mouse_position[0] // 100] = "x"
                x, y = random.randint(0, 2), random.randint(0, 2)
                while field[x][y] != "":
                    x, y = random.randint(0, 2), random.randint(0, 2)
                field[x][y] = "0"

        player_win = get_win_check("x")
        ai_win = get_win_check("0")
        result = \
            field[0].count("x") + \
            field[0].count("0") + \
            field[1].count("x") + \
            field[1].count("0") + \
            field[2].count("x") + \
            field[2].count("0")

        if player_win or ai_win:
            game_over = True
            if player_win:
                pygame.display.set_caption("Вы победили")
            else:
                pygame.display.set_caption("Компьютер победил")
        elif result == 8:
            pygame.display.set_caption("Ничья")
            time.sleep(5)
            run_game = False

    screen.fill(WHITE)
    if game_over:
        pygame.draw.rect(screen, GREEN, (win[0][0] * 100, win[0][1] * 100, 100, 100))
        pygame.draw.rect(screen, GREEN, (win[1][0] * 100, win[1][1] * 100, 100, 100))
        pygame.draw.rect(screen, GREEN, (win[2][0] * 100, win[2][1] * 100, 100, 100))
    draw_tic_tac_toe()
    draw_grid()
    pygame.display.flip()


pygame.quit()

