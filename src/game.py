"""Game module"""


import pygame
import settings


class Game:
    """Game class"""
    def __init__(self) -> None:
        """Game initialization"""
        self.__screen = pygame.display.set_mode(settings.WINDOW_SIZE)
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption(settings.WINDOW_CAPTION)
        pygame.display.set_icon(settings.WINDOW_ICON)

    def mainloop(self) -> None:
        """Game mainloop"""
        while True:
            self.__screen.fill(settings.WINDOW_BACKGROUND_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)

            self.__clock.tick(settings.FPS)
            pygame.display.update()
