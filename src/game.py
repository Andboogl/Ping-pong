"""Game module"""


import sys
import pygame
import settings
import objects


class Game:
    """Game class"""
    def __init__(self) -> None:
        """Game initialization"""
        pygame.init()

        self.__screen = pygame.display.set_mode(settings.WINDOW_SIZE)
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption(settings.WINDOW_CAPTION)
        pygame.display.set_icon(settings.WINDOW_ICON)

        self.__play_mode = 'Playing'
        self.__init()

        # Score
        self.__left_score = 0
        self.__right_score = 0
        self.__score_font = pygame.font.Font('fonts/Score-Font.ttf', 50)

        self.__pause_font = pygame.font.Font('fonts/Score-Font.ttf', 60)

    def __init(self) -> None:
        """Init game"""
        # Tables
        self.__table1 = objects.Table(self.__screen, 50, 50)
        self.__table2 = objects.Table(self.__screen, 1115, 70)

        # Ball
        self.__ball = objects.Ball(self.__screen, 500, 500)

    def mainloop(self) -> None:
        """Game mainloop"""
        while True:
            if self.__play_mode  == 'Playing':
                self.__screen.fill(settings.WINDOW_BACKGROUND_COLOR)

                # Score
                text = f'{self.__left_score} - {self.__right_score}'
                text_object = self.__score_font.render(text, True, (255, 255, 255))
                self.__screen.blit(
                    text_object,
                    (settings.WINDOW_SIZE[0] / 2 - text_object.get_width() / 2, 10)
                    )
                self.__table1.draw()
                self.__table2.draw()
                self.__ball.draw()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_s]:
                    self.__table1.move('down')

                elif keys[pygame.K_w]:
                    self.__table1.move('top')

                if keys[pygame.K_DOWN]:
                    self.__table2.move('down')

                elif keys[pygame.K_UP]:
                    self.__table2.move('top')

                if self.__ball.image.colliderect(self.__table1.image_rect) or\
                    self.__ball.image.colliderect(self.__table2.image_rect):
                    self.__ball.push_back()
                    pygame.mixer.Sound('sounds/bump.mp3').play()

                if self.__ball.x <= 0:
                    self.__right_score += 1
                    self.__init()
                    pygame.mixer.Sound('sounds/loss.mp3').play()

                elif self.__ball.x >= settings.WINDOW_SIZE[0]:
                    self.__left_score += 1
                    self.__init()
                    pygame.mixer.Sound('sounds/loss.mp3').play()

                self.__ball.move()

            if self.__play_mode == 'Pause':
                self.__screen.blit(
                    self.__pause_font.render('Pause', True, (255, 255, 255)),
                    (550, 600))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.__play_mode = 'Pause' if self.__play_mode == 'Playing' else 'Playing'

            self.__clock.tick(settings.FPS)
            pygame.display.update()

