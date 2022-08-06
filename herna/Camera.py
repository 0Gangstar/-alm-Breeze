from pygame import Rect


class Camera:
    def __init__(self, width, height):
        self.camera = Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.vel = (0, 0)

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def apply_collide(self, collide):
        return collide.hit_rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)
        # limit scrolling to map size
        # x = min(0, x)  # lef
        # y = min(0, y)  # top
        # x = max(-(self.width - width), x)  # right
        # y = max(-(self.height - height), y)  # bottom
        self.camera = Rect(x, y, self.width, self.height)