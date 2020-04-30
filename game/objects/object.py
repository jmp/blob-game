from __future__ import annotations

from dataclasses import asdict
from typing import List

import pyxel

from ..bbox import BBox
from ..image import Image


class Object:
    x: int = 0
    y: int = 0
    bbox: BBox = BBox()
    images: List[Image] = []
    img: Image = None
    move_speed: int = 1
    direction: int = 0
    colkey: int = 13
    size: int = 8

    def draw(self):
        if self.img:
            pyxel.blt(
                **asdict(self.img),
                x=self.x,
                y=self.y,
            )

    def overlaps(self, other: Object):
        bbox_self = self.bbox.at(self.x, self.y)
        bbox_other = other.bbox.at(other.x, other.y)
        return bbox_self.overlaps(bbox_other)
