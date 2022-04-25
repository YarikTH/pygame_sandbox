import sys
import pygame
import numpy as np
from enum import Enum


class CellType(Enum):
    FLOOR = 0
    WALL = 1
    PLAYER = 2
    DIAMOND = 3


cell_type_colors = {
    CellType.FLOOR: (200, 200, 200),
    CellType.WALL: (0, 200, 0),
    CellType.PLAYER: (200, 0, 0),
    CellType.DIAMOND: (0, 0, 200),
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


def main():
    pygame.init()
    drawing_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BLACK = (0, 0, 0)
    drawing_surface.fill(BLACK)

    while True:
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
