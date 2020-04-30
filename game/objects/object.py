from __future__ import annotations

from dataclasses import asdict
from typing import List

import pyxel

from ..bbox import BBox
from ..image import Image


class Object:
    images: List[Image] = []
    img: Image = None
    move_speed: int = 1
    direction: int = 0
    colkey: int = 13
    size: int = 8

    def __init__(self, x=0, y=0):
        self._x: int = x
        self._y: int = y
        self.bbox: BBox = BBox(offset_x=x, offset_y=y)

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self.bbox.offset_x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self.bbox.offset_y = value

    def draw(self):
        if self.img:
            pyxel.blt(
                **asdict(self.img),
                x=self.x,
                y=self.y,
            )

    def overlaps(self, other: Object):
        return self.bbox.overlaps(other.bbox)
