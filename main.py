import sys
import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400


def main():
    pygame.init()
    drawing_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    drawing_surface.fill(BLACK)

    while True:
        draw_grid(drawing_surface)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def draw_grid(drawing_surface):
    block_size = 20  # Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, block_size):
        for y in range(0, WINDOW_HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(drawing_surface, WHITE, rect, 1)


if __name__ == '__main__':
    main()
