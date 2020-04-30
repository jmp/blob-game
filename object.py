from dataclasses import asdict
from typing import List

import pyxel

from image import Image


class Object:
    x: int = 0
    y: int = 0
    images: List[Image] = []
    img: Image = None
    move_speed: int = 1
    direction = 0
    colkey: int = 13
    size = 8

    def draw(self):
        if self.img:
            pyxel.blt(
                **asdict(self.img),
                x=self.x,
                y=self.y,
            )

    def intersects(self, x, y, w, h):
        if self.x + self.size < x:
            return False
        if self.x > x + w:
            return False
        if self.y > y + h:
            return False
        if self.y + self.size < y:
            return False
        return True
