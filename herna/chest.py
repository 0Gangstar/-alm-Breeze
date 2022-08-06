import pygame


class Chest:
    def __init__(self, id):
        self.id = id
        self.screen = pygame.Surface((70,70))
        self.screen.fill((201, 186, 46))

    def open_storage(self, storage_id):
        pass