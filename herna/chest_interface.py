import pygame


class Interface:
    def __init__(self):
        self.screen = pygame.Surface((300,100))
        self.screen.fill((100,100,100))
        self.opened = False
