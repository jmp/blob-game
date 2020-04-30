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

    def update(self):
        moving = False
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.move_speed
            self.direction = 1
            moving = True
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.move_speed
            self.direction = 0
            moving = True
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.move_speed
            moving = True
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.move_speed
            moving = True
        self.img = self.images[self.direction]
        if moving:
            self.img = self.images[self.direction::2][
                (pyxel.frame_count // 2) % len(self.images[self.direction::2])
            ]
