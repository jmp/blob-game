from time import time
from typing import List

from ..bbox import BBox
from ..image import Image
from ..renderers.protocols import Renderer


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
        self.img = self.images[0]
        self.spawn_time = time()

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value
        self.bbox.offset_x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value
        self.bbox.offset_y = value

    @property
    def frame_index(self) -> int:
        return int((time() - self.spawn_time) * 50)

    def draw(self, renderer: Renderer) -> None:
        renderer.draw(self.img, self.x, self.y)

    def overlaps(self, other: "Object"):
        return self.bbox.overlaps(other.bbox)
