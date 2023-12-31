"""Table"""


import pygame
import settings


class Table:
    """Table"""
    def __init__(self, screen, x: int, y: int) -> None:
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__size = (35, 200)
        self.__color = (255, 255, 255)
        self.__speed = 7

        self.__image_rect = pygame.rect.Rect(self.__x, self.__y, self.__size[0], self.__size[1])

    @property
    def image_rect(self) -> pygame.rect.Rect:
        """Get table image rect"""
        return self.__image_rect

    def move(self, where: str) -> None:
        """Move table"""
        if where == 'down':
            if self.__y + self.__image_rect.height < settings.WINDOW_SIZE[1]:
                self.__y += self.__speed
                self.__image_rect = pygame.rect.Rect(self.__x, self.__y, self.__size[0], self.__size[1])

        elif where == 'top':
            if self.__y > 0:
                self.__y -= self.__speed
                self.__image_rect = pygame.rect.Rect(self.__x, self.__y, self.__size[0], self.__size[1])

        else:
            raise ValueError

    def draw(self) -> None:
        """Draw table on the screen"""
        pygame.draw.rect(self.__screen, self.__color, self.__image_rect)

