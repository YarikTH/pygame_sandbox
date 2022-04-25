import sys
import pygame
import numpy as np
import glm
from enum import Enum


class CellType(Enum):
    FLOOR = 0
    WALL = 1
    PLAYER = 2
    DIAMOND = 3


class Direction(Enum):
    NONE = -1
    TOP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


cell_type_colors = {
    CellType.FLOOR: (200, 200, 200),
    CellType.WALL: (0, 200, 0),
    CellType.PLAYER: (200, 0, 0),
    CellType.DIAMOND: (0, 0, 200),
}


direction_offsets = {
    Direction.NONE:  glm.vec2(0,  0),
    Direction.TOP:   glm.vec2(-1, 0),
    Direction.RIGHT: glm.vec2(0,  1),
    Direction.DOWN:  glm.vec2(1,  0),
    Direction.LEFT:  glm.vec2(0,  -1),
}


game_map = np.array([
    [CellType.WALL, CellType.WALL,   CellType.WALL,  CellType.WALL,   CellType.WALL],
    [CellType.WALL, CellType.FLOOR,  CellType.FLOOR, CellType.FLOOR,  CellType.WALL],
    [CellType.WALL, CellType.PLAYER, CellType.FLOOR, CellType.FLOOR,  CellType.WALL],
    [CellType.WALL, CellType.FLOOR,  CellType.FLOOR, CellType.DIAMOND, CellType.WALL],
    [CellType.WALL, CellType.WALL,   CellType.WALL,  CellType.WALL,   CellType.WALL],
])


CELL_SIZE = 50
WINDOW_HEIGHT, WINDOW_WIDTH = tuple(x * CELL_SIZE for x in game_map.shape)
player_pos = glm.vec2(2, 1)


def game_map_element(pos):
    return game_map[int(pos.x), int(pos.y)]


def set_game_map_element(pos, value):
    game_map[int(pos.x), int(pos.y)] = value


def main():
    global player_pos
    global game_map

    pygame.init()
    drawing_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BLACK = (0, 0, 0)
    drawing_surface.fill(BLACK)

    running = True

    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                direction = Direction.NONE
                if event.key == pygame.K_w:
                    direction = Direction.TOP
                elif event.key == pygame.K_a:
                    direction = Direction.LEFT
                elif event.key == pygame.K_s:
                    direction = Direction.DOWN
                elif event.key == pygame.K_d:
                    direction = Direction.RIGHT

                if direction != Direction.NONE:
                    player_target_pos = player_pos + direction_offsets[direction]
                    player_target_cell = game_map_element(player_target_pos)
                    if player_target_cell != CellType.WALL:
                        set_game_map_element(player_pos, CellType.FLOOR)
                        set_game_map_element(player_target_pos, CellType.PLAYER)
                        player_pos = player_target_pos

        draw_grid(drawing_surface)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def draw_grid(drawing_surface):
    for i, row in enumerate(game_map):
        y = i * CELL_SIZE
        for j, cell in enumerate(row):
            x = j * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(drawing_surface, cell_type_colors[cell], rect)


if __name__ == '__main__':
    main()
