import pyxel

from game.image import Image
from .object import Object


class Player(Object):
    images = [
        Image(0, 0, 0, colkey=13),
        Image(0, 8, 0, colkey=13),
        Image(1, 0, 0, colkey=13),
        Image(1, 8, 0, colkey=13),
    ]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.bbox.y = 1
        self.bbox.h = 7

    def update(self):
        moving = False
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.move_speed
            if self.x < -self.bbox.x:
                self.x = -self.bbox.x
            self.direction = 1
            moving = True
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.move_speed
            max_x = pyxel.width - (self.bbox.x + self.bbox.w)
            if self.x > max_x:
                self.x = max_x
            self.direction = 0
            moving = True
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.move_speed
            if self.y < -self.bbox.y:
                self.y = -self.bbox.y
            moving = True
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.move_speed
            max_y = pyxel.height - (self.bbox.y + self.bbox.h)
            if self.y > max_y:
                self.y = max_y
            moving = True
        self.img = self.images[self.direction]
        if moving:
            self.img = self.images[self.direction::2][
                (pyxel.frame_count // 2) % len(self.images[self.direction::2])
            ]
