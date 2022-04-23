# based on https://gist.github.com/nibrahim/773300
# able to draw colored python script on the screen
import pygame
from pygame.locals import *
from pygame.color import Color

from pygments.lexers import PythonLexer
from pygments.styles.zenburn import ZenburnStyle

SCREENRECT = Rect(0, 0, 1024, 700)


def create_text(screen):
    with open("scratch/pygment.py") as f:
        t = f.read()
    font = pygame.font.Font("scratch/monaco.ttf", 12)
    # font.set_bold(True)
    height = font.get_height()
    y = 0
    for i in t.split("\n"):
        x = 0
        for token, value in PythonLexer().get_tokens(i):
            colour = ZenburnStyle.style_for_token(token)['color']
            if colour:
                r, g, b = int(colour[0:2], 16), int(colour[2:4], 16), int(colour[4:6], 16)
            else:
                r = g = b = 255
            print(value, colour)
            tsurface = font.render(value.rstrip(), True, (r, g, b))
            screen.blit(tsurface, (x, y))
            x += font.size(value)[0]
        y += height


def main():
    screen = pygame.display.set_mode(SCREENRECT.size, DOUBLEBUF)
    pygame.mouse.set_visible(False)
    pygame.font.init()
    empty = pygame.Surface(SCREENRECT.size).convert()
    create_text(screen)
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            # all.clear(screen,empty)
            pygame.display.flip()


if __name__ == "__main__":
    import sys

    sys.exit(main())
