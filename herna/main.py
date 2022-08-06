import pygame
import sys
from player import Player
from chest import Chest
from chest_interface import Interface
from map import Map
from Camera import Camera
from Sprite import ScreenGroup
from Sprite import draw_frame


class Window:
    def __init__(self):
        pygame.init()
        width, height = 1280, 720
        self.display = pygame.display.set_mode((width, height))
        pygame.display.set_caption("О май гад!")
        self.player = Player(width / 2 - 22 + 200, height / 2 - 22)
        chest = Chest(1)
        self.grass = pygame.image.load("grass.png").convert()
        self.camera = Camera(width, height)
        info = {1: 'chest', 3: 'tree'}
        interface = Interface()
        # screen_walls = ScreenGroup()
        # screen_objects = ScreenGroup()
        self.clock = pygame.time.Clock()
        self.map = Map("map.tmx")
        # self.map.map_image = pygame.transform.scale(self.map.map_image, (self.map.width * 2, self.map.height * 2))

        time = 0
        sec = 0
        while True:
            time += self.clock.get_time()
            if time // 1000 == sec:
                sec += 1
                pygame.display.set_caption("fps: " + str(self.clock.get_fps()))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.player.mleft = True
                self.player.sight = 'Left'
            elif keys[pygame.K_d]:
                self.player.mright = True
                self.player.sight = 'Right'
            if keys[pygame.K_w]:
                self.player.mup = True
                self.player.sight = 'Up'
            elif keys[pygame.K_s]:
                self.player.mdown = True
                self.player.sight = 'Down'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(len(self.map.walls))
                    if event.key == pygame.K_SPACE:
                        interface.opened = bool(interface.opened ^ True)
                    if event.key == pygame.K_DOWN:
                        for sprite in self.map.walls:
                            if self.player.interaction_box.colliderect(sprite.hit_polygon):
                                if info[sprite.gid + 1] == 'tree':
                                    self.map.map_image.blit(self.grass, (sprite.rect.x, sprite.rect.y))
                                    sprite.kill()
                                break

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.player.mright = False
                    if event.key == pygame.K_a:
                        self.player.mleft = False
                    if event.key == pygame.K_w:
                        self.player.mup = False
                    if event.key == pygame.K_s:
                        self.player.mdown = False

            self.player.update()

            for sprite in self.map.walls:
                if self.player.rect.colliderect(sprite.hit_polygon):
                    if self.player.mright:
                        self.player.move(sprite.hit_polygon.left - self.player.rect.width, self.player.rect.y)
                    elif self.player.mleft:
                        self.player.move(sprite.hit_polygon.right, self.player.rect.y)
                    elif self.player.mup:
                        self.player.move(self.player.rect.x, sprite.hit_polygon.bottom)
                    elif self.player.mdown:
                        self.player.move(self.player.rect.x, sprite.hit_polygon.top - self.player.rect.height)



            self.camera.update(self.player)
            self.display.fill((0, 0, 0))
            # self.display.blit(chest.screen, (300, 300))
            draw_frame(self.display, self.camera, self.map, self.player)
            pygame.display.flip()
            self.clock.tick(60)



Window()


