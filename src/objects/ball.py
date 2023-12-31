"""Ball"""


import pygame
import settings


class Ball:
    """Ball"""
    def __init__(self, screen, x: int, y: int) -> None:
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__x_speed = -8
        self.__y_speed = -8
        self.__color = (255, 255, 155)
        self.__image = pygame.draw.circle(self.__screen, self.__color, (self.__x, self.__y), 40, 40)

    @property
    def image(self) -> pygame.rect.Rect:
        """Get ball image"""
        return self.__image

    @property
    def x(self) -> int:
        """Get ball position on x"""
        return self.__x

    def move(self) -> None:
        """Move ball"""
        self.__x -= self.__x_speed
        self.__y -= self.__y_speed

        if self.__x <= 0:
            self.__x_speed = -self.__x_speed

        if self.__x >= settings.WINDOW_SIZE[0]:
            self.__x_speed = -self.__x_speed

        if self.__y <= 0:
            self.__y_speed = -self.__y_speed

        if self.__y + self.__image.height >= settings.WINDOW_SIZE[1]:
            self.__y_speed = -self.__y_speed

        # Updating ball image
        self.__image = pygame.draw.circle(self.__screen, self.__color, (self.__x, self.__y), 40, 40)

    def push_back(self) -> None:
        """Push ball back"""
        self.__x_speed = -self.__x_speed
        self.__y_speed = self.__y_speed

        # Updating ball image
        self.__image = pygame.draw.circle(self.__screen, self.__color, (self.__x, self.__y), 40, 40)

    def draw(self) -> None:
        """Draw ball"""
        pygame.draw.circle(self.__screen, self.__color, (self.__x, self.__y), 40, 40)

