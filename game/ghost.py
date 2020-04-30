from random import randint

import pyxel

from .image import Image
from .object import Object


class Ghost(Object):
    images = [
        Image(0, 0, 16, colkey=13),
        Image(0, 8, 16, colkey=13),
        Image(1, 0, 16, colkey=13),
        Image(1, 8, 16, colkey=13),
    ]

    def __init__(self):
        self.reset()

    def reset(self):
        self.x = -8
        self.y = randint(0, pyxel.height - 8)

    def update(self):
        self.img = self.images[self.direction::2][
            (pyxel.frame_count // 2) % len(self.images[self.direction::2])
        ]
        self.x += 1
        if self.x > pyxel.width:
            self.reset()
