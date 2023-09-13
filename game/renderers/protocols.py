from typing import Protocol

from ..image import Image


class Renderer(Protocol):
    def draw(self, img: Image, x: int, y: int):
        pass
