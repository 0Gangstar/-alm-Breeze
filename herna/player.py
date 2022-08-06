import pygame


class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((44, 44))
        self.image.fill((114, 147, 255))
        self.rect = self.image.get_rect()
        self.image2 = pygame.Surface((64, 64))
        self.image2.fill((223, 23, 33))
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.sight = None
        # self.boxright = pygame.Rect(self.rect.right, self.rect.top, 42, self.rect.height)
        # self.boxleft = pygame.Rect(self.rect.left - 42, self.rect.top, 42, self.rect.height)
        # self.boxtop = pygame.Rect(self.rect.right, self.rect.top - 42, self.rect.width, 42)
        # self.boxbottom = pygame.Rect(self.rect.right, self.rect.bottom, self.rect.width, 42)
        self.interaction_box = pygame.Rect(self.rect.x - 10, self.rect.y - 10, 64, 64)
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False
        self.player_speed = 3

    def update(self):
        if self.mright:
            self.x += self.player_speed
        elif self.mleft:
            self.x -= self.player_speed
        elif self.mup:
            self.y -= self.player_speed
        elif self.mdown:
            self.y += self.player_speed
        self.rect.x = self.x
        self.rect.y = self.y
        self.interaction_box.x = self.rect.x - 10
        self.interaction_box.y = self.rect.y - 10

    def move(self, x, y):
        if x is not None:
            self.rect.x = x
            self.interaction_box.x = self.rect.x - 10
            self.x = x
        if y is not None:
            self.y = y
            self.rect.y = y
            self.interaction_box.y = self.rect.y - 10

    def move2(self, x, y):
        if x != None:
            self.rect.x += x
            self.interaction_box.x += x
            self.x = self.rect.x

        self.rect.y += y
        self.y = self.rect.y

        self.interaction_box.y += y
