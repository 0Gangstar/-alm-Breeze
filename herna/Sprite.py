import pygame


class ScreenGroup(pygame.sprite.Group):
    def sprites_update(self, group, camera):
        cam = camera.camera
        self.empty()
        for spr in group:
            rect = spr.rect
            if rect[0] <= -cam[0] + cam[2] and rect[0] + rect[2] >= -cam[0] and rect[1] <= -cam[1] + cam[3] and rect[1] + rect[3] >= -cam[1]:
                self.add(spr)


class Wall(pygame.sprite.Sprite):
    source = None
    source_id = 2
    source_size = None

    def __init__(self, image, colliders, gid, x, y, *groups):  # с помощью супера все созданные спрайты скидываю в группу спрайтов
        self.groups = groups
        pygame.sprite.Sprite.__init__(self, *self.groups)
        self.image = image
        # print(self.texture_pos)
        self.spite_size = self.image.get_size()
        self.rect = pygame.Rect(0, 0, *self.spite_size)
        self.pos = [x, y]
        self.gid = gid
        self.rect.topleft = self.pos
        self.vel = (0, 0)
        self._layer = self.rect.bottom
        self.hit_polygon = None
        self.down_layer = None

        for collider in colliders:
            if collider.name == 'bottom_layer':
                self.down_layer = pygame.Rect(collider.x + x, collider.y + y, collider.width, collider.height)
            if collider.name is None:
                self.hit_polygon = pygame.Rect(collider.x + x, collider.y + y, collider.width, collider.height)

    def get_rect(self):
        return self.rect

    def set_sprite_pos(self, new_image):
        self.image = new_image
        self.spite_size = self.image.get_size()
        self.rect = pygame.Rect(0, 0, *self.spite_size)
        self.rect.topleft = self.pos

    def set_sprite_colliders(self, new_colliders):
        for collider in new_colliders:
            if collider.name == 'bottom_layer':
                self.down_layer = pygame.Rect(collider.x + self.pos[0], collider.y + self.pos[1], collider.width, collider.height)
            elif collider.name is None:
                try:
                    pass
                    # self.hit_polygon = Polygon(collider.points, self.pos)
                except AttributeError:
                    self.hit_polygon = pygame.Rect(collider.x + self.pos[0], collider.y + self.pos[1], collider.width, collider.height)



class Obstacle(pygame.sprite.Sprite):
    def __init__(self, object, *groups):
        print(groups)
        self.groups = groups
        pygame.sprite.Sprite.__init__(self, *self.groups)
        self.data = object
        self.gid = object.gid
        print(self.data)
        self.rect = pygame.Rect(object.x, object.y, object.width, object.height)
        self.pos = [object.x, object.y]
        # print(self.rect)
        try:
            pass
            # self.hit_polygon = Polygon(self.data.points)
        except AttributeError:
            self.hit_polygon = pygame.Rect(round(object.x), round(object.y), round(object.width), round(object.height))
        # self.hit_polygon = []
        # for points in self.data.points:
        #     self.hit_polygon.append([points[0], points[1]])
        # self.hit_polygon.append([self.data.points[0][0], self.data.points[0][1]])


def draw_frame(screen, camera, map, player):
    screen.blit(map.map_image, camera.apply_rect(map.map_rect))
    # screen.blit(player.image2, camera.apply_rect(player.interaction_box))
    screen.blit(player.image, (camera.apply(player)))
