"""Game module"""


import sys
import pygame
import settings
import objects


class Game:
    """Game class"""
    def __init__(self) -> None:
        """Game initialization"""
        self.__screen = pygame.display.set_mode(settings.WINDOW_SIZE)
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption(settings.WINDOW_CAPTION)
        pygame.display.set_icon(settings.WINDOW_ICON)

        # Tables
        self.__table1 = objects.Table(self.__screen, 50, 50)
        self.__table2 = objects.Table(self.__screen, 1115, 70)

    def mainloop(self) -> None:
        """Game mainloop"""
        while True:
            self.__screen.fill(settings.WINDOW_BACKGROUND_COLOR)
            self.__table1.draw()
            self.__table2.draw()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_s]:
                self.__table1.move('down')

            elif keys[pygame.K_w]:
                self.__table1.move('top')

            if keys[pygame.K_DOWN]:
                self.__table2.move('down')

            elif keys[pygame.K_UP]:
                self.__table2.move('top')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)


            self.__clock.tick(settings.FPS)
            pygame.display.update()

